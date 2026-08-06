<template>
  <div class="portal-screen provider-screen">
    <template v-if="page === 'dashboard'">
      <div class="dashboard-shell">
      <div class="screen-header"><h1>Service Provider Dashboard</h1><p>Track bookings, earnings, and today's schedule.</p></div>
      <div class="stat-grid provider-stats">
        <div v-for="stat in providerStats" :key="stat.label" class="card stat-card"><div class="stat-label">{{ stat.label }}</div><div class="stat-value">{{ stat.value }}</div></div>
      </div>
      <div class="content-grid two-col">
        <section class="card"><h3 class="card-title">Today's Schedule</h3><div v-for="booking in filteredProviderBookings.slice(0, 3)" :key="booking.id" class="list-row"><div><strong>{{ booking.resident_name || `Resident #${booking.resident_user_id}` }}</strong><p>{{ booking.request_notes || 'Service request' }} · {{ booking.created_at || '-' }}</p></div><span class="badge" :class="badgeClass(booking.booking_status || booking.status)">{{ booking.booking_status || booking.status }}</span></div></section>
        <section class="card"><h3 class="card-title">Quick Actions</h3><div class="chip-row"><router-link to="/provider/services" class="chip-link">Update Services</router-link><router-link to="/provider/availability" class="chip-link">Edit Availability</router-link><router-link to="/provider/earnings" class="chip-link">View Earnings</router-link></div></section>
      </div>
      </div>
    </template>

    <template v-else-if="page === 'bookings'">
      <div class="screen-header"><h1>Bookings</h1><p>Accept or reject incoming requests.</p></div>
      <div class="chip-row">
        <span class="chip">Pending Requests ({{ pendingRequestsCount }})</span>
        <span class="chip">Booking History ({{ bookingHistoryCount }})</span>
      </div>
      <div class="stack"><article v-for="booking in orderedProviderBookings" :key="booking.id" class="card booking-card"><div><strong>{{ booking.resident_name || `Resident #${booking.resident_user_id}` }}</strong><p>{{ booking.request_notes || 'Service request' }} · {{ booking.created_at || '-' }}</p></div><div class="row-actions"><button v-if="canAcceptBooking(booking)" class="btn btn-secondary btn-sm" :disabled="Boolean(actionBookingIds[booking.id])" @click="acceptProviderBooking(booking.id)">Accept</button><button v-if="canDeclineBooking(booking)" class="btn btn-outline btn-sm" :disabled="Boolean(actionBookingIds[booking.id])" @click="declineProviderBooking(booking.id)">Reject</button><button v-if="canCompleteBooking(booking)" class="btn btn-primary btn-sm" :disabled="Boolean(actionBookingIds[booking.id])" @click="completeProviderBooking(booking.id)">Complete</button><span v-if="!canAcceptBooking(booking) && !canDeclineBooking(booking) && !canCompleteBooking(booking)" class="chip">No actions</span></div></article></div>
    </template>

    <template v-else-if="page === 'availability'">
      <div class="screen-header"><h1>Availability</h1><p>Set working days and time slots.</p></div>
      <div class="card form-card">
        <div class="form-grid two-col">
          <label class="form-group"><span class="form-label">Start</span><input v-model="slotForm.slot_start" type="datetime-local" /></label>
          <label class="form-group"><span class="form-label">End</span><input v-model="slotForm.slot_end" type="datetime-local" /></label>
        </div>
        <button class="btn btn-primary" @click="addAvailabilitySlot">Add Slot</button>
      </div>
      <div class="card">
        <h3 class="card-title">My Slots</h3>
        <div v-if="providerSlots.length === 0" class="list-row">No slots added yet.</div>
        <div v-for="slot in providerSlots" :key="slot.id" class="list-row">
          <div>
            <strong>{{ formatDateTime(slot.slot_start) }} - {{ formatDateTime(slot.slot_end) }}</strong>
            <p>{{ slot.is_available ? 'Available' : 'Unavailable' }}</p>
          </div>
          <button class="btn btn-danger btn-sm" @click="removeAvailabilitySlot(slot.id)">Delete</button>
        </div>
      </div>
    </template>

    <template v-else-if="page === 'services'">
      <div class="screen-header row-between"><div><h1>Services List</h1><p>Manage your service catalog and pricing.</p></div><button class="btn btn-primary" @click="saveProviderService">Save Service</button></div>
      <form class="card form-card" @submit.prevent="saveProviderService">
        <label class="form-group"><span class="form-label">Business Name</span><input v-model="serviceForm.business_name" type="text" /></label>
        <label class="form-group"><span class="form-label">Service Description</span><textarea v-model="serviceForm.service_description" rows="4"></textarea></label>
        <button class="btn btn-primary">Update Service</button>
      </form>

      <section class="card">
        <h3 class="card-title">Provided Services</h3>
        <div v-if="providerServiceItems.length === 0" class="list-row">No services available yet. Add service details and save.</div>
        <div v-else class="stack">
          <article v-for="service in providerServiceItems" :key="service.name" class="service-row row-between">
            <div>
              <strong>{{ service.name }}</strong>
              <p>{{ service.description || 'Standard service offering' }}</p>
            </div>
            <span class="chip">{{ service.price }}</span>
          </article>
        </div>
      </section>
    </template>

    <template v-else-if="page === 'reviews'">
      <div class="screen-header"><h1>Reviews</h1><p>See customer feedback and service quality.</p></div>
      <div class="content-grid two-col"><section class="card rating-card"><div class="rating-value">{{ Number(providerStatsLive.rating_avg || 0).toFixed(1) }}</div><div class="stars">{{ stars(Math.round(Number(providerStatsLive.rating_avg || 0))).join(' ') }}</div><p>Average rating across recent bookings.</p></section><section class="card"><article v-for="review in providerReviewsList" :key="review.id" class="review-row"><strong>{{ review.customer || review.reviewer_name || 'Resident' }}</strong><span>{{ stars(review.rating).join(' ') }}</span><p>{{ review.comment || review.review_text || 'No comment provided.' }}</p></article><div v-if="providerReviewsList.length === 0" class="list-row">No reviews yet.</div></section></div>
    </template>

    <template v-else-if="page === 'earnings'">
      <div class="screen-header"><h1>Earnings</h1><p>Monitor income across the current month and lifetime.</p></div>
      <div class="stat-grid provider-stats"><div class="card stat-card"><div class="stat-label">This Month</div><div class="stat-value">₹{{ Number(providerEarnings.monthly_earnings || providerEarnings.total_earnings || 0).toLocaleString() }}</div></div><div class="card stat-card"><div class="stat-label">Total</div><div class="stat-value">₹{{ Number(providerEarnings.total_earnings || 0).toLocaleString() }}</div></div></div>
      <div class="card"><div v-if="earningsBreakdown.length === 0" class="list-row">No earnings breakdown available yet.</div><div v-for="entry in earningsBreakdown" :key="entry.label" class="progress-row"><span>{{ entry.label }}</span><div class="progress"><span :style="{ width: `${entry.value}%` }"></span></div></div></div>
    </template>

    <template v-else-if="page === 'profile'">
      <div class="content-grid two-col">
        <section class="card profile-card">
          <div class="avatar avatar-xl">{{ userInitials }}</div>
          <h1>{{ providerName }}</h1>
          <p>{{ providerRoleText }}</p>
          <button class="btn btn-outline" @click="isEditingProfile = !isEditingProfile">{{ isEditingProfile ? 'Cancel' : 'Edit' }}</button>
        </section>
        <section class="card">
          <h3 class="card-title">Contact</h3>
          <template v-if="!isEditingProfile">
            <p>Phone: {{ providerPhone }}</p>
            <p>Email: {{ providerEmail }}</p>
          </template>
          <form v-else class="form-card" @submit.prevent="saveProviderProfile">
            <label class="form-group"><span class="form-label">Full Name</span><input v-model="profileForm.full_name" type="text" /></label>
            <label class="form-group"><span class="form-label">Phone</span><input v-model="profileForm.phone" type="text" /></label>
            <label class="form-group"><span class="form-label">Email (read-only)</span><input v-model="profileForm.email" type="text" disabled /></label>
            <button class="btn btn-primary">Save Profile</button>
          </form>
        </section>
      </div>
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
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Customer</th><th>Service</th><th>Date</th><th>Status</th></tr></thead><tbody><tr v-for="booking in filteredProviderBookings" :key="booking.id + 'history'"><td>{{ booking.resident_name || `Resident #${booking.resident_user_id}` }}</td><td>{{ booking.request_notes || '-' }}</td><td>{{ booking.created_at || '-' }}</td><td><span class="badge" :class="badgeClass(booking.booking_status || booking.status)">{{ booking.booking_status || booking.status }}</span></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'completed-jobs'">
      <div class="screen-header"><h1>Completed Jobs</h1><p>Finished work and service outcomes.</p></div>
      <div class="stack"><article v-for="booking in filteredProviderBookings.filter(item => (item.booking_status || item.status) === 'completed')" :key="booking.id" class="card completed-row"><strong>{{ booking.resident_name || `Resident #${booking.resident_user_id}` }}</strong><p>{{ booking.request_notes || '-' }}</p></article></div>
    </template>

    <template v-else-if="page === 'payouts'">
      <div class="screen-header"><h1>Payouts</h1><p>Payout summary and transfer history.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Period</th><th>Amount</th><th>Status</th></tr></thead><tbody><tr><td>This Week</td><td>₹4,500</td><td><span class="badge badge-success">Processed</span></td></tr><tr><td>Last Week</td><td>₹3,250</td><td><span class="badge badge-success">Processed</span></td></tr></tbody></table></div>
    </template>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'
