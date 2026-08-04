<template>
  <div class="portal-screen admin-screen">
    <template v-if="page === 'dashboard'">
      <div class="dashboard-shell">
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
      </div>
    </template>

    <template v-else-if="page === 'residents'">
      <div class="screen-header row-between">
        <div><h1>Residents</h1><p>Search and manage resident records.</p></div>
        <button class="btn btn-primary">Add Resident</button>
      </div>
      <div class="card toolbar"><input type="text" placeholder="Search residents" /></div>
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
      <div class="screen-header row-between"><div><h1>Providers</h1><p>Manage service provider listings.</p></div><button class="btn btn-primary">Add Provider</button></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Name</th><th>Service</th><th>Phone</th><th>Rating</th></tr></thead><tbody><tr v-for="provider in providerRows" :key="provider.id"><td>{{ provider.business_name || provider.name }}</td><td>{{ provider.category || provider.category_id }}</td><td>{{ provider.phone || '-' }}</td><td>{{ provider.rating_avg || provider.rating || 0 }}</td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'complaints'">
      <div class="screen-header"><h1>Complaints Management</h1><p>Assign and track complaint resolution.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>ID</th><th>Title</th><th>Resident</th><th>Status</th><th>Assign</th></tr></thead><tbody><tr v-for="complaint in complaintRows" :key="complaint.id"><td>{{ complaint.id }}</td><td>{{ complaint.subject || complaint.title }}</td><td>{{ complaint.raised_by_user_id || complaint.resident || '-' }}</td><td><span class="badge" :class="badgeClass(complaint.status)">{{ complaint.status }}</span></td><td><div class="row-actions"><select v-model="complaintAssignments[complaint.id]"><option disabled value="">Select user</option><option v-for="person in assignableUsers" :key="person.id" :value="person.id">{{ person.name }}</option></select><button class="btn btn-secondary btn-sm" @click="assignComplaintToUser(complaint)">Assign</button></div></td></tr></tbody></table></div>
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
      <div class="card-grid three-col"><article v-for="report in reports" :key="report.title" class="card report-card"><h3>{{ report.title }}</h3><p>{{ report.description }}</p><button class="btn btn-outline btn-sm">Export</button></article></div>
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

const noticeForm = reactive({ title: '', body: '', notice_type: 'maintenance', priority: 'normal' })
const eventForm = reactive({ title: '', description: '', event_date: '', start_time: '', venue: '' })

const adminStats = computed(() => [
  { label: 'Total Residents', value: adminDashboardStats.value.total_residents ?? 0 },
  { label: 'Pending Complaints', value: adminDashboardStats.value.pending_complaints ?? 0 },
  { label: 'Bookings Today', value: adminDashboardStats.value.todays_bookings ?? 0 },
  { label: 'Upcoming Events', value: adminDashboardStats.value.upcoming_events ?? 0 },
])

const residentRows = computed(() => {
  return backendUsers.value
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
  return backendUsers.value.map((user) => ({ id: user.id, name: user.full_name || user.name || `User #${user.id}` }))
})

const adminAnalytics = computed(() => {
  const statusCounts = backendComplaints.value.reduce((acc, complaint) => {
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

const roles = [
  { name: 'Resident', scope: 'Community access', access: 'Notices, complaints, bookings' },
  { name: 'Admin', scope: 'Full control', access: 'Residents, reports, management' },
  { name: 'Provider', scope: 'Service operations', access: 'Bookings, availability, earnings' },
  { name: 'Security', scope: 'Gate operations', access: 'Visitor and vehicle monitoring' },
]

const reports = [
  { title: 'Monthly Summary', description: 'Residents, complaints, and bookings overview.' },
  { title: 'Security Snapshot', description: 'Visitor activity and gate operations summary.' },
  { title: 'Notice Archive', description: 'Published notices and event communications.' },
]

async function loadAdminData() {
  try {
    if (!authStore.user && authStore.token) {
      await authStore.fetchMe()
    }
    if (authStore.token) {
      backendUsers.value = await authStore.listUsers()
      backendProviders.value = await authStore.listProviders()
      backendComplaints.value = await authStore.listComplaints()
      backendNotices.value = await authStore.listNotices()
      backendEvents.value = await authStore.listEvents()
      adminDashboardStats.value = await authStore.getAdminDashboardStats()
      bookingStatusBreakdown.value = await authStore.getBookingsAnalytics()
    }
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to load admin data')
  }
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
.stat-grid, .card-grid, .content-grid { display: grid; gap: var(--space-5); }
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
.form-card { display: grid; gap: var(--space-5); }
.form-grid.two-col { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-5); }
.switch-row { display: flex; align-items: center; justify-content: space-between; gap: var(--space-4); padding: var(--space-2) 0; }
@media (max-width: 960px) {
  .stat-grid, .content-grid.two-col, .card-grid.three-col, .form-grid.two-col { grid-template-columns: 1fr; }
  .screen-header.row-between { flex-direction: column; align-items: flex-start; }
}

.dashboard-shell {
  display: grid;
  gap: var(--space-6);
}

.dashboard-shell .screen-header {
  padding: var(--space-6);
  border: 1px solid rgba(37, 99, 235, 0.08);
  border-radius: var(--radius-2xl);
  background:
    radial-gradient(circle at top right, rgba(37, 99, 235, 0.12), transparent 28%),
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
.dashboard-shell .chart-card,
.dashboard-shell .notice-row,
.dashboard-shell .report-card,
.dashboard-shell .form-card {
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

.dashboard-shell .chart-card,
.dashboard-shell .form-card {
  padding: var(--space-5);
}

.dashboard-shell .bar-chart {
  min-height: 240px;
}

.dashboard-shell .bar {
  background: linear-gradient(180deg, var(--color-primary-light), var(--color-primary-dark));
  box-shadow: 0 12px 24px rgba(37, 99, 235, 0.2);
}

.dashboard-shell .progress {
  height: 12px;
}

.dashboard-shell .toolbar {
  padding: var(--space-4);
  background: rgba(255, 255, 255, 0.9);
}

.dashboard-shell .notice-row,
.dashboard-shell .report-card {
  padding: var(--space-5) var(--space-6);
}

.dashboard-shell .switch-row {
  padding: var(--space-4) 0;
  border-bottom: 1px solid var(--color-border);
}

.dashboard-shell .switch-row:last-child {
  border-bottom: none;
}
</style>