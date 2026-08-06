<template>
  <div class="portal-screen admin-screen">
    <template v-if="page === 'dashboard'">
      <div class="screen-header">
        <h1>Admin Dashboard</h1>
        <p>Overview of residents, complaints, bookings, and events.</p>
      </div>
      <div class="stat-grid admin-stats">
        <div v-for="stat in adminStats" :key="stat.label" class="card stat-card">
          <div class="stat-label">{{ stat.label }}</div>
          <div class="stat-value">{{ stat.value }}</div>
        </div>
      </div>
      <div class="content-grid two-col">
        <section class="card chart-card">
          <h3 class="card-title">Complaints Trend</h3>
          <div class="bar-chart">
            <div v-for="point in adminAnalytics.complaintsOverTime" :key="point.month" class="bar-item">
              <span class="bar" :style="{ height: `${point.count * 4}px` }"></span>
              <small>{{ point.month }}</small>
            </div>
          </div>
        </section>
        <section class="card chart-card">
          <h3 class="card-title">Bookings by Status</h3>
          <div v-for="(value, key) in adminAnalytics.bookingsByService" :key="key" class="progress-row">
            <span>{{ key }}</span>
            <div class="progress"><span :style="{ width: `${Math.min(value * 4, 100)}%` }"></span></div>
          </div>
        </section>
      </div>
    </template>

    <template v-else-if="page === 'residents'">
      <div class="screen-header row-between">
        <div><h1>Residents</h1><p>Search and manage resident records.</p></div>
        <button class="btn btn-primary" @click="showResidentForm = !showResidentForm">{{ showResidentForm ? 'Cancel' : 'Add Resident' }}</button>
      </div>
      <form v-if="showResidentForm" class="card form-card" @submit.prevent="submitResident">
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Full Name</span><input v-model="residentForm.full_name" type="text" /></label><label class="form-group"><span class="form-label">Email</span><input v-model="residentForm.email" type="email" /></label></div>
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Phone</span><input v-model="residentForm.phone" type="text" /></label><label class="form-group"><span class="form-label">Password</span><input v-model="residentForm.password" type="password" /></label></div>
        <button class="btn btn-primary">Create Resident</button>
      </form>
      <div class="card toolbar"><input v-model="userSearchQuery" type="text" placeholder="Search users (name, email, phone, role)" /></div>
      <div class="card table-wrap">
        <table class="data-table">
          <thead><tr><th>Name</th><th>Flat No</th><th>Phone</th><th>Email</th><th>Status</th></tr></thead>
          <tbody><tr v-for="resident in residentRows" :key="resident.id"><td>{{ resident.name }}</td><td>{{ resident.flat }}</td><td>{{ resident.phone }}</td><td>{{ resident.email }}</td><td><span class="badge" :class="badgeClass(resident.status)">{{ resident.status }}</span></td></tr></tbody>
        </table>
      </div>
    </template>

    <template v-else-if="page === 'tenants'">
      <div class="screen-header"><h1>Tenants</h1><p>Track tenant leases and contact details.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Name</th><th>Flat No</th><th>Owner</th><th>Lease Start</th><th>Lease End</th><th>Status</th></tr></thead><tbody><tr v-for="tenant in tenants" :key="tenant.id"><td>{{ tenant.name }}</td><td>{{ tenant.flat }}</td><td>{{ tenant.owner }}</td><td>{{ tenant.leaseStart }}</td><td>{{ tenant.leaseEnd }}</td><td><span class="badge" :class="badgeClass(tenant.status)">{{ tenant.status }}</span></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'providers'">
      <div class="screen-header row-between"><div><h1>Providers</h1><p>Manage service provider listings.</p></div><button class="btn btn-primary" @click="showProviderForm = !showProviderForm">{{ showProviderForm ? 'Cancel' : 'Add Provider' }}</button></div>
      <form v-if="showProviderForm" class="card form-card" @submit.prevent="submitProvider">
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Provider Name</span><input v-model="providerForm.full_name" type="text" /></label><label class="form-group"><span class="form-label">Email</span><input v-model="providerForm.email" type="email" /></label></div>
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Phone</span><input v-model="providerForm.phone" type="text" /></label><label class="form-group"><span class="form-label">Password</span><input v-model="providerForm.password" type="password" /></label></div>
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Category</span><select v-model="providerForm.category_id"><option disabled value="">Select category</option><option v-for="category in serviceCategories" :key="category.id" :value="category.id">{{ category.name }}</option></select></label><label class="form-group"><span class="form-label">Business Name</span><input v-model="providerForm.business_name" type="text" /></label></div>
        <label class="form-group"><span class="form-label">Service Description</span><textarea v-model="providerForm.service_description" rows="3"></textarea></label>
        <button class="btn btn-primary">Create Provider</button>
      </form>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Name</th><th>Service</th><th>Phone</th><th>Rating</th></tr></thead><tbody><tr v-for="provider in providerRows" :key="provider.id"><td>{{ provider.business_name || provider.name }}</td><td>{{ provider.category || provider.category_id }}</td><td>{{ provider.phone || '-' }}</td><td>{{ provider.rating_avg || provider.rating || 0 }}</td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'complaints'">
      <div class="screen-header"><h1>Complaints Management</h1><p>Assign and track complaint resolution.</p></div>
      <div class="card toolbar"><input v-model="userSearchQuery" type="text" placeholder="Search assign users (name, email, phone, role)" /></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>ID</th><th>Title</th><th>Resident</th><th>Status</th><th>Assign</th></tr></thead><tbody><tr v-for="complaint in complaintRows" :key="complaint.id"><td>{{ complaint.id }}</td><td>{{ complaint.subject || complaint.title }}</td><td>{{ complaint.raised_by_user_id || complaint.resident || '-' }}</td><td><span class="badge" :class="badgeClass(complaint.status)">{{ complaint.status }}</span></td><td><div class="row-actions"><template v-if="canAssignComplaint(complaint)"><select v-model="complaintAssignments[complaint.id]"><option disabled value="">Select user</option><option v-for="person in assignableUsers" :key="person.id" :value="person.id">{{ person.name }}</option></select><button class="btn btn-secondary btn-sm" @click="assignComplaintToUser(complaint)">{{ complaint.assigned_to_user_id ? 'Reassign' : 'Assign' }}</button></template><span v-else class="chip">Closed</span></div></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'notices'">
      <div class="screen-header row-between"><div><h1>Notice Management</h1><p>Publish, edit, or remove notices.</p></div><router-link to="/admin/notices/create" class="btn btn-primary">Create Notice</router-link></div>
      <div class="stack"><article v-for="notice in noticeRows" :key="notice.id" class="card notice-row"><div><strong>{{ notice.title }}</strong><p>{{ notice.body || notice.content }}</p></div><div class="row-actions"><button class="btn btn-danger btn-sm" @click="removeNotice(notice.id)">Delete</button></div></article></div>
    </template>

    <template v-else-if="page === 'create-notice'">
      <div class="screen-header"><h1>Create Notice</h1><p>Write and publish a new society notice.</p></div>
      <form class="card form-card" @submit.prevent="submitNotice"><label class="form-group"><span class="form-label">Title</span><input v-model="noticeForm.title" type="text" /></label><label class="form-group"><span class="form-label">Category</span><select v-model="noticeForm.notice_type"><option value="maintenance">Maintenance</option><option value="event">Event</option><option value="rules">Rules</option><option value="security">Security</option></select></label><label class="form-group"><span class="form-label">Priority</span><select v-model="noticeForm.priority"><option value="low">Low</option><option value="normal">Normal</option><option value="high">High</option><option value="urgent">Urgent</option></select></label><label class="form-group"><span class="form-label">Content</span><textarea v-model="noticeForm.body" rows="5"></textarea></label><button class="btn btn-primary">Publish</button></form>
    </template>

    <template v-else-if="page === 'events'">
      <div class="screen-header row-between"><div><h1>Events Management</h1><p>Monitor event listings and attendance.</p></div><router-link to="/admin/events/create" class="btn btn-primary">Create Event</router-link></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Event</th><th>Date</th><th>Venue</th><th>Status</th><th>Action</th></tr></thead><tbody><tr v-for="event in eventRows" :key="event.id"><td>{{ event.title }}</td><td>{{ event.event_date || event.date }}</td><td>{{ event.venue }}</td><td><span class="badge" :class="badgeClass(event.status || 'scheduled')">{{ event.status || 'scheduled' }}</span></td><td><button class="btn btn-danger btn-sm" @click="removeEvent(event.id)">Delete</button></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'create-event'">
      <div class="screen-header"><h1>Create Event</h1><p>Set up a new community activity.</p></div>
      <form class="card form-card" @submit.prevent="submitEvent"><div class="form-grid two-col"><label class="form-group"><span class="form-label">Event Name</span><input v-model="eventForm.title" type="text" /></label><label class="form-group"><span class="form-label">Date</span><input v-model="eventForm.event_date" type="date" /></label></div><div class="form-grid two-col"><label class="form-group"><span class="form-label">Start Time</span><input v-model="eventForm.start_time" type="time" /></label><label class="form-group"><span class="form-label">Venue</span><input v-model="eventForm.venue" type="text" /></label></div><label class="form-group"><span class="form-label">Description</span><textarea v-model="eventForm.description" rows="5"></textarea></label><button class="btn btn-primary">Create Event</button></form>
    </template>

    <template v-else-if="page === 'analytics'">
      <div class="screen-header"><h1>Analytics</h1><p>Usage, occupancy, and event trends.</p></div>
      <div class="content-grid two-col">
        <section class="card"><h3 class="card-title">Complaints</h3><div class="bar-chart"><div v-for="point in adminAnalytics.complaintsOverTime" :key="point.month" class="bar-item"><span class="bar" :style="{ height: `${point.count * 4}px` }"></span><small>{{ point.month }}</small></div></div></section>
        <section class="card"><h3 class="card-title">Complaint Status</h3><div v-for="(value, key) in adminAnalytics.complaintsByStatus" :key="key" class="progress-row"><span>{{ key }}</span><div class="progress"><span :style="{ width: `${Math.min(value * 5, 100)}%` }"></span></div></div></section>
      </div>
    </template>

    <template v-else-if="page === 'settings'">
      <div class="screen-header"><h1>Admin Settings</h1><p>Basic administrative preferences.</p></div>
      <form class="card form-card"><label class="switch-row"><span>Maintenance reminders</span><input type="checkbox" checked /></label><label class="switch-row"><span>Email alerts</span><input type="checkbox" checked /></label><label class="switch-row"><span>Auto approvals</span><input type="checkbox" /></label></form>
    </template>

    <template v-else-if="page === 'roles'">
      <div class="screen-header"><h1>Roles & Permissions</h1><p>Define access control by role.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Role</th><th>Scope</th><th>Access</th></tr></thead><tbody><tr v-for="role in roles" :key="role.name"><td>{{ role.name }}</td><td>{{ role.scope }}</td><td>{{ role.access }}</td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'maintenance-fees'">
      <div class="screen-header"><h1>Maintenance Fees</h1><p>Fee overview and recent payments.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Month</th><th>Amount</th><th>Status</th></tr></thead><tbody><tr v-for="bill in maintenanceBills" :key="bill.id"><td>{{ bill.month }}</td><td>{{ currency(bill.amount) }}</td><td><span class="badge" :class="badgeClass(bill.status)">{{ bill.status }}</span></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'reports'">
      <div class="screen-header"><h1>Reports & Export</h1><p>Download operational summaries.</p></div>
      <div class="stat-grid admin-stats"><div class="card stat-card" v-for="item in reportSummaryCards" :key="item.label"><div class="stat-label">{{ item.label }}</div><div class="stat-value">{{ item.value }}</div></div></div>
      <div class="card report-card"><h3>Monthly Report Export</h3><p>Download current month operations snapshot in CSV format.</p><button class="btn btn-outline btn-sm" :disabled="isExporting" @click="exportMonthlyReport">{{ isExporting ? 'Exporting...' : 'Export CSV' }}</button></div>
    </template>

    <template v-else-if="page === 'logs'">
      <div class="screen-header"><h1>System Logs</h1><p>Audit trail of key admin actions.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Action</th><th>User</th><th>Timestamp</th><th>Details</th></tr></thead><tbody><tr v-for="log in systemLogs" :key="log.id"><td>{{ log.action }}</td><td>{{ log.user }}</td><td>{{ log.timestamp }}</td><td>{{ log.details }}</td></tr></tbody></table></div>
    </template>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'