import { useNotificationStore } from '@/stores/notificationStore'
import { faqs, providerBookings, reviews } from '@/data/mockData'
import { badgeClass, stars } from './screenUtils'

const route = useRoute()
const authStore = useAuthStore()
const notify = useNotificationStore()
const page = computed(() => route.meta.page || 'dashboard')
const backendBookings = ref([])
const providerStatsLive = ref({})
const providerProfile = ref(null)
const providerCategories = ref([])
const providerSlots = ref([])
const providerReviewsLive = ref([])
const providerEarnings = ref({})
const providerBookingsMeta = ref({ total: 0 })
const actionBookingIds = ref({})
const isEditingProfile = ref(false)
const serviceForm = ref({ business_name: '', service_description: '' })
const slotForm = ref({ slot_start: '', slot_end: '' })
const profileForm = ref({ full_name: '', phone: '', email: '' })

const providerName = computed(() => authStore.user?.name || 'Service Provider')
const userInitials = computed(() => authStore.userInitials || 'SP')
const providerEmail = computed(() => authStore.user?.email || '-')
const providerPhone = computed(() => authStore.user?.phone || '-')
const providerRoleText = computed(() => (authStore.user?.category ? `${authStore.user.category} Provider` : 'Verified Provider'))
const globalSearchQuery = computed(() => String(route.query.q || '').trim().toLowerCase())

