<template>
  <div class="portal-screen resident-screen">
    <template v-if="page === 'dashboard'">
      <div class="dashboard-shell">
      <div class="screen-hero card">
        <div>
          <p class="eyebrow">Resident Portal</p>
          <h1>Good Morning, {{ currentUserDisplayName }}</h1>
          <p>Here is a quick snapshot of your society activity.</p>
        </div>
        <div class="screen-avatar avatar avatar-xl">{{ currentUserInitials }}</div>
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
          <div v-for="notice in residentNotices.slice(0, 4)" :key="notice.id" class="list-row">
            <div>
              <strong>{{ notice.title }}</strong>
              <p>{{ notice.content || notice.body }}</p>
            </div>
            <span class="badge" :class="badgeClass(notice.priority)">{{ notice.category || notice.notice_type || 'Notice' }}</span>
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
          <div v-for="event in residentEvents.slice(0, 3)" :key="event.id" class="event-card">
            <div>
              <strong>{{ event.title }}</strong>
              <p>{{ formatEventMeta(event) }}</p>
            </div>
            <button class="btn btn-primary btn-sm" @click="joinEvent(event.id)">Join</button>
          </div>
        </section>
        <section class="card">
          <div class="card-header"><span class="card-title">Recent Notices</span></div>
          <div v-for="notice in residentNotices.slice(0, 3)" :key="notice.id + '-recent'" class="list-row compact">
            <div>
              <strong>{{ notice.title }}</strong>
              <p>{{ notice.date || notice.publish_at || '-' }}</p>
            </div>
          </div>
        </section>
      </div>
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
        <article v-for="notice in residentNotices" :key="notice.id" class="card notice-card">
          <div class="card-header no-border">
            <strong>{{ notice.title }}</strong>
            <span class="badge" :class="badgeClass(notice.priority)">{{ notice.priority }}</span>
          </div>
          <p>{{ notice.content || notice.body }}</p>
          <small>{{ notice.date || notice.publish_at || '-' }} · {{ notice.category || notice.notice_type || 'Notice' }}</small>
        </article>
      </div>
    </template>

    <template v-else-if="page === 'events'">
      <div class="screen-header">
        <h1>Upcoming Events</h1>
        <p>Community activities, celebrations, and wellness sessions.</p>
      </div>
      <div class="card-grid three-col">
        <article v-for="event in residentEvents" :key="event.id" class="card event-tile">
          <div class="tile-visual">{{ event.category }}</div>
          <h3>{{ event.title }}</h3>
          <p>{{ event.date || event.event_date }} · {{ event.time || event.start_time || '-' }}</p>
          <p>{{ event.venue }}</p>
          <button class="btn btn-primary btn-sm" @click="joinEvent(event.id)">Register / Join Event</button>
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
            <tr v-for="complaint in residentComplaints" :key="complaint.id">
              <td>{{ complaint.id }}</td>
              <td><router-link :to="`/resident/complaints/${complaint.id}`">{{ complaint.title || complaint.subject }}</router-link></td>
              <td>{{ complaint.category }}</td>
              <td><span class="badge" :class="badgeClass(complaint.status)">{{ complaint.status }}</span></td>
              <td>{{ complaint.date || complaint.created_at || '-' }}</td>
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
      <div v-if="browseServiceCards.length > 0" class="card-grid three-col">
        <article v-for="service in browseServiceCards" :key="service.id" class="card service-tile">
          <div class="service-icon">🛠️</div>
          <h3>{{ service.name }}</h3>
          <p>{{ service.description || 'Verified community service provider' }}</p>
          <router-link
            v-if="hasProviderForCategory(service.id)"
            :to="providerRouteForCategory(service.id)"
            class="btn btn-outline btn-sm"
          >
            View providers
          </router-link>
          <span v-else class="chip">No providers yet</span>
        </article>
      </div>
      <section v-else class="card">
        <p>No service categories are configured yet.</p>
      </section>
    </template>

    <template v-else-if="page === 'provider-details'">
      <div class="content-grid two-col align-start">
        <section class="card provider-card">
          <div class="provider-top">
            <div class="avatar avatar-xl">RP</div>
            <div>
              <h1>{{ selectedProvider?.business_name || 'Provider' }}</h1>
              <p>{{ selectedProvider?.service_description || 'Service provider profile' }}</p>
              <div class="stars">{{ stars(selectedProvider?.rating_avg || 0).join(' ') }}</div>
            </div>
          </div>
          <p>{{ selectedProvider?.service_description || 'Book trusted providers for your needs.' }}</p>
          <button class="btn btn-primary" @click="bookServiceNow">Book Now</button>
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
        <article v-for="booking in residentBookings" :key="booking.id" class="card booking-card">
          <div><strong>{{ bookingFacility(booking) }}</strong><p>{{ bookingDate(booking) }}</p></div>
          <span class="badge" :class="badgeClass(booking.status || booking.booking_status)">{{ booking.status || booking.booking_status }}</span>
        </article>
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
          <div class="avatar avatar-xl">{{ currentUserInitials }}</div>
          <h1>{{ currentUserDisplayName }}</h1>
          <p>{{ authStore.user?.flat || 'Resident' }} · Green Valley Society</p>
          <button class="btn btn-outline" @click="isEditingProfile = !isEditingProfile">
            {{ isEditingProfile ? 'Cancel' : 'Edit Profile' }}
          </button>
        </section>
        <section class="card">
          <h3 class="card-title">Contact Details</h3>
          <div v-if="!isEditingProfile" class="detail-list">
            <div class="detail-row"><span>Phone</span><strong>{{ profileForm.phone || '-' }}</strong></div>
            <div class="detail-row"><span>Email</span><strong>{{ profileForm.email || '-' }}</strong></div>
          </div>
          <form v-else class="form-card" @submit.prevent="saveProfile">
            <label class="form-group">
              <span class="form-label">Full Name</span>
              <input v-model="profileForm.full_name" type="text" />
            </label>
            <label class="form-group">
              <span class="form-label">Phone</span>
              <input v-model="profileForm.phone" type="text" />
            </label>
            <label class="form-group">
              <span class="form-label">Email (read-only)</span>
              <input v-model="profileForm.email" type="text" disabled />
            </label>
            <button class="btn btn-primary">Save Profile</button>
          </form>
        </section>
      </div>
    </template>

    <template v-else-if="page === 'book-events'">
      <div class="screen-header">
        <h1>Book Events</h1>
        <p>Register for upcoming community events.</p>
      </div>
      <div class="card-grid three-col">
        <article v-for="event in residentEvents" :key="event.id + '-book'" class="card event-tile">
          <div class="tile-visual">{{ event.category || 'Event' }}</div>
          <h3>{{ event.title }}</h3>
          <p>{{ event.date || event.event_date }} · {{ event.time || event.start_time || '-' }}</p>
          <p>{{ event.venue }}</p>
          <button class="btn btn-primary btn-sm" @click="joinEvent(event.id)">Book / Join</button>
          <button class="btn btn-outline btn-sm" @click="leaveEvent(event.id)">Cancel Booking</button>
          <small v-if="joinedEventIds.has(event.id)">Booked</small>
        </article>
      </div>
    </template>

    <template v-else-if="page === 'book-amenities'">
      <div class="content-grid two-col align-start">
        <form class="card form-card amenity-booking-form" @submit.prevent="submitAmenityBooking">
          <div class="form-grid two-col">
            <label class="form-group"><span class="form-label">Facility</span><select v-model="amenityForm.category_id"><option disabled value="">Select facility</option><option v-for="category in browseServiceCards" :key="category.id" :value="category.id">{{ category.name }}</option></select></label>
            <label class="form-group"><span class="form-label">Assigned Provider</span><input :value="selectedAmenityProviderName" type="text" disabled /></label>
          </div>
          <div class="form-grid two-col">
            <label class="form-group"><span class="form-label">Date</span><input v-model="amenityForm.date" type="date" /></label>
            <label class="form-group"><span class="form-label">Time Slot</span><input v-model="amenityForm.time_slot" type="text" placeholder="09:00 AM - 10:00 AM" /></label>
          </div>
          <label class="form-group"><span class="form-label">Purpose</span><input v-model="amenityForm.purpose" type="text" placeholder="Enter purpose" /></label>
          <button class="btn btn-primary">Book Now</button>
        </form>
        <section class="card">
          <h3 class="card-title">My Bookings</h3>
          <div v-for="booking in residentBookings.slice(0, 3)" :key="booking.id + 'amenity'" class="list-row compact"><strong>{{ bookingFacility(booking) }}</strong><span>{{ booking.status || booking.booking_status }}</span></div>
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
        <article v-for="booking in residentBookings" :key="booking.id + 'history'" class="card history-card">
          <div><strong>{{ bookingFacility(booking) }}</strong><p>{{ bookingDate(booking) }}</p></div>
          <span class="badge" :class="badgeClass(booking.status || booking.booking_status)">{{ booking.status || booking.booking_status }}</span>
        </article>
      </div>
    </template>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'