import { useNotificationStore } from '@/stores/notificationStore'
import {
  maintenanceBills,
  systemLogs,
  tenants,
} from '@/data/mockData'
import { badgeClass, currency } from './screenUtils'

const route = useRoute()
const authStore = useAuthStore()
const notify = useNotificationStore()
const page = computed(() => route.meta.page || 'dashboard')

const backendUsers = ref([])
const backendProviders = ref([])
const backendComplaints = ref([])
const backendNotices = ref([])
const backendEvents = ref([])
const adminDashboardStats = ref({})
const complaintAssignments = ref({})
const bookingStatusBreakdown = ref({})
const complaintStatusBreakdown = ref({})
const serviceCategories = ref([])
const monthlyReport = ref({})
const showResidentForm = ref(false)
const showProviderForm = ref(false)
const isExporting = ref(false)
const userSearchQuery = ref('')

const noticeForm = reactive({ title: '', body: '', notice_type: 'maintenance', priority: 'normal' })
const eventForm = reactive({ title: '', description: '', event_date: '', start_time: '', venue: '' })
const residentForm = reactive({ full_name: '', email: '', phone: '', password: '' })
const providerForm = reactive({ full_name: '', email: '', phone: '', password: '', category_id: '', business_name: '', service_description: '' })

const adminStats = computed(() => [
  { label: 'Total Residents', value: adminDashboardStats.value.total_residents ?? 0 },
  { label: 'Pending Complaints', value: pendingComplaintsCount.value },
  { label: 'Bookings Today', value: adminDashboardStats.value.todays_bookings ?? 0 },
  { label: 'Upcoming Events', value: adminDashboardStats.value.upcoming_events ?? 0 },
])

