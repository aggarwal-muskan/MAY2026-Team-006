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
            <div v-for="point in analyticsData.complaintsOverTime" :key="point.month" class="bar-item">
              <span class="bar" :style="{ height: `${point.count * 4}px` }"></span>
              <small>{{ point.month }}</small>
            </div>
          </div>
        </section>
        <section class="card chart-card">
          <h3 class="card-title">Bookings by Service</h3>
          <div v-for="(value, key) in analyticsData.bookingsByService" :key="key" class="progress-row">
            <span>{{ key }}</span>
            <div class="progress"><span :style="{ width: `${Math.min(value * 4, 100)}%` }"></span></div>
          </div>
        </section>
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
          <tbody><tr v-for="resident in residents" :key="resident.id"><td>{{ resident.name }}</td><td>{{ resident.flat }}</td><td>{{ resident.phone }}</td><td>{{ resident.email }}</td><td><span class="badge" :class="badgeClass(resident.status)">{{ resident.status }}</span></td></tr></tbody>
        </table>
      </div>
    </template>

    <template v-else-if="page === 'tenants'">
      <div class="screen-header"><h1>Tenants</h1><p>Track tenant leases and contact details.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Name</th><th>Flat No</th><th>Owner</th><th>Lease Start</th><th>Lease End</th><th>Status</th></tr></thead><tbody><tr v-for="tenant in tenants" :key="tenant.id"><td>{{ tenant.name }}</td><td>{{ tenant.flat }}</td><td>{{ tenant.owner }}</td><td>{{ tenant.leaseStart }}</td><td>{{ tenant.leaseEnd }}</td><td><span class="badge" :class="badgeClass(tenant.status)">{{ tenant.status }}</span></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'providers'">
      <div class="screen-header row-between"><div><h1>Providers</h1><p>Manage service provider listings.</p></div><button class="btn btn-primary">Add Provider</button></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Name</th><th>Service</th><th>Phone</th><th>Rating</th></tr></thead><tbody><tr v-for="provider in serviceProviders" :key="provider.id"><td>{{ provider.name }}</td><td>{{ provider.category }}</td><td>{{ provider.phone }}</td><td>{{ provider.rating }}</td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'complaints'">
      <div class="screen-header"><h1>Complaints Management</h1><p>Assign and track complaint resolution.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>ID</th><th>Title</th><th>Resident</th><th>Status</th><th>Assign</th></tr></thead><tbody><tr v-for="complaint in complaints" :key="complaint.id"><td>{{ complaint.id }}</td><td>{{ complaint.title }}</td><td>{{ complaint.resident }}</td><td><span class="badge" :class="badgeClass(complaint.status)">{{ complaint.status }}</span></td><td><select><option>Maintenance Team</option><option>Security Team</option><option>Housekeeping Team</option></select></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'notices'">
      <div class="screen-header row-between"><div><h1>Notice Management</h1><p>Publish, edit, or remove notices.</p></div><router-link to="/admin/notices/create" class="btn btn-primary">Create Notice</router-link></div>
      <div class="stack"><article v-for="notice in notices" :key="notice.id" class="card notice-row"><div><strong>{{ notice.title }}</strong><p>{{ notice.content }}</p></div><div class="row-actions"><button class="btn btn-outline btn-sm">Edit</button><button class="btn btn-danger btn-sm">Delete</button></div></article></div>
    </template>

    <template v-else-if="page === 'create-notice'">
      <div class="screen-header"><h1>Create Notice</h1><p>Write and publish a new society notice.</p></div>
      <form class="card form-card" @submit.prevent="notify.success('Notice published')"><label class="form-group"><span class="form-label">Title</span><input type="text" /></label><label class="form-group"><span class="form-label">Category</span><select><option>Maintenance</option><option>Event</option><option>Rules</option><option>Security</option></select></label><label class="form-group"><span class="form-label">Content</span><textarea rows="5"></textarea></label><button class="btn btn-primary">Publish</button></form>
    </template>

    <template v-else-if="page === 'events'">
      <div class="screen-header row-between"><div><h1>Events Management</h1><p>Monitor event listings and attendance.</p></div><router-link to="/admin/events/create" class="btn btn-primary">Create Event</router-link></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Event</th><th>Date</th><th>Venue</th><th>Status</th></tr></thead><tbody><tr v-for="event in events" :key="event.id"><td>{{ event.title }}</td><td>{{ event.date }}</td><td>{{ event.venue }}</td><td><span class="badge badge-success">Scheduled</span></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'create-event'">
      <div class="screen-header"><h1>Create Event</h1><p>Set up a new community activity.</p></div>
      <form class="card form-card" @submit.prevent="notify.success('Event created')"><div class="form-grid two-col"><label class="form-group"><span class="form-label">Event Name</span><input type="text" /></label><label class="form-group"><span class="form-label">Category</span><input type="text" /></label></div><div class="form-grid two-col"><label class="form-group"><span class="form-label">Date / Time</span><input type="text" /></label><label class="form-group"><span class="form-label">Venue</span><input type="text" /></label></div><label class="form-group"><span class="form-label">Description</span><textarea rows="5"></textarea></label><button class="btn btn-primary">Create Event</button></form>
    </template>

    <template v-else-if="page === 'parking'">
      <div class="screen-header"><h1>Parking Management</h1><p>Color-coded parking slots across the society.</p></div>
      <div class="parking-grid admin-parking">
        <div v-for="slot in parkingSlots" :key="slot.id" class="parking-slot" :class="slot.status.toLowerCase()">{{ slot.id }}</div>
      </div>
    </template>

    <template v-else-if="page === 'assign-parking'">
      <div class="screen-header"><h1>Assign Parking</h1><p>Assign a slot to a resident and vehicle.</p></div>
      <form class="card form-card" @submit.prevent="notify.success('Parking slot assigned')"><div class="form-grid two-col"><label class="form-group"><span class="form-label">Resident</span><select><option v-for="resident in residents" :key="resident.id">{{ resident.name }}</option></select></label><label class="form-group"><span class="form-label">Slot</span><select><option v-for="slot in parkingSlots" :key="slot.id">{{ slot.id }}</option></select></label></div><label class="form-group"><span class="form-label">Vehicle Number</span><input type="text" /></label><button class="btn btn-primary">Assign Slot</button></form>
    </template>

    <template v-else-if="page === 'analytics'">
      <div class="screen-header"><h1>Analytics</h1><p>Usage, occupancy, and event trends.</p></div>
      <div class="content-grid two-col">
        <section class="card"><h3 class="card-title">Complaints</h3><div class="bar-chart"><div v-for="point in analyticsData.complaintsOverTime" :key="point.month" class="bar-item"><span class="bar" :style="{ height: `${point.count * 4}px` }"></span><small>{{ point.month }}</small></div></div></section>
        <section class="card"><h3 class="card-title">Occupancy</h3><div v-for="(value, key) in analyticsData.parkingUtilization" :key="key" class="progress-row"><span>{{ key }}</span><div class="progress"><span :style="{ width: `${value * 10}%` }"></span></div></div></section>
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
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useNotificationStore } from '@/stores/notificationStore'
import {
  analyticsData,
  complaints,
  events,
  maintenanceBills,
  notices,
  parkingSlots,
  residents,
  serviceProviders,
  systemLogs,
  tenants,
} from '@/data/mockData'
import { badgeClass, currency } from './screenUtils'