import { useNotificationStore } from '@/stores/notificationStore'
import {
  bookings,
  complaints as mockComplaints,
  events as mockEvents,
  familyMembers,
  faqs,
  maintenanceBills,
  notices as mockNotices,
  notifications,
  serviceCategories as mockServiceCategories,
  serviceProviders,
} from '@/data/mockData'
import { badgeClass, currency, days, stars } from './screenUtils'

const route = useRoute()
const authStore = useAuthStore()
const notify = useNotificationStore()
const page = computed(() => route.meta.page || 'dashboard')

const backendEvents = ref([])
const backendNotices = ref([])
const backendComplaints = ref([])
const backendProviders = ref([])
const backendServiceCategories = ref([])
const backendBookings = ref([])
const providerAmenityNameById = ref({})
const joinedEventIds = ref(new Set())
const isEditingProfile = ref(false)
const profileForm = reactive({ full_name: '', phone: '', email: '' })
const amenityForm = reactive({ category_id: '', date: '', time_slot: '', purpose: '' })
const globalSearchQuery = computed(() => String(route.query.q || '').trim().toLowerCase())

function matchesSearch(values, query) {
  if (!query) return true
  return values
    .map((value) => String(value || '').toLowerCase())
    .some((value) => value.includes(query))
}

const residentEvents = computed(() => {
  const list = authStore.token ? backendEvents.value : mockEvents
  const query = globalSearchQuery.value
  if (!query) return list
  return list.filter((event) => matchesSearch([
    event?.title,
    event?.description,
    event?.venue,
    event?.category,
    event?.event_date,
    event?.date,
  ], query))
})