const pendingComplaintsCount = computed(() => {
  const openCount = Number(complaintStatusBreakdown.value.open || 0)
  const inProgressCount = Number(complaintStatusBreakdown.value.in_progress || 0)
  if (openCount || inProgressCount) return openCount + inProgressCount
  return backendComplaints.value.filter((item) => ['open', 'in_progress'].includes(String(item.status || '').toLowerCase())).length
})

const filteredUsers = computed(() => {
  const query = String(userSearchQuery.value || '').trim().toLowerCase()
  if (!query) return backendUsers.value

  return backendUsers.value.filter((user) => {
    const haystack = [
      user.full_name,
      user.name,
      user.email,
      user.phone,
      user.role,
      user.unit_number,
      user.flat,
      user.status,
    ].map((value) => String(value || '').toLowerCase())

    return haystack.some((value) => value.includes(query))
  })
})

const residentRows = computed(() => {
  return filteredUsers.value
    .filter((user) => ['owner', 'tenant'].includes(user.role))
    .map((user) => ({
      id: user.id,
      name: user.full_name || user.name,
      flat: user.unit_number || user.flat || '-',
      phone: user.phone || '-',
      email: user.email,
      status: user.status || 'active',
    }))
})

const providerRows = computed(() => {
  return backendProviders.value
})