const route = useRoute()
const notify = useNotificationStore()
const page = computed(() => route.meta.page || 'dashboard')

const adminStats = [
  { label: 'Total Residents', value: 250 },
  { label: 'Pending Complaints', value: 15 },
  { label: 'Bookings Today', value: 28 },
  { label: 'Upcoming Events', value: 35 },
]

const roles = [
  { name: 'Resident', scope: 'Community access', access: 'Notices, complaints, bookings' },
  { name: 'Admin', scope: 'Full control', access: 'Residents, reports, management' },
  { name: 'Provider', scope: 'Service operations', access: 'Bookings, availability, earnings' },
  { name: 'Security', scope: 'Gate operations', access: 'Visitor and vehicle monitoring' },
]

const reports = [
  { title: 'Monthly Summary', description: 'Residents, complaints, and bookings overview.' },
  { title: 'Parking Snapshot', description: 'Available, occupied, and reserved slot report.' },
  { title: 'Notice Archive', description: 'Published notices and event communications.' },
]
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
.parking-grid { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: var(--space-3); }
.admin-parking .parking-slot { min-height: 72px; display: grid; place-items: center; }
.notice-row, .report-card { display: grid; gap: var(--space-3); }
.row-actions { display: flex; gap: var(--space-2); }
.form-card { display: grid; gap: var(--space-4); }
.form-grid.two-col { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-4); }
.switch-row { display: flex; align-items: center; justify-content: space-between; gap: var(--space-4); }
@media (max-width: 960px) {
  .stat-grid, .content-grid.two-col, .card-grid.three-col, .parking-grid, .form-grid.two-col { grid-template-columns: 1fr; }
  .screen-header.row-between { flex-direction: column; align-items: flex-start; }
}
</style>