const providerBookingsList = computed(() => {
  if (authStore.token) return backendBookings.value
  return providerBookings
})

function matchesProviderBookingSearch(booking, query) {
  if (!query) return true
  const values = [
    booking?.resident_name,
    booking?.resident_user_id,
    booking?.request_notes,
    booking?.created_at,
    booking?.booking_status,
    booking?.status,
  ].map((value) => String(value || '').toLowerCase())
  return values.some((value) => value.includes(query))
}

const filteredProviderBookings = computed(() => {
  const query = globalSearchQuery.value
  if (!query) return providerBookingsList.value
  return providerBookingsList.value.filter((booking) => matchesProviderBookingSearch(booking, query))
})

const bookingHistoryCount = computed(() => {
  const total = Number(providerBookingsMeta.value?.total || 0)
  if (total > 0) return total
  return providerBookingsList.value.length
})

function bookingStatus(item) {
  return String(item.booking_status || item.status || '').toLowerCase()
}

const pendingRequestsCount = computed(() => {
  return providerBookingsList.value.filter((item) => bookingStatus(item) === 'requested').length
})

const completedBookingsCount = computed(() => {
  return providerBookingsList.value.filter((item) => bookingStatus(item) === 'completed').length
})

const orderedProviderBookings = computed(() => {
  const priority = { requested: 0, accepted: 1, completed: 2, declined: 3, cancelled: 4 }
  return [...filteredProviderBookings.value].sort((a, b) => {
    const statusDiff = (priority[bookingStatus(a)] ?? 99) - (priority[bookingStatus(b)] ?? 99)
    if (statusDiff !== 0) return statusDiff
    return new Date(b.created_at || 0).getTime() - new Date(a.created_at || 0).getTime()
  })
})