const complaintRows = computed(() => {
  return backendComplaints.value
})

const noticeRows = computed(() => {
  return backendNotices.value
})

const eventRows = computed(() => {
  return backendEvents.value
})

const assignableUsers = computed(() => {
  const roles = new Set(['admin', 'security', 'service_provider'])
  return filteredUsers.value
    .filter((user) => roles.has(String(user.role || '').toLowerCase()))
    .map((user) => ({ id: user.id, name: user.full_name || user.name || `User #${user.id}` }))
})

async function loadAllUsers() {
  const limit = 100
  let page = 1
  let pages = 1
  const allItems = []

  do {
    const query = new URLSearchParams({ page: String(page), limit: String(limit) }).toString()
    const payload = await authStore.listUsers(query, { withMeta: true })
    const items = payload?.items || []
    allItems.push(...items)

    const totalPages = Number(payload?.pagination?.pages || 1)
    pages = Number.isFinite(totalPages) && totalPages > 0 ? totalPages : 1
    page += 1
  } while (page <= pages)

  return allItems
}

const adminAnalytics = computed(() => {
  const statusCounts = Object.keys(complaintStatusBreakdown.value).length
    ? complaintStatusBreakdown.value
    : backendComplaints.value.reduce((acc, complaint) => {
      const key = complaint.status || 'open'
      acc[key] = (acc[key] || 0) + 1
      return acc
    }, {})

  const monthCounts = backendComplaints.value.reduce((acc, complaint) => {
    if (!complaint.created_at) return acc
    const date = new Date(complaint.created_at)
    if (Number.isNaN(date.getTime())) return acc
    const month = date.toLocaleString('en-US', { month: 'short' })
    acc[month] = (acc[month] || 0) + 1
    return acc
  }, {})

  const complaintsOverTime = Object.entries(monthCounts).map(([month, count]) => ({ month, count }))

  return {
    complaintsOverTime,
    bookingsByService: bookingStatusBreakdown.value,
    complaintsByStatus: statusCounts,
  }
})

const reportSummaryCards = computed(() => {
  const data = monthlyReport.value || {}
  return [
    { label: 'Residents', value: data?.residents?.total ?? 0 },
    { label: 'Complaints', value: data?.complaints?.raised ?? 0 },
    { label: 'Bookings', value: data?.bookings?.total ?? 0 },
    { label: 'Visitors', value: data?.visitors?.total ?? 0 },
  ]
})