const residentNotices = computed(() => {
  if (authStore.token) {
    const sorted = [...backendNotices.value].sort((a, b) => {
      const aTime = new Date(a.publish_at || a.created_at || a.date || 0).getTime()
      const bTime = new Date(b.publish_at || b.created_at || b.date || 0).getTime()
      return bTime - aTime
    })
    const query = globalSearchQuery.value
    if (!query) return sorted
    return sorted.filter((notice) => matchesSearch([
      notice?.title,
      notice?.body,
      notice?.content,
      notice?.notice_type,
      notice?.category,
      notice?.priority,
    ], query))
  }
  const query = globalSearchQuery.value
  if (!query) return mockNotices
  return mockNotices.filter((notice) => matchesSearch([
    notice?.title,
    notice?.body,
    notice?.content,
    notice?.notice_type,
    notice?.category,
    notice?.priority,
  ], query))
})

const residentComplaints = computed(() => {
  if (authStore.token) {
    const sorted = [...backendComplaints.value].sort((a, b) => {
      const aTime = new Date(a.created_at || a.date || 0).getTime()
      const bTime = new Date(b.created_at || b.date || 0).getTime()
      if (aTime !== bTime) return bTime - aTime
      return Number(b.id || 0) - Number(a.id || 0)
    })
    const query = globalSearchQuery.value
    if (!query) return sorted
    return sorted.filter((complaint) => matchesSearch([
      complaint?.id,
      complaint?.title,
      complaint?.subject,
      complaint?.description,
      complaint?.category,
      complaint?.status,
    ], query))
  }
  const query = globalSearchQuery.value
  if (!query) return mockComplaints
  return mockComplaints.filter((complaint) => matchesSearch([
    complaint?.id,
    complaint?.title,
    complaint?.subject,
    complaint?.description,
    complaint?.category,
    complaint?.status,
  ], query))
})

