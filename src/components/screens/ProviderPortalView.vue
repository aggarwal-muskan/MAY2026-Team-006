<template>
  <div class="portal-screen provider-screen">
    <template v-if="page === 'dashboard'">
      <div class="screen-header"><h1>Service Provider Dashboard</h1><p>Track bookings, earnings, and today's schedule.</p></div>
      <div class="stat-grid provider-stats">
        <div v-for="stat in providerStats" :key="stat.label" class="card stat-card"><div class="stat-label">{{ stat.label }}</div><div class="stat-value">{{ stat.value }}</div></div>
      </div>
      <div class="content-grid two-col">
        <section class="card"><h3 class="card-title">Today's Schedule</h3><div v-for="booking in providerBookings.slice(0, 3)" :key="booking.id" class="list-row"><div><strong>{{ booking.customer }}</strong><p>{{ booking.service }} · {{ booking.time }}</p></div><span class="badge" :class="badgeClass(booking.status)">{{ booking.status }}</span></div></section>
        <section class="card"><h3 class="card-title">Quick Actions</h3><div class="chip-row"><router-link to="/provider/services" class="chip-link">Update Services</router-link><router-link to="/provider/availability" class="chip-link">Edit Availability</router-link><router-link to="/provider/earnings" class="chip-link">View Earnings</router-link></div></section>
      </div>
    </template>

    <template v-else-if="page === 'bookings'">
      <div class="screen-header"><h1>Bookings</h1><p>Accept or reject incoming requests.</p></div>
      <div class="chip-row"><span v-for="tab in ['Pending Requests', 'Booking History']" :key="tab" class="chip">{{ tab }}</span></div>
      <div class="stack"><article v-for="booking in providerBookings" :key="booking.id" class="card booking-card"><div><strong>{{ booking.customer }}</strong><p>{{ booking.service }} · {{ booking.date }}</p></div><div class="row-actions"><button class="btn btn-secondary btn-sm">Accept</button><button class="btn btn-outline btn-sm">Reject</button></div></article></div>
    </template>

    <template v-else-if="page === 'availability'">
      <div class="screen-header"><h1>Availability</h1><p>Set working days and time slots.</p></div>
      <div class="card"><div class="chip-row"><span v-for="day in weekDays" :key="day" class="chip">{{ day }}</span></div><div class="time-grid"><button v-for="slot in timeSlots" :key="slot" class="time-slot">{{ slot }}</button></div></div>
    </template>

    <template v-else-if="page === 'services'">
      <div class="screen-header row-between"><div><h1>Services List</h1><p>Manage your service catalog and pricing.</p></div><button class="btn btn-primary">Add Service</button></div>
      <div class="stack"><article v-for="service in providerServices" :key="service.name" class="card service-row"><div><strong>{{ service.name }}</strong><p>{{ service.price }}</p></div><button class="btn btn-outline btn-sm">Edit</button></article></div>
    </template>

    <template v-else-if="page === 'reviews'">
      <div class="screen-header"><h1>Reviews</h1><p>See customer feedback and service quality.</p></div>
      <div class="content-grid two-col"><section class="card rating-card"><div class="rating-value">4.7</div><div class="stars">★★★★★</div><p>Average rating across recent bookings.</p></section><section class="card"><article v-for="review in reviews" :key="review.id" class="review-row"><strong>{{ review.customer }}</strong><span>{{ stars(review.rating).join(' ') }}</span><p>{{ review.comment }}</p></article></section></div>
    </template>

    <template v-else-if="page === 'earnings'">
      <div class="screen-header"><h1>Earnings</h1><p>Monitor income across the current month and lifetime.</p></div>
      <div class="stat-grid provider-stats"><div class="card stat-card"><div class="stat-label">This Month</div><div class="stat-value">₹12,450</div></div><div class="card stat-card"><div class="stat-label">Total</div><div class="stat-value">₹1,24,500</div></div></div>
      <div class="card"><div v-for="entry in earningsBreakdown" :key="entry.label" class="progress-row"><span>{{ entry.label }}</span><div class="progress"><span :style="{ width: `${entry.value}%` }"></span></div></div></div>
    </template>

    <template v-else-if="page === 'profile'">
      <div class="content-grid two-col"><section class="card profile-card"><div class="avatar avatar-xl">RP</div><h1>Ravi Plumber</h1><p>Plumber · 5 years experience</p><button class="btn btn-outline">Edit</button></section><section class="card"><h3 class="card-title">Contact</h3><p>Phone: 9111222333</p><p>Email: ravi.plumber@email.com</p></section></div>
    </template>

    <template v-else-if="page === 'notifications'">
      <div class="screen-header"><h1>Notifications</h1><p>New booking alerts and updates.</p></div>
      <div class="stack"><article v-for="note in providerNotifications" :key="note" class="card note-card">{{ note }}</article></div>
    </template>

    <template v-else-if="page === 'settings'">
      <div class="screen-header"><h1>Settings</h1><p>Manage provider preferences.</p></div>
      <form class="card form-card"><label class="switch-row"><span>SMS alerts</span><input type="checkbox" checked /></label><label class="switch-row"><span>Email summaries</span><input type="checkbox" checked /></label><label class="switch-row"><span>Language</span><select><option>English</option><option>Hindi</option></select></label></form>
    </template>

    <template v-else-if="page === 'help'">
      <div class="screen-header"><h1>Help & Support</h1><p>FAQs and support contact.</p></div>
      <div class="content-grid two-col"><section class="card"><div v-for="faq in faqs" :key="faq.id" class="faq-item"><strong>{{ faq.question }}</strong><p>{{ faq.answer }}</p></div></section><section class="card"><h3 class="card-title">Contact support</h3><p>support@socioneed.com</p><p>+91 98765 43210</p></section></div>
    </template>

    <template v-else-if="page === 'customer-history'">
      <div class="screen-header"><h1>Customer History</h1><p>Past customers and request history.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Customer</th><th>Service</th><th>Date</th><th>Status</th></tr></thead><tbody><tr v-for="booking in providerBookings" :key="booking.id + 'history'"><td>{{ booking.customer }}</td><td>{{ booking.service }}</td><td>{{ booking.date }}</td><td><span class="badge" :class="badgeClass(booking.status)">{{ booking.status }}</span></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'completed-jobs'">
      <div class="screen-header"><h1>Completed Jobs</h1><p>Finished work and service outcomes.</p></div>
      <div class="stack"><article v-for="booking in providerBookings.filter(item => item.status === 'Completed')" :key="booking.id" class="card completed-row"><strong>{{ booking.customer }}</strong><p>{{ booking.service }} · {{ booking.amount }}</p></article></div>
    </template>

    <template v-else-if="page === 'payouts'">
      <div class="screen-header"><h1>Payouts</h1><p>Payout summary and transfer history.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Period</th><th>Amount</th><th>Status</th></tr></thead><tbody><tr><td>This Week</td><td>₹4,500</td><td><span class="badge badge-success">Processed</span></td></tr><tr><td>Last Week</td><td>₹3,250</td><td><span class="badge badge-success">Processed</span></td></tr></tbody></table></div>
    </template>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { faqs, providerBookings, reviews } from '@/data/mockData'