const roles = [
  { name: 'Resident', scope: 'Community access', access: 'Notices, complaints, bookings' },
  { name: 'Admin', scope: 'Full control', access: 'Residents, reports, management' },
  { name: 'Provider', scope: 'Service operations', access: 'Bookings, availability, earnings' },
  { name: 'Security', scope: 'Gate operations', access: 'Visitor and vehicle monitoring' },
]

async function loadAdminData() {
  try {
    if (!authStore.user && authStore.token) {
      await authStore.fetchMe()
    }
    if (authStore.token) {
      const [
        usersResult,
        providersResult,
        complaintsResult,
        noticesResult,
        eventsResult,
        dashboardResult,
        bookingsAnalyticsResult,
        complaintsAnalyticsResult,
        categoriesResult,
        monthlyReportResult,
      ] = await Promise.allSettled([
        loadAllUsers(),
        authStore.listProviders(),
        authStore.listComplaints(),
        authStore.listNotices(),
        authStore.listEvents(),
        authStore.getAdminDashboardStats(),
        authStore.getBookingsAnalytics(),
        authStore.getComplaintsAnalytics(),
        authStore.listServiceCategories(),
        authStore.getMonthlyReport(),
      ])

      if (usersResult.status === 'fulfilled') backendUsers.value = usersResult.value
      if (providersResult.status === 'fulfilled') backendProviders.value = providersResult.value
      if (complaintsResult.status === 'fulfilled') {
        backendComplaints.value = complaintsResult.value
        syncComplaintAssignments()
      }
      if (noticesResult.status === 'fulfilled') backendNotices.value = noticesResult.value
      if (eventsResult.status === 'fulfilled') backendEvents.value = eventsResult.value
      if (dashboardResult.status === 'fulfilled') adminDashboardStats.value = dashboardResult.value
      if (bookingsAnalyticsResult.status === 'fulfilled') bookingStatusBreakdown.value = bookingsAnalyticsResult.value
      if (complaintsAnalyticsResult.status === 'fulfilled') complaintStatusBreakdown.value = complaintsAnalyticsResult.value
      if (categoriesResult.status === 'fulfilled') serviceCategories.value = categoriesResult.value
      if (monthlyReportResult.status === 'fulfilled') monthlyReport.value = monthlyReportResult.value
    }
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to load admin data')
  }
}

async function submitResident() {
  try {
    await authStore.createUser({
      society_id: authStore.user?.society_id || 1,
      role: 'owner',
      full_name: String(residentForm.full_name || '').trim(),
      email: String(residentForm.email || '').trim(),
      phone: String(residentForm.phone || '').trim(),
      password: String(residentForm.password || ''),
      status: 'active',
    })
    residentForm.full_name = ''
    residentForm.email = ''
    residentForm.phone = ''
    residentForm.password = ''
    showResidentForm.value = false
    await loadAdminData()
    notify.success('Resident added successfully')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to add resident')
  }
}

async function submitProvider() {
  try {
    const createdUser = await authStore.createUser({
      society_id: authStore.user?.society_id || 1,
      role: 'service_provider',
      full_name: String(providerForm.full_name || '').trim(),
      email: String(providerForm.email || '').trim(),
      phone: String(providerForm.phone || '').trim(),
      password: String(providerForm.password || ''),
      status: 'active',
    })

    await authStore.createProvider({
      user_id: createdUser.id,
      category_id: Number(providerForm.category_id),
      business_name: String(providerForm.business_name || '').trim(),
      service_description: String(providerForm.service_description || '').trim(),
    })

    providerForm.full_name = ''
    providerForm.email = ''
    providerForm.phone = ''
    providerForm.password = ''
    providerForm.category_id = ''
    providerForm.business_name = ''
    providerForm.service_description = ''
    showProviderForm.value = false
    await loadAdminData()
    notify.success('Provider added successfully')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to add provider')
  }
}

async function exportMonthlyReport() {
  try {
    isExporting.value = true
    const blob = await authStore.exportMonthlyReportCsv()
    const url = URL.createObjectURL(blob)
    const anchor = document.createElement('a')
    anchor.href = url
    anchor.download = `monthly-report-${new Date().toISOString().slice(0, 10)}.csv`
    document.body.appendChild(anchor)
    anchor.click()
    anchor.remove()
    URL.revokeObjectURL(url)
    notify.success('Report exported')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to export report')
  } finally {
    isExporting.value = false
  }
}