const residentBookings = computed(() => {
  const list = authStore.token ? backendBookings.value : bookings
  const query = globalSearchQuery.value
  if (!query) return list
  return list.filter((booking) => matchesSearch([
    booking?.request_notes,
    booking?.status,
    booking?.booking_status,
    booking?.provider_name,
    booking?.created_at,
    booking?.date,
    bookingFacility(booking),
  ], query))
})

const browseServiceCards = computed(() => {
  const list = authStore.token ? backendServiceCategories.value : mockServiceCategories
  const query = globalSearchQuery.value
  if (!query) return list
  return list.filter((category) => matchesSearch([
    category?.name,
    category?.description,
  ], query))
})

const selectedProvider = computed(() => {
  const id = Number(route.params.id)
  if (!id) return backendProviders.value[0] || null
  return backendProviders.value.find((item) => Number(item.id) === id) || null
})

const amenityProviders = computed(() => {
  const categoryId = Number(amenityForm.category_id)
  if (!categoryId) return backendProviders.value
  return backendProviders.value.filter((item) => Number(item.category_id) === categoryId)
})

const selectedAmenityProvider = computed(() => {
  const categoryId = Number(amenityForm.category_id)
  if (!categoryId) return null

  const category = browseServiceCards.value.find((item) => Number(item.id) === categoryId)
  const categoryName = String(category?.name || '').trim().toLowerCase()
  const list = amenityProviders.value

  if (Array.isArray(list) && list.length) {
    const directMatch = list.find((provider) => String(provider.business_name || '').toLowerCase().includes(categoryName))
    if (directMatch) return directMatch
    return list[0]
  }

  const fallback = backendProviders.value.find((provider) => String(provider.business_name || '').toLowerCase().includes(categoryName))
  return fallback || null
})

const selectedAmenityProviderName = computed(() => {
  if (!amenityForm.category_id) return 'Select facility first'
  return selectedAmenityProvider.value?.business_name || 'No provider available for selected facility'
})

const currentUserDisplayName = computed(() => authStore.user?.name || 'Resident')
const currentUserInitials = computed(() => authStore.userInitials)

const complaintForm = reactive({ category: 'Plumbing', title: '', description: '' })

const dashboardStats = computed(() => [
  { label: 'My Complaints', value: residentComplaints.value.length },
  { label: 'My Bookings', value: residentBookings.value.length },
  { label: 'Upcoming Events', value: residentEvents.value.length },
  { label: 'New Notices', value: residentNotices.value.length },
])