const providerCategory = computed(() => {
  const fromProfile = providerProfile.value?.category_name || providerProfile.value?.category?.name
  if (fromProfile) return String(fromProfile).trim().toLowerCase()

  const categoryId = Number(providerProfile.value?.category_id)
  if (categoryId) {
    const matchedCategory = providerCategories.value.find((item) => Number(item.id) === categoryId)
    if (matchedCategory?.name) return String(matchedCategory.name).trim().toLowerCase()
  }

  return String(authStore.user?.category || '').trim().toLowerCase()
})

const providerServiceItems = computed(() => {
  const categoryLabel = providerProfile.value?.category_name
    || providerCategories.value.find((item) => Number(item.id) === Number(providerProfile.value?.category_id))?.name
    || providerCategory.value

  const businessName = String(serviceForm.value.business_name || '').trim()
  const description = String(serviceForm.value.service_description || '').trim()
  if (!businessName && !description) {
    return []
  }

  return [{
    name: businessName || `${categoryLabel || 'Service'} Provider`,
    price: 'Price on request',
    description: description || `${categoryLabel || 'General'} service`,
  }]
})

const providerStats = computed(() => [
  { label: 'Today Bookings', value: providerStatsLive.value.todays_bookings ?? providerBookingsList.value.length },
  { label: 'Pending Requests', value: pendingRequestsCount.value },
  { label: 'Completed', value: completedBookingsCount.value },
  { label: 'Rating', value: providerStatsLive.value.rating_avg ?? '0' },
])

const providerReviewsList = computed(() => {
  if (authStore.token) return providerReviewsLive.value
  return reviews
})

const providerNotifications = ['New booking from Priya Sharma', 'Cancellation request from Rahul Verma', '2 new review notifications']
const earningsBreakdown = computed(() => {
  const list = providerEarnings.value?.monthly_breakdown || []
  if (!Array.isArray(list) || list.length === 0) return []
  const maxAmount = Math.max(...list.map((item) => Number(item.amount || 0)), 1)
  return list.map((item) => ({
    label: item.label || item.month || 'Period',
    value: Math.max(4, Math.round((Number(item.amount || 0) / maxAmount) * 100)),
  }))
})

async function loadProviderData() {
  try {
    if (!authStore.user && authStore.token) {
      await authStore.fetchMe()
    }
    if (authStore.user) {
      profileForm.value.full_name = authStore.user.full_name || authStore.user.name || ''
      profileForm.value.phone = authStore.user.phone || ''
      profileForm.value.email = authStore.user.email || ''
    }
    if (authStore.token) {
      await authStore.ensureProviderProfile()

      const [bookingsResult, statsResult, profileResult, categoriesResult] = await Promise.allSettled([
        authStore.listBookings({ withMeta: true }),
        authStore.getProviderDashboardStats(),
        authStore.getMyProviderProfile(),
        authStore.listServiceCategories(),
      ])

      if (bookingsResult.status === 'fulfilled') {
        backendBookings.value = bookingsResult.value.items || []
        providerBookingsMeta.value = bookingsResult.value.pagination || { total: backendBookings.value.length }
      }
      if (statsResult.status === 'fulfilled') {
        providerStatsLive.value = statsResult.value
      }
      if (profileResult.status === 'fulfilled') {
        providerProfile.value = profileResult.value
        if (providerProfile.value) {
          serviceForm.value.business_name = providerProfile.value.business_name || ''
          serviceForm.value.service_description = providerProfile.value.service_description || ''
          const [slotsResult, reviewsResult, earningsResult] = await Promise.allSettled([
            authStore.listProviderSlots(providerProfile.value.id),
            authStore.getProviderReviews(providerProfile.value.id),
            authStore.getProviderEarnings(providerProfile.value.id),
          ])

          if (slotsResult.status === 'fulfilled') {
            providerSlots.value = slotsResult.value
          }
          if (reviewsResult.status === 'fulfilled') {
            providerReviewsLive.value = reviewsResult.value
          }
          if (earningsResult.status === 'fulfilled') {
            providerEarnings.value = earningsResult.value || {}
          }
        }
      }

      if (categoriesResult.status === 'fulfilled') {
        providerCategories.value = categoriesResult.value || []
      }

      if (bookingsResult.status === 'rejected' && statsResult.status === 'rejected') {
        throw bookingsResult.reason || statsResult.reason
      }
    }
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to load provider data')
  }
}