function canAssignComplaint(complaint) {
  const status = String(complaint.status || '').toLowerCase()
  return status !== 'closed'
}

function syncComplaintAssignments() {
  const next = { ...complaintAssignments.value }
  for (const complaint of backendComplaints.value) {
    next[complaint.id] = complaint.assigned_to_user_id || ''
  }
  complaintAssignments.value = next
}

async function assignComplaintToUser(complaint) {
  const selectedUserId = Number(complaintAssignments.value[complaint.id])
  if (!selectedUserId) {
    notify.error('Select a user to assign the complaint')
    return
  }

  try {
    await authStore.assignComplaint(complaint.id, selectedUserId)
    backendComplaints.value = await authStore.listComplaints()
    syncComplaintAssignments()
    complaintStatusBreakdown.value = await authStore.getComplaintsAnalytics()
    notify.success('Complaint assigned successfully')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to assign complaint')
  }
}

async function submitNotice() {
  try {
    await authStore.createNotice({
      title: String(noticeForm.title || '').trim(),
      body: String(noticeForm.body || '').trim(),
      notice_type: noticeForm.notice_type,
      priority: noticeForm.priority,
    })
    backendNotices.value = await authStore.listNotices()
    noticeForm.title = ''
    noticeForm.body = ''
    notify.success('Notice published')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to publish notice')
  }
}

async function removeNotice(noticeId) {
  try {
    await authStore.deleteNotice(noticeId)
    backendNotices.value = await authStore.listNotices()
    notify.success('Notice deleted')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to delete notice')
  }
}

async function submitEvent() {
  try {
    await authStore.createEvent({
      title: String(eventForm.title || '').trim(),
      description: String(eventForm.description || '').trim(),
      event_date: eventForm.event_date,
      start_time: eventForm.start_time,
      venue: String(eventForm.venue || '').trim(),
    })
    backendEvents.value = await authStore.listEvents()
    eventForm.title = ''
    eventForm.description = ''
    eventForm.event_date = ''
    eventForm.start_time = ''
    eventForm.venue = ''
    notify.success('Event created')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to create event')
  }
}

async function removeEvent(eventId) {
  try {
    await authStore.deleteEvent(eventId)
    backendEvents.value = await authStore.listEvents()
    notify.success('Event deleted')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to delete event')
  }
}

onMounted(() => {
  loadAdminData()
})
</script>

<style scoped>
.portal-screen { display: grid; gap: var(--space-6); }
.screen-header { display: grid; gap: var(--space-2); }
.screen-header h1 { margin: 0; }
.screen-header p { color: var(--color-text-secondary); }
.screen-header.row-between { display: flex; align-items: center; justify-content: space-between; gap: var(--space-4); }
.stat-grid, .card-grid, .content-grid { display: grid; gap: var(--space-4); }
.stat-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.admin-stats .stat-value { font-size: var(--text-3xl); font-weight: var(--font-bold); margin-top: var(--space-2); }
.content-grid.two-col { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.table-wrap { overflow-x: auto; }
.bar-chart { display: flex; align-items: end; gap: var(--space-4); min-height: 220px; padding-top: var(--space-6); }
.bar-item { display: grid; justify-items: center; gap: var(--space-2); flex: 1; }
.bar { width: 100%; max-width: 36px; border-radius: var(--radius-md) var(--radius-md) 0 0; background: linear-gradient(180deg, var(--color-primary-light), var(--color-primary)); }
.progress-row { display: grid; gap: var(--space-2); margin-bottom: var(--space-4); }
.progress { height: 10px; border-radius: var(--radius-full); background: var(--color-gray-100); overflow: hidden; }
.progress span { display: block; height: 100%; background: linear-gradient(90deg, var(--color-secondary), var(--color-info)); }
.toolbar { margin-bottom: var(--space-2); }
.toolbar input { width: 100%; }
.notice-row, .report-card { display: grid; gap: var(--space-3); }
.row-actions { display: flex; gap: var(--space-2); }
.form-card { display: grid; gap: var(--space-4); }
.form-grid.two-col { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-4); }
.switch-row { display: flex; align-items: center; justify-content: space-between; gap: var(--space-4); }
@media (max-width: 960px) {
  .stat-grid, .content-grid.two-col, .card-grid.three-col, .form-grid.two-col { grid-template-columns: 1fr; }
  .screen-header.row-between { flex-direction: column; align-items: flex-start; }
}
</style>