const quickActions = [
  { label: 'Raise Complaint', icon: '📝', to: '/resident/complaints/new' },
  { label: 'Book Service', icon: '🛠️', to: '/resident/services' },
  { label: 'Track Events', icon: '🎉', to: '/resident/events' },
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

const serviceRates = computed(() => {
  const provider = selectedProvider.value
  if (!provider) return []

  const category = backendServiceCategories.value.find(
    (item) => Number(item.id) === Number(provider.category_id),
  )
  const categoryName = String(category?.name || '').trim().toLowerCase()
  const matched = serviceProviders.find(
    (item) => String(item.category || '').trim().toLowerCase() === categoryName,
  )

  if (matched?.services?.length) {
    return matched.services
  }

  if (provider.service_description) {
    return [{ name: provider.business_name || 'Service', price: 'Price on request' }]
  }

  return []
})

const availability = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
const calendarDays = days(30)
const timeSlots = ['08:00', '09:00', '10:00', '11:00', '14:00', '15:00']

async function submitComplaint() {
  try {
    await authStore.createComplaint({
      subject: String(complaintForm.title || '').trim(),
      description: String(complaintForm.description || '').trim(),
      category: complaintForm.category,
      priority: 'medium',
    })
    notify.success('Complaint submitted successfully')
    complaintForm.title = ''
    complaintForm.description = ''
    backendComplaints.value = await authStore.listComplaints()
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Failed to submit complaint')
  }
}

function formatEventMeta(event) {
  const date = event.date || event.event_date || '-'
  const time = event.time || event.start_time || '-'
  const venue = event.venue || '-'
  return `${date} · ${time} · ${venue}`
}

function hasProviderForCategory(categoryId) {
  return backendProviders.value.some((provider) => Number(provider.category_id) === Number(categoryId))
}

function providerRouteForCategory(categoryId) {
  const provider = backendProviders.value.find((item) => Number(item.category_id) === Number(categoryId))
  if (!provider) return '/resident/services'
  return `/resident/services/provider/${provider.id}`
}

async function loadResidentData() {
  try {
    if (!authStore.user && authStore.token) {
      await authStore.fetchMe()
    }

    if (authStore.user) {
      profileForm.full_name = authStore.user.full_name || authStore.user.name || ''
      profileForm.phone = authStore.user.phone || ''
      profileForm.email = authStore.user.email || ''
    }

    if (authStore.token) {
      const searchTerm = String(route.query.q || '').trim()
      const searchQueryString = searchTerm ? new URLSearchParams({ search: searchTerm }).toString() : ''
      const [
        eventsResult,
        noticesResult,
        complaintsResult,
        providersResult,
        categoriesResult,
        bookingsResult,
      ] = await Promise.allSettled([
        authStore.listEvents(searchQueryString),
        authStore.listNotices(searchQueryString),
        authStore.listComplaints(searchQueryString),
        authStore.listProviders(searchQueryString),
        authStore.listServiceCategories(),
        authStore.listBookings(),
      ])

      if (eventsResult.status === 'fulfilled') backendEvents.value = eventsResult.value
      if (noticesResult.status === 'fulfilled') backendNotices.value = noticesResult.value
      if (complaintsResult.status === 'fulfilled') backendComplaints.value = complaintsResult.value
      if (providersResult.status === 'fulfilled') backendProviders.value = providersResult.value
      if (categoriesResult.status === 'fulfilled') backendServiceCategories.value = categoriesResult.value
      if (bookingsResult.status === 'fulfilled') {
        backendBookings.value = bookingsResult.value
        await hydrateBookingAmenityNames(backendBookings.value)
      }
    }
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to load resident data')
  }
}

async function saveProfile() {
  try {
    await authStore.updateMe({
      full_name: String(profileForm.full_name || '').trim(),
      phone: String(profileForm.phone || '').trim(),
    })
    isEditingProfile.value = false
    notify.success('Profile updated successfully')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Profile update failed')
  }
}

async function joinEvent(eventId) {
  if (!eventId) {
    notify.error('Invalid event selection')
    return
  }
  try {
    await authStore.registerEvent(eventId)
    const next = new Set(joinedEventIds.value)
    next.add(eventId)
    joinedEventIds.value = next
    notify.success('Event booked successfully')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Event booking failed')
  }
}

async function bookServiceNow() {
  if (!selectedProvider.value?.id) {
    notify.error('No provider selected')
    return
  }

  try {
    await authStore.createBooking({
      provider_id: selectedProvider.value.id,
      request_notes: 'Booking created from resident portal',
    })
    backendBookings.value = await authStore.listBookings()
    await hydrateBookingAmenityNames(backendBookings.value)
    notify.success('Service booking created successfully')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to create booking')
  }
}

async function submitAmenityBooking() {
  try {
    const providerId = Number(selectedAmenityProvider.value?.id)
    if (!providerId) {
      notify.error('No provider available for selected facility')
      return
    }

    const category = browseServiceCards.value.find((item) => Number(item.id) === Number(amenityForm.category_id))
    const notesParts = [
      category?.name ? `Facility: ${category.name}` : '',
      amenityForm.date ? `Date: ${amenityForm.date}` : '',
      amenityForm.time_slot ? `Time: ${amenityForm.time_slot}` : '',
      amenityForm.purpose ? `Purpose: ${amenityForm.purpose}` : '',
    ].filter(Boolean)

    await authStore.createBooking({
      provider_id: providerId,
      request_notes: notesParts.join(' | ') || 'Amenity booking request',
    })

    backendBookings.value = await authStore.listBookings()
    await hydrateBookingAmenityNames(backendBookings.value)
    amenityForm.category_id = ''
    amenityForm.date = ''
    amenityForm.time_slot = ''
    amenityForm.purpose = ''
    notify.success('Amenity booking created successfully')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to create amenity booking')
  }
}

async function hydrateBookingAmenityNames(bookingsList) {
  if (!authStore.token || !Array.isArray(bookingsList) || bookingsList.length === 0) return

  const nextMap = { ...providerAmenityNameById.value }
  const providerIds = [...new Set(bookingsList.map((item) => Number(item.provider_id)).filter((id) => Number.isFinite(id) && id > 0))]
  const missingIds = providerIds.filter((id) => !nextMap[id])
  if (missingIds.length === 0) {
    providerAmenityNameById.value = nextMap
    return
  }

  const providerResults = await Promise.allSettled(missingIds.map((id) => authStore.getProvider(id)))
  for (let index = 0; index < providerResults.length; index += 1) {
    const result = providerResults[index]
    const providerId = missingIds[index]
    if (result.status !== 'fulfilled' || !result.value) continue

    const provider = result.value
    const categoryId = Number(provider.category_id)
    const category = backendServiceCategories.value.find((item) => Number(item.id) === categoryId)
    nextMap[providerId] = category?.name || provider.business_name || `Provider #${providerId}`
  }

  providerAmenityNameById.value = nextMap
}

function bookingFacility(booking) {
  const notes = String(booking?.request_notes || '')
  const match = notes.match(/Facility:\s*([^|]+)/i)
  if (match?.[1]) return match[1].trim()

  const providerId = Number(booking?.provider_id)
  if (providerId) {
    if (providerAmenityNameById.value[providerId]) {
      return providerAmenityNameById.value[providerId]
    }

    const provider = backendProviders.value.find((item) => Number(item.id) === providerId)
    const categoryId = Number(provider?.category_id)
    if (categoryId) {
      const category = backendServiceCategories.value.find((item) => Number(item.id) === categoryId)
      if (category?.name) return category.name
    }
    if (provider?.business_name) return provider.business_name
  }

  return booking?.facility || booking?.provider_name || `Provider #${booking?.provider_id}`
}

function bookingDate(booking) {
  const notes = String(booking?.request_notes || '')
  const dateMatch = notes.match(/Date:\s*([^|]+)/i)
  const timeMatch = notes.match(/Time:\s*([^|]+)/i)
  if (dateMatch?.[1] || timeMatch?.[1]) {
    return [dateMatch?.[1]?.trim(), timeMatch?.[1]?.trim()].filter(Boolean).join(' · ')
  }
  return booking?.date || booking?.created_at || '-'
}

async function leaveEvent(eventId) {
  try {
    await authStore.unregisterEvent(eventId)
    const next = new Set(joinedEventIds.value)
    next.delete(eventId)
    joinedEventIds.value = next
    notify.success('Event booking cancelled')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to cancel event booking')
  }
}

onMounted(() => {
  loadResidentData()
})

watch(
  () => route.query.q,
  () => {
    loadResidentData()
  }
)
</script>

<style scoped>
.portal-screen { display: grid; gap: var(--space-6); }
.screen-hero { display: flex; align-items: center; justify-content: space-between; gap: var(--space-6); }
.eyebrow { text-transform: uppercase; letter-spacing: 0.08em; font-size: var(--text-xs); color: var(--color-primary); font-weight: var(--font-semibold); margin-bottom: var(--space-2); }
.screen-hero h1, .screen-header h1 { margin-bottom: var(--space-3); }
.screen-hero p, .screen-header p { color: var(--color-text-secondary); }
.screen-avatar { background: linear-gradient(135deg, var(--color-primary-100), var(--color-info-100)); color: var(--color-primary); }
.stat-grid, .card-grid, .action-grid, .content-grid { display: grid; gap: var(--space-5); }
.stat-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.stat-card { padding: var(--space-5); }
.stat-label { font-size: var(--text-sm); color: var(--color-text-secondary); }
.stat-value { font-size: var(--text-3xl); font-weight: var(--font-bold); margin-top: var(--space-2); }
.content-grid.two-col { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.card-grid.three-col { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.list-row, .event-card, .booking-card, .notification-card, .bill-card, .history-card, .member-card, .faq-item { display: flex; align-items: center; justify-content: space-between; gap: var(--space-4); }
.list-row, .event-card, .booking-card, .notification-card, .bill-card, .history-card, .member-card { padding: var(--space-4) var(--space-5); border-bottom: 1px solid var(--color-border); }
.list-row:last-child, .event-card:last-child, .booking-card:last-child, .notification-card:last-child, .bill-card:last-child, .history-card:last-child, .member-card:last-child { border-bottom: none; }
.compact { padding: var(--space-3) var(--space-5); }
.action-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.action-card { display: grid; gap: var(--space-3); padding: var(--space-5); border: 1px solid var(--color-border); border-radius: var(--radius-lg); background: var(--color-gray-50); color: inherit; }
.chip-row { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.chip { padding: 6px 12px; border-radius: var(--radius-full); background: var(--color-gray-100); color: var(--color-text-secondary); font-size: var(--text-xs); }
.stack { display: grid; gap: var(--space-4); }
.tile-visual, .service-icon { width: 64px; height: 64px; display: grid; place-items: center; border-radius: var(--radius-lg); background: var(--color-primary-50); color: var(--color-primary); font-weight: var(--font-semibold); }
.provider-top { display: flex; align-items: center; gap: var(--space-4); margin-bottom: var(--space-4); }
.stars { color: var(--color-accent-dark); letter-spacing: 2px; }
.calendar-grid { display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 10px; margin-bottom: var(--space-4); }
.calendar-day { padding: var(--space-3); border-radius: var(--radius-md); background: var(--color-gray-50); border: 1px solid var(--color-border); }
.calendar-day.active { background: var(--color-primary); color: white; }
.detail-list { display: grid; gap: var(--space-4); }
.detail-row { display: flex; justify-content: space-between; gap: var(--space-4); }
.timeline-row { display: flex; gap: var(--space-3); margin-top: var(--space-4); }
.timeline-dot { width: 12px; height: 12px; margin-top: 6px; border-radius: 50%; background: var(--color-border); }
.timeline-dot.done { background: var(--color-primary); }
.form-card { display: grid; gap: var(--space-4); }
.form-grid.two-col { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-4); }
.amenity-booking-form .form-group { margin-bottom: 0; display: grid; gap: var(--space-2); align-content: start; }
.amenity-booking-form select,
.amenity-booking-form input { min-height: 44px; }
.screen-header.row-between { display: flex; align-items: center; justify-content: space-between; gap: var(--space-4); }
.profile-card { text-align: center; }
.provider-card, .profile-card { align-items: flex-start; }
.faq-item { display: block; padding: var(--space-4) var(--space-5); border-bottom: 1px solid var(--color-border); }
.faq-item:last-child { border-bottom: none; }
.bill-meta { display: grid; justify-items: end; gap: var(--space-2); }
.align-start { align-items: start; }
@media (max-width: 960px) {
  .stat-grid, .content-grid.two-col, .card-grid.three-col { grid-template-columns: 1fr; }
  .screen-hero, .screen-header.row-between, .provider-top { flex-direction: column; align-items: flex-start; }
  .form-grid.two-col { grid-template-columns: 1fr; }
}

.dashboard-shell {
  display: grid;
  gap: var(--space-6);
}

.dashboard-shell .screen-hero {
  padding: var(--space-6);
  border: 1px solid rgba(37, 99, 235, 0.08);
  background:
    radial-gradient(circle at top right, rgba(37, 99, 235, 0.12), transparent 28%),
    linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(248, 250, 252, 0.92));
  box-shadow: 0 24px 60px rgba(15, 23, 42, 0.08);
}

.dashboard-shell .screen-hero h1 {
  font-size: clamp(2rem, 3vw, 3rem);
  line-height: 1.05;
}

.dashboard-shell .screen-avatar {
  width: 88px;
  height: 88px;
  box-shadow: 0 18px 36px rgba(37, 99, 235, 0.2);
}

.dashboard-shell .stat-grid {
  gap: var(--space-5);
}

.dashboard-shell .stat-card {
  position: relative;
  overflow: hidden;
  padding: var(--space-5);
  border: 1px solid rgba(229, 231, 235, 0.92);
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(248, 250, 252, 0.94));
  box-shadow: var(--shadow-sm);
}

.dashboard-shell .stat-card::after {
  content: '';
  position: absolute;
  inset: auto -16px -16px auto;
  width: 84px;
  height: 84px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(37, 99, 235, 0.12), transparent 70%);
}