import { badgeClass, stars } from './screenUtils'

const route = useRoute()
const page = computed(() => route.meta.page || 'dashboard')

const providerStats = [
  { label: 'Today Bookings', value: 3 },
  { label: 'Pending Requests', value: 2 },
  { label: 'Completed', value: 18 },
  { label: 'Rating', value: '4.7' },
]

const weekDays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
const timeSlots = ['08:00', '09:00', '10:00', '11:00', '14:00', '15:00', '16:00']
const providerServices = [
  { name: 'Plumbing Work', price: '₹500 - ₹2000' },
  { name: 'Pipe Fitting', price: '₹300 - ₹1500' },
  { name: 'Bathroom Repair', price: '₹800 - ₹3000' },
]
const providerNotifications = ['New booking from Priya Sharma', 'Cancellation request from Rahul Verma', '2 new review notifications']
const earningsBreakdown = [
  { label: 'Plumbing', value: 78 },
  { label: 'Pipe Fitting', value: 62 },
  { label: 'Repairs', value: 88 },
]
</script>

<style scoped>
.portal-screen { display: grid; gap: var(--space-6); }
.screen-header { display: grid; gap: var(--space-2); }
.screen-header h1 { margin: 0; }
.screen-header p { color: var(--color-text-secondary); }
.screen-header.row-between { display: flex; justify-content: space-between; align-items: center; gap: var(--space-4); }
.stat-grid, .content-grid { display: grid; gap: var(--space-4); }
.stat-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.provider-stats .stat-value { font-size: var(--text-3xl); font-weight: var(--font-bold); margin-top: var(--space-2); }
.content-grid.two-col { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.list-row, .booking-card, .service-row, .review-row, .completed-row, .note-card, .faq-item { padding: var(--space-4) 0; border-bottom: 1px solid var(--color-border); }
.list-row:last-child, .booking-card:last-child, .service-row:last-child, .review-row:last-child, .completed-row:last-child, .note-card:last-child, .faq-item:last-child { border-bottom: none; }
.chip-row { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.chip, .chip-link { padding: 6px 12px; border-radius: var(--radius-full); background: var(--color-gray-100); color: var(--color-text-secondary); text-decoration: none; }
.time-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: var(--space-3); margin-top: var(--space-4); }
.time-slot { padding: var(--space-3); border: 1px solid var(--color-border); border-radius: var(--radius-md); background: var(--color-gray-50); }
.rating-card { display: grid; gap: var(--space-3); align-items: start; }
.rating-value { font-size: 3rem; font-weight: var(--font-bold); color: var(--color-primary); }
.stars { color: var(--color-accent-dark); }
.progress-row { display: grid; gap: var(--space-2); margin-bottom: var(--space-4); }
.progress { height: 10px; border-radius: var(--radius-full); background: var(--color-gray-100); overflow: hidden; }
.progress span { display: block; height: 100%; background: linear-gradient(90deg, var(--color-secondary), var(--color-primary)); }
.form-card { display: grid; gap: var(--space-4); }
.switch-row { display: flex; justify-content: space-between; gap: var(--space-4); align-items: center; }
.profile-card { text-align: center; }
.table-wrap { overflow-x: auto; }
@media (max-width: 960px) { .stat-grid, .content-grid.two-col, .time-grid { grid-template-columns: 1fr; } .screen-header.row-between { flex-direction: column; align-items: flex-start; } }
</style>