async function saveProviderProfile() {
  try {
    await authStore.updateMe({
      full_name: String(profileForm.value.full_name || '').trim(),
      phone: String(profileForm.value.phone || '').trim(),
    })
    isEditingProfile.value = false
    notify.success('Profile updated successfully')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to update profile')
  }
}

function formatDateTime(value) {
  if (!value) return '-'
  const date = new Date(value)
  if (Number.isNaN(date.getTime())) return String(value)
  return date.toLocaleString()
}

function canAcceptBooking(booking) {
  return bookingStatus(booking) === 'requested'
}

function canDeclineBooking(booking) {
  const status = bookingStatus(booking)
  return status === 'requested' || status === 'accepted'
}

function canCompleteBooking(booking) {
  return bookingStatus(booking) === 'accepted'
}

function markBookingAction(bookingId, isBusy) {
  actionBookingIds.value = {
    ...actionBookingIds.value,
    [bookingId]: isBusy,
  }
}

async function saveProviderService() {
  try {
    if (!providerProfile.value?.id) {
      notify.error('Provider profile not found')
      return
    }

    const updated = await authStore.updateProvider(providerProfile.value.id, {
      business_name: String(serviceForm.value.business_name || '').trim(),
      service_description: String(serviceForm.value.service_description || '').trim(),
    })
    providerProfile.value = updated
    notify.success('Service details updated')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to update service details')
  }
}

async function addAvailabilitySlot() {
  try {
    if (!providerProfile.value?.id) {
      notify.error('Provider profile not found')
      return
    }
    if (!slotForm.value.slot_start || !slotForm.value.slot_end) {
      notify.error('Start and end date/time are required')
      return
    }

    await authStore.createProviderSlot({
      provider_id: providerProfile.value.id,
      slot_start: new Date(slotForm.value.slot_start).toISOString(),
      slot_end: new Date(slotForm.value.slot_end).toISOString(),
      is_available: true,
    })
    providerSlots.value = await authStore.listProviderSlots(providerProfile.value.id)
    slotForm.value.slot_start = ''
    slotForm.value.slot_end = ''
    notify.success('Availability slot added')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to add availability slot')
  }
}

async function removeAvailabilitySlot(slotId) {
  try {
    await authStore.deleteProviderSlot(slotId)
    if (providerProfile.value?.id) {
      providerSlots.value = await authStore.listProviderSlots(providerProfile.value.id)
    }
    notify.success('Availability slot removed')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to remove availability slot')
  }
}

async function acceptProviderBooking(bookingId) {
  try {
    markBookingAction(bookingId, true)
    await authStore.acceptBooking(bookingId)
    const bookingsPayload = await authStore.listBookings({ withMeta: true })
    backendBookings.value = bookingsPayload.items || []
    providerBookingsMeta.value = bookingsPayload.pagination || { total: backendBookings.value.length }
    providerStatsLive.value = await authStore.getProviderDashboardStats()
    notify.success('Booking accepted')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to accept booking')
  } finally {
    markBookingAction(bookingId, false)
  }
}

async function declineProviderBooking(bookingId) {
  try {
    markBookingAction(bookingId, true)
    await authStore.declineBooking(bookingId)
    const bookingsPayload = await authStore.listBookings({ withMeta: true })
    backendBookings.value = bookingsPayload.items || []
    providerBookingsMeta.value = bookingsPayload.pagination || { total: backendBookings.value.length }
    providerStatsLive.value = await authStore.getProviderDashboardStats()
    notify.success('Booking rejected')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to reject booking')
  } finally {
    markBookingAction(bookingId, false)
  }
}

async function completeProviderBooking(bookingId) {
  try {
    markBookingAction(bookingId, true)
    await authStore.completeBooking(bookingId)
    const bookingsPayload = await authStore.listBookings({ withMeta: true })
    backendBookings.value = bookingsPayload.items || []
    providerBookingsMeta.value = bookingsPayload.pagination || { total: backendBookings.value.length }
    providerStatsLive.value = await authStore.getProviderDashboardStats()
    notify.success('Booking marked complete')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to complete booking')
  } finally {
    markBookingAction(bookingId, false)
  }
}