.dashboard-shell .content-grid.two-col {
  align-items: start;
}

.dashboard-shell .card {
  border: 1px solid rgba(229, 231, 235, 0.9);
  box-shadow: var(--shadow-sm);
}

.dashboard-shell .card-header {
  margin-bottom: var(--space-3);
}

.dashboard-shell .card-title {
  font-size: var(--text-lg);
}

.dashboard-shell .action-grid {
  gap: var(--space-3);
}

.dashboard-shell .action-card {
  position: relative;
  min-height: 128px;
  padding: var(--space-5);
  border: 1px solid rgba(37, 99, 235, 0.08);
  background: linear-gradient(180deg, rgba(248, 250, 252, 0.98), rgba(255, 255, 255, 0.94));
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.05);
  transition: transform var(--transition-base), box-shadow var(--transition-base), border-color var(--transition-base);
}

.dashboard-shell .action-card:hover {
  transform: translateY(-3px);
  border-color: rgba(37, 99, 235, 0.18);
  box-shadow: 0 18px 36px rgba(37, 99, 235, 0.14);
}

.dashboard-shell .action-card span:first-child {
  width: 44px;
  height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-lg);
  background: linear-gradient(135deg, var(--color-primary-50), var(--color-info-50));
  font-size: 1.25rem;
}

.dashboard-shell .list-row,
.dashboard-shell .event-card,
.dashboard-shell .booking-card,
.dashboard-shell .notification-card,
.dashboard-shell .bill-card,
.dashboard-shell .history-card,
.dashboard-shell .member-card,
.dashboard-shell .faq-item {
  padding-block: var(--space-4);
}

.dashboard-shell .detail-list,
.dashboard-shell .stack {
  gap: var(--space-3);
}
</style>