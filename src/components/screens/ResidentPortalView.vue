<template>
  <div class="portal-screen resident-screen">
    <template v-if="page === 'dashboard'">
      <div class="screen-hero card">
        <div>
          <p class="eyebrow">Resident Portal</p>
          <h1>Good Morning, Priya Sharma</h1>
          <p>Here is a quick snapshot of your society activity.</p>
        </div>
        <div class="screen-avatar avatar avatar-xl">PS</div>
      </div>
      <div class="stat-grid">
        <div v-for="stat in dashboardStats" :key="stat.label" class="card stat-card">
          <div class="stat-label">{{ stat.label }}</div>
          <div class="stat-value">{{ stat.value }}</div>
        </div>
      </div>
      <div class="content-grid two-col">
        <section class="card">
          <div class="card-header"><span class="card-title">Latest Notices</span><router-link to="/resident/notices">View all</router-link></div>
          <div v-for="notice in notices.slice(0, 4)" :key="notice.id" class="list-row">
            <div>
              <strong>{{ notice.title }}</strong>
              <p>{{ notice.content }}</p>
            </div>
            <span class="badge" :class="badgeClass(notice.priority)">{{ notice.category }}</span>
          </div>
        </section>
        <section class="card">
          <div class="card-header"><span class="card-title">Quick Actions</span></div>
          <div class="action-grid">
            <router-link v-for="action in quickActions" :key="action.label" :to="action.to" class="action-card">
              <span>{{ action.icon }}</span>
              <strong>{{ action.label }}</strong>
            </router-link>
          </div>
        </section>
      </div>
      <div class="content-grid two-col">
        <section class="card">
          <div class="card-header"><span class="card-title">Upcoming Events</span><router-link to="/resident/events">View all</router-link></div>
          <div v-for="event in events.slice(0, 3)" :key="event.id" class="event-card">
            <div>
              <strong>{{ event.title }}</strong>
              <p>{{ event.date }} · {{ event.time }} · {{ event.venue }}</p>
            </div>
            <button class="btn btn-primary btn-sm">Join</button>
          </div>
        </section>
        <section class="card">
          <div class="card-header"><span class="card-title">Recent Notices</span></div>
          <div v-for="notice in notices.slice(0, 3)" :key="notice.id + '-recent'" class="list-row compact">
            <div>
              <strong>{{ notice.title }}</strong>
              <p>{{ notice.date }}</p>
            </div>
          </div>
        </section>
      </div>
    </template>

    <template v-else-if="page === 'notices'">
      <div class="screen-header">
        <h1>Notice Board</h1>
        <p>Read society announcements, maintenance updates, and important circulars.</p>
      </div>
      <div class="chip-row">
        <span v-for="chip in ['All', 'Maintenance', 'Events', 'Rules']" :key="chip" class="chip">{{ chip }}</span>
      </div>
      <div class="stack">
        <article v-for="notice in notices" :key="notice.id" class="card notice-card">
          <div class="card-header no-border">
            <strong>{{ notice.title }}</strong>
            <span class="badge" :class="badgeClass(notice.priority)">{{ notice.priority }}</span>
          </div>
          <p>{{ notice.content }}</p>
          <small>{{ notice.date }} · {{ notice.category }}</small>
        </article>
      </div>
    </template>

    <template v-else-if="page === 'events'">
      <div class="screen-header">
        <h1>Upcoming Events</h1>
        <p>Community activities, celebrations, and wellness sessions.</p>
      </div>
      <div class="card-grid three-col">
        <article v-for="event in events" :key="event.id" class="card event-tile">
          <div class="tile-visual">{{ event.category }}</div>
          <h3>{{ event.title }}</h3>
          <p>{{ event.date }} · {{ event.time }}</p>
          <p>{{ event.venue }}</p>
          <button class="btn btn-primary btn-sm">Register / Join Event</button>
        </article>
      </div>
    </template>

    <template v-else-if="page === 'complaints'">
      <div class="screen-header row-between">
        <div>
          <h1>My Complaints</h1>
          <p>Track your raised issues and their current resolution status.</p>
        </div>
        <router-link to="/resident/complaints/new" class="btn btn-primary">New Complaint</router-link>
      </div>
      <div class="table-wrap card">
        <table class="data-table">
          <thead><tr><th>#</th><th>Title</th><th>Category</th><th>Status</th><th>Date</th></tr></thead>
          <tbody>
            <tr v-for="complaint in complaints" :key="complaint.id">
              <td>{{ complaint.id }}</td>
              <td><router-link :to="`/resident/complaints/${complaint.id}`">{{ complaint.title }}</router-link></td>
              <td>{{ complaint.category }}</td>
              <td><span class="badge" :class="badgeClass(complaint.status)">{{ complaint.status }}</span></td>
              <td>{{ complaint.date }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </template>

    <template v-else-if="page === 'raise-complaint'">
      <div class="screen-header">
        <h1>Raise Complaint</h1>
        <p>Submit a new issue for the maintenance or management team.</p>
      </div>
      <form class="card form-card" @submit.prevent="submitComplaint">
        <div class="form-grid two-col">
          <label class="form-group"><span class="form-label">Category</span><select v-model="complaintForm.category"><option>Plumbing</option><option>Electrical</option><option>Maintenance</option><option>Security</option></select></label>
          <label class="form-group"><span class="form-label">Title</span><input v-model="complaintForm.title" type="text" placeholder="Short issue title" /></label>
        </div>
        <label class="form-group"><span class="form-label">Description</span><textarea v-model="complaintForm.description" rows="5" placeholder="Describe the issue"></textarea></label>
        <label class="form-group"><span class="form-label">Upload Image</span><input type="file" /></label>
        <button class="btn btn-primary">Submit Complaint</button>
      </form>
    </template>

    <template v-else-if="page === 'complaint-details'">
      <div class="screen-header">
        <h1>Complaint ID: C-034</h1>
        <p>Complaint details, assignment progress, and updates.</p>
      </div>
      <div class="content-grid two-col">
        <section class="card">
          <div class="detail-list">
            <div v-for="item in complaintDetails" :key="item.label" class="detail-row"><span>{{ item.label }}</span><strong>{{ item.value }}</strong></div>
          </div>
          <p class="detail-copy">Water leakage in the bathroom tap from the past two days.</p>
        </section>
        <section class="card">
          <h3 class="card-title">Timeline</h3>
          <div v-for="step in timeline" :key="step.label" class="timeline-row">
            <span class="timeline-dot" :class="step.done ? 'done' : ''"></span>
            <div><strong>{{ step.label }}</strong><p>{{ step.value }}</p></div>
          </div>
        </section>
      </div>
    </template>

    <template v-else-if="page === 'browse-services'">
      <div class="screen-header">
        <h1>Browse Services</h1>
        <p>Choose a trusted service provider category.</p>
      </div>
      <div class="card-grid three-col">
        <article v-for="provider in serviceCategories" :key="provider.id" class="card service-tile">
          <div class="service-icon">{{ provider.icon }}</div>
          <h3>{{ provider.name }}</h3>
          <p>{{ provider.description }}</p>
          <router-link to="/resident/services/provider/1" class="btn btn-outline btn-sm">View providers</router-link>
        </article>
      </div>
    </template>

    <template v-else-if="page === 'provider-details'">
      <div class="content-grid two-col align-start">
        <section class="card provider-card">
          <div class="provider-top">
            <div class="avatar avatar-xl">RP</div>
            <div>
              <h1>Ravi Plumber</h1>
              <p>5 years experience · Plumbing expert</p>
              <div class="stars">{{ stars(4.5).join(' ') }}</div>
            </div>
          </div>
          <p>Experienced plumber specializing in bathroom repairs, pipe fitting, and drainage solutions.</p>
          <button class="btn btn-primary">Book Now</button>
        </section>
        <section class="card">
          <h3 class="card-title">Services & Availability</h3>
          <div v-for="service in serviceRates" :key="service.name" class="list-row compact"><strong>{{ service.name }}</strong><span>{{ service.price }}</span></div>
          <div class="chip-row"><span v-for="slot in availability" :key="slot" class="chip">{{ slot }}</span></div>
        </section>
      </div>
    </template>

    <template v-else-if="page === 'booking-calendar'">
      <div class="screen-header">
        <h1>Booking Calendar</h1>
        <p>Select your preferred date and time slot.</p>
      </div>
      <div class="card calendar-card">
        <div class="calendar-grid">
          <button v-for="day in calendarDays" :key="day" class="calendar-day" :class="{ active: day === 14 }">{{ day }}</button>
        </div>
        <div class="chip-row">
          <span v-for="slot in timeSlots" :key="slot" class="chip">{{ slot }}</span>
        </div>
      </div>
    </template>

    <template v-else-if="page === 'my-bookings'">
      <div class="screen-header">
        <h1>My Bookings</h1>
        <p>Review upcoming, completed, and cancelled bookings.</p>
      </div>
      <div class="chip-row"><span v-for="tab in ['Upcoming', 'Completed', 'Cancelled']" :key="tab" class="chip">{{ tab }}</span></div>
      <div class="stack">
        <article v-for="booking in bookings" :key="booking.id" class="card booking-card">
          <div><strong>{{ booking.facility }}</strong><p>{{ booking.date }} · {{ booking.time }}</p></div>
          <span class="badge" :class="badgeClass(booking.status)">{{ booking.status }}</span>
        </article>
      </div>
    </template>

    <template v-else-if="page === 'parking'">
      <div class="content-grid two-col">
        <section class="card">
          <h1>My Parking</h1>
          <p>Assigned slot: <strong>B-102</strong> · Flat: <strong>A-101</strong></p>
          <button class="btn btn-primary">Download Pass</button>
        </section>
        <section class="card">
          <h3 class="card-title">Visitor Parking</h3>
          <div class="parking-grid small">
            <div v-for="slot in visitorSlots" :key="slot.id" class="parking-slot" :class="slot.status.toLowerCase()">{{ slot.id }}</div>
          </div>
        </section>
      </div>
    </template>

    <template v-else-if="page === 'visitor-parking'">
      <div class="screen-header">
        <h1>Visitor Parking</h1>
        <p>Book temporary parking for visitors and guests.</p>
      </div>
      <div class="content-grid two-col">
        <form class="card form-card" @submit.prevent="notify.success('Visitor parking booked')">
          <label class="form-group"><span class="form-label">Visitor Name</span><input type="text" placeholder="Enter visitor name" /></label>
          <label class="form-group"><span class="form-label">Vehicle Number</span><input type="text" placeholder="Vehicle registration" /></label>
          <button class="btn btn-primary">Book Slot</button>
        </form>
        <section class="card">
          <h3 class="card-title">Available Slots</h3>
          <div class="parking-grid small">
            <div v-for="slot in visitorSlots" :key="slot.id + 'v'" class="parking-slot" :class="slot.status.toLowerCase()">{{ slot.id }}</div>
          </div>
        </section>
      </div>
    </template>

    <template v-else-if="page === 'family'">
      <div class="screen-header row-between">
        <div><h1>My Family</h1><p>Keep family members and emergency contacts updated.</p></div>
        <button class="btn btn-primary">Add Member</button>
      </div>
      <div class="stack">
        <article v-for="member in familyMembers" :key="member.id" class="card member-card">
          <div class="avatar">{{ member.name.split(' ').map(part => part[0]).join('') }}</div>
          <div><strong>{{ member.name }}</strong><p>{{ member.relation }}</p></div>
        </article>
      </div>
    </template>

    <template v-else-if="page === 'notifications'">
      <div class="screen-header">
        <h1>Notifications</h1>
        <p>Complaint updates, booking confirmations, and maintenance alerts.</p>
      </div>
      <div class="stack">
        <article v-for="notification in notifications" :key="notification.id" class="card notification-card">
          <small>{{ notification.date }}</small>
          <strong>{{ notification.title }}</strong>
          <p>{{ notification.description }}</p>
        </article>
      </div>
    </template>

    <template v-else-if="page === 'profile'">
      <div class="content-grid two-col">
        <section class="card profile-card">
          <div class="avatar avatar-xl">PS</div>
          <h1>Priya Sharma</h1>
          <p>A-101 · Green Valley Society</p>
          <button class="btn btn-outline">Edit Profile</button>
        </section>
        <section class="card">
          <h3 class="card-title">Contact Details</h3>
          <div class="detail-list">
            <div class="detail-row"><span>Phone</span><strong>9876543210</strong></div>
            <div class="detail-row"><span>Email</span><strong>priya.sharma@email.com</strong></div>
          </div>
        </section>
      </div>
    </template>

    <template v-else-if="page === 'book-amenities'">
      <div class="content-grid two-col align-start">
        <form class="card form-card" @submit.prevent="notify.success('Amenity booking submitted')">
          <div class="form-grid two-col">
            <label class="form-group"><span class="form-label">Facility</span><select><option>Club House</option><option>Gym</option><option>Swimming Pool</option><option>Community Hall</option></select></label>
            <label class="form-group"><span class="form-label">Date</span><input type="date" /></label>
          </div>
          <div class="form-grid two-col">
            <label class="form-group"><span class="form-label">Time Slot</span><select><option>09:00 AM - 10:00 AM</option><option>10:00 AM - 11:00 AM</option><option>04:00 PM - 05:00 PM</option></select></label>
            <label class="form-group"><span class="form-label">Purpose</span><input type="text" placeholder="Enter purpose" /></label>
          </div>
          <button class="btn btn-primary">Book Now</button>
        </form>
        <section class="card">
          <h3 class="card-title">My Bookings</h3>
          <div v-for="booking in bookings.slice(0, 3)" :key="booking.id + 'amenity'" class="list-row compact"><strong>{{ booking.facility }}</strong><span>{{ booking.status }}</span></div>
        </section>
      </div>
    </template>

    <template v-else-if="page === 'help-support'">
      <div class="screen-header">
        <h1>Help & Support</h1>
        <p>Browse frequently asked questions or reach out to the society team.</p>
      </div>
      <div class="content-grid two-col">
        <section class="card">
          <h3 class="card-title">FAQs</h3>
          <div v-for="faq in faqs" :key="faq.id" class="faq-item">
            <strong>{{ faq.question }}</strong>
            <p>{{ faq.answer }}</p>
          </div>
        </section>
        <section class="card">
          <h3 class="card-title">Contact Us</h3>
          <p>Phone: +91 98765 43210</p>
          <p>Email: support@socioneed.com</p>
        </section>
      </div>
    </template>

    <template v-else-if="page === 'maintenance-bills'">
      <div class="screen-header">
        <h1>Maintenance Bills</h1>
        <p>Track monthly charges and payment status.</p>
      </div>
      <div class="stack">
        <article v-for="bill in maintenanceBills" :key="bill.id" class="card bill-card">
          <div><strong>{{ bill.month }}</strong><p>Due {{ bill.dueDate }}</p></div>
          <div class="bill-meta"><strong>{{ currency(bill.amount) }}</strong><span class="badge" :class="badgeClass(bill.status)">{{ bill.status }}</span></div>
        </article>
      </div>
    </template>

    <template v-else-if="page === 'service-history'">
      <div class="screen-header">
        <h1>Service History</h1>
        <p>Review past service requests and completed jobs.</p>
      </div>
      <div class="stack">
        <article v-for="booking in bookings" :key="booking.id + 'history'" class="card history-card">
          <div><strong>{{ booking.facility }}</strong><p>{{ booking.purpose }}</p></div>
          <span class="badge" :class="badgeClass(booking.status)">{{ booking.status }}</span>
        </article>
      </div>
    </template>
  </div>
</template>

<script setup>
import { computed, reactive } from 'vue'
import { useRoute } from 'vue-router'
import { useNotificationStore } from '@/stores/notificationStore'
import {
  bookings,
  complaints,
  events,
  familyMembers,
  faqs,
  maintenanceBills,
  notices,
  parkingSlots,
  serviceCategories,
} from '@/data/mockData'
import { badgeClass, currency, days, stars } from './screenUtils'

const route = useRoute()
const notify = useNotificationStore()
const page = computed(() => route.meta.page || 'dashboard')

const complaintForm = reactive({ category: 'Plumbing', title: '', description: '' })

const dashboardStats = [
  { label: 'My Complaints', value: complaints.length },
  { label: 'My Bookings', value: bookings.length },
  { label: 'Upcoming Events', value: events.length },
  { label: 'New Notices', value: notices.length },
]

const quickActions = [
  { label: 'Raise Complaint', icon: '📝', to: '/resident/complaints/new' },
  { label: 'Book Service', icon: '🛠️', to: '/resident/services' },
  { label: 'Pay Parking', icon: '🅿️', to: '/resident/parking' },
  { label: 'My Family', icon: '👪', to: '/resident/family' },
]

const complaintDetails = [
  { label: 'Category', value: 'Plumbing' },
  { label: 'Status', value: 'In Progress' },
  { label: 'Assigned To', value: 'Maintenance Team' },
  { label: 'Date', value: '2024-05-20' },
]

const timeline = [
  { label: 'Submitted', value: 'Complaint created', done: true },
  { label: 'Assigned', value: 'Maintenance team notified', done: true },
  { label: 'In Progress', value: 'Technician working on issue', done: true },
  { label: 'Resolved', value: 'Pending completion', done: false },
]

const serviceRates = [
  { name: 'Plumbing Work', price: '₹500 - ₹2000' },
  { name: 'Pipe Fitting', price: '₹300 - ₹1500' },
  { name: 'Bathroom Repair', price: '₹800 - ₹3000' },
]

const availability = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
const calendarDays = days(30)
const timeSlots = ['08:00', '09:00', '10:00', '11:00', '14:00', '15:00']
const visitorSlots = parkingSlots.filter(slot => slot.block === 'B').slice(0, 5)

function submitComplaint() {
  notify.success('Complaint submitted successfully')
  complaintForm.title = ''
  complaintForm.description = ''
}
</script>

<style scoped>
.portal-screen { display: grid; gap: var(--space-6); }
.screen-hero { display: flex; align-items: center; justify-content: space-between; gap: var(--space-6); }
.eyebrow { text-transform: uppercase; letter-spacing: 0.08em; font-size: var(--text-xs); color: var(--color-primary); font-weight: var(--font-semibold); margin-bottom: var(--space-2); }
.screen-hero h1, .screen-header h1 { margin-bottom: var(--space-2); }
.screen-hero p, .screen-header p { color: var(--color-text-secondary); }
.screen-avatar { background: linear-gradient(135deg, var(--color-primary-100), var(--color-info-100)); color: var(--color-primary); }
.stat-grid, .card-grid, .action-grid, .content-grid { display: grid; gap: var(--space-4); }
.stat-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.stat-card { padding: var(--space-5); }
.stat-label { font-size: var(--text-sm); color: var(--color-text-secondary); }
.stat-value { font-size: var(--text-3xl); font-weight: var(--font-bold); margin-top: var(--space-2); }
.content-grid.two-col { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.card-grid.three-col { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.list-row, .event-card, .booking-card, .notification-card, .bill-card, .history-card, .member-card, .faq-item { display: flex; align-items: center; justify-content: space-between; gap: var(--space-4); }
.list-row, .event-card, .booking-card, .notification-card, .bill-card, .history-card, .member-card { padding: var(--space-4) 0; border-bottom: 1px solid var(--color-border); }
.list-row:last-child, .event-card:last-child, .booking-card:last-child, .notification-card:last-child, .bill-card:last-child, .history-card:last-child, .member-card:last-child { border-bottom: none; }
.compact { padding: var(--space-3) 0; }
.action-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.action-card { display: grid; gap: var(--space-2); padding: var(--space-5); border: 1px solid var(--color-border); border-radius: var(--radius-lg); background: var(--color-gray-50); color: inherit; }
.chip-row { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.chip { padding: 6px 12px; border-radius: var(--radius-full); background: var(--color-gray-100); color: var(--color-text-secondary); font-size: var(--text-xs); }
.stack { display: grid; gap: var(--space-4); }
.tile-visual, .service-icon { width: 64px; height: 64px; display: grid; place-items: center; border-radius: var(--radius-lg); background: var(--color-primary-50); color: var(--color-primary); font-weight: var(--font-semibold); }
.provider-top { display: flex; align-items: center; gap: var(--space-4); margin-bottom: var(--space-4); }
.stars { color: var(--color-accent-dark); letter-spacing: 2px; }
.calendar-grid { display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 10px; margin-bottom: var(--space-4); }
.calendar-day { padding: var(--space-3); border-radius: var(--radius-md); background: var(--color-gray-50); border: 1px solid var(--color-border); }
.calendar-day.active { background: var(--color-primary); color: white; }
.parking-grid.small { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: var(--space-3); }
.parking-slot { padding: var(--space-3); text-align: center; border-radius: var(--radius-md); border: 1px solid var(--color-border); background: var(--color-gray-50); }
.parking-slot.available { background: var(--color-secondary-50); color: var(--color-secondary-dark); }
.parking-slot.occupied { background: var(--color-danger-50); color: var(--color-danger-dark); }
.parking-slot.reserved { background: var(--color-accent-50); color: var(--color-accent-dark); }
.detail-list { display: grid; gap: var(--space-3); }
.detail-row { display: flex; justify-content: space-between; gap: var(--space-4); }
.timeline-row { display: flex; gap: var(--space-3); margin-top: var(--space-4); }
.timeline-dot { width: 12px; height: 12px; margin-top: 6px; border-radius: 50%; background: var(--color-border); }
.timeline-dot.done { background: var(--color-primary); }
.form-card { display: grid; gap: var(--space-4); }
.form-grid.two-col { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-4); }
.screen-header.row-between { display: flex; align-items: center; justify-content: space-between; gap: var(--space-4); }
.profile-card { text-align: center; }
.provider-card, .profile-card { align-items: flex-start; }
.faq-item { display: block; padding: var(--space-4) 0; border-bottom: 1px solid var(--color-border); }
.faq-item:last-child { border-bottom: none; }
.bill-meta { display: grid; justify-items: end; gap: var(--space-2); }
.align-start { align-items: start; }
@media (max-width: 960px) {
  .stat-grid, .content-grid.two-col, .card-grid.three-col { grid-template-columns: 1fr; }
  .screen-hero, .screen-header.row-between, .provider-top { flex-direction: column; align-items: flex-start; }
  .form-grid.two-col { grid-template-columns: 1fr; }
}
</style>