onMounted(() => {
  loadProviderData()
})
</script>

<style scoped>
.portal-screen { display: grid; gap: var(--space-6); }
.screen-header { display: grid; gap: var(--space-2); }
.screen-header h1 { margin: 0; }
.screen-header p { color: var(--color-text-secondary); }
.screen-header.row-between { display: flex; justify-content: space-between; align-items: center; gap: var(--space-4); }
.stat-grid, .content-grid { display: grid; gap: var(--space-5); }
.stat-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.provider-stats .stat-value { font-size: var(--text-3xl); font-weight: var(--font-bold); margin-top: var(--space-2); }
.content-grid.two-col { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.list-row, .booking-card, .service-row, .review-row, .completed-row, .note-card, .faq-item { padding: var(--space-4) var(--space-5); border-bottom: 1px solid var(--color-border); }
.list-row:last-child, .booking-card:last-child, .service-row:last-child, .review-row:last-child, .completed-row:last-child, .note-card:last-child, .faq-item:last-child { border-bottom: none; }
.chip-row { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.chip, .chip-link { padding: 6px 12px; border-radius: var(--radius-full); background: var(--color-gray-100); color: var(--color-text-secondary); text-decoration: none; }
.time-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: var(--space-4); margin-top: var(--space-4); }
.time-slot { padding: var(--space-3); border: 1px solid var(--color-border); border-radius: var(--radius-md); background: var(--color-gray-50); }
.rating-card { display: grid; gap: var(--space-4); align-items: start; }
.rating-value { font-size: 3rem; font-weight: var(--font-bold); color: var(--color-primary); }
.stars { color: var(--color-accent-dark); }
.progress-row { display: grid; gap: var(--space-2); margin-bottom: var(--space-4); }
.progress { height: 10px; border-radius: var(--radius-full); background: var(--color-gray-100); overflow: hidden; }
.progress span { display: block; height: 100%; background: linear-gradient(90deg, var(--color-secondary), var(--color-primary)); }
.form-card { display: grid; gap: var(--space-5); }
.switch-row { display: flex; justify-content: space-between; gap: var(--space-4); align-items: center; padding: var(--space-2) 0; }
.profile-card { text-align: center; }
.table-wrap { overflow-x: auto; }
@media (max-width: 960px) { .stat-grid, .content-grid.two-col, .time-grid { grid-template-columns: 1fr; } .screen-header.row-between { flex-direction: column; align-items: flex-start; } }

.dashboard-shell {
  display: grid;
  gap: var(--space-6);
}

.dashboard-shell .screen-header {
  padding: var(--space-6);
  border: 1px solid rgba(37, 99, 235, 0.08);
  border-radius: var(--radius-2xl);
  background:
    radial-gradient(circle at top right, rgba(34, 197, 94, 0.12), transparent 28%),
    linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(248, 250, 252, 0.94));
  box-shadow: 0 24px 60px rgba(15, 23, 42, 0.08);
}

.dashboard-shell .screen-header h1 {
  font-size: clamp(2rem, 2.8vw, 3rem);
}

.dashboard-shell .stat-grid {
  gap: var(--space-5);
}

.dashboard-shell .stat-card,
.dashboard-shell .card {
  border: 1px solid rgba(229, 231, 235, 0.9);
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(248, 250, 252, 0.94));
  box-shadow: var(--shadow-sm);
}

.dashboard-shell .stat-card {
  padding: var(--space-5);
}

.dashboard-shell .stat-card .stat-value {
  font-size: clamp(1.8rem, 3vw, 2.5rem);
}

.dashboard-shell .content-grid.two-col {
  align-items: start;
}

.dashboard-shell .chip,
.dashboard-shell .chip-link {
  background: rgba(37, 99, 235, 0.08);
  color: var(--color-primary);
}

.dashboard-shell .time-slot {
  background: rgba(255, 255, 255, 0.9);
}

.dashboard-shell .progress {
  height: 12px;
}

.dashboard-shell .rating-value {
  font-size: clamp(2.6rem, 5vw, 4rem);
}
</style>