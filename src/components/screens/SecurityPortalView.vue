<template>
  <div class="portal-screen security-screen">
    <template v-if="page === 'dashboard'">
      <div class="screen-header"><h1>Security Dashboard</h1><p>Monitor visitor flow, patrol activity, and parking access.</p></div>
      <div class="stat-grid"><div v-for="stat in securityStats" :key="stat.label" class="card stat-card"><div class="stat-label">{{ stat.label }}</div><div class="stat-value">{{ stat.value }}</div></div></div>
      <div class="content-grid two-col"><section class="card"><h3 class="card-title">Recent Entries</h3><div v-for="entry in visitorLogs.slice(0, 4)" :key="entry.id" class="list-row"><div><strong>{{ entry.name }}</strong><p>{{ entry.purpose }} · {{ entry.flat }}</p></div><span class="badge" :class="badgeClass(entry.status)">{{ entry.status }}</span></div></section><section class="card"><h3 class="card-title">Quick Actions</h3><div class="chip-row"><router-link to="/security/visitor-entry" class="chip-link">Visitor Entry</router-link><router-link to="/security/parking" class="chip-link">Parking Monitor</router-link><router-link to="/security/vehicles" class="chip-link">Vehicle Logs</router-link></div></section></div>
    </template>

    <template v-else-if="page === 'visitor-entry'">
      <div class="screen-header"><h1>Visitor Entry</h1><p>Log visitors and approve access.</p></div>
      <div class="content-grid two-col"><form class="card form-card" @submit.prevent="notify.success('Visitor entry saved')"><label class="form-group"><span class="form-label">Name</span><input type="text" /></label><label class="form-group"><span class="form-label">Purpose</span><input type="text" /></label><label class="form-group"><span class="form-label">Flat Visiting</span><input type="text" /></label><label class="form-group"><span class="form-label">Entry Time</span><input type="text" /></label><button class="btn btn-primary">Save Entry</button></form><section class="card table-wrap"><h3 class="card-title">Recent Visitor Log</h3><table class="data-table"><thead><tr><th>Name</th><th>Purpose</th><th>Status</th></tr></thead><tbody><tr v-for="entry in visitorLogs" :key="entry.id"><td>{{ entry.name }}</td><td>{{ entry.purpose }}</td><td><span class="badge" :class="badgeClass(entry.status)">{{ entry.status }}</span></td></tr></tbody></table></section></div>
    </template>

    <template v-else-if="page === 'parking-monitor'">
      <div class="screen-header"><h1>Parking Monitor</h1><p>Live parking status across all blocks.</p></div>
      <div class="stat-grid"><div class="card stat-card"><div class="stat-label">Total Vehicles</div><div class="stat-value">32</div></div><div class="card stat-card"><div class="stat-label">Available Slots</div><div class="stat-value">5</div></div><div class="card stat-card"><div class="stat-label">Occupied</div><div class="stat-value">9</div></div></div>
      <div class="parking-grid"><div v-for="slot in parkingSlots" :key="slot.id" class="parking-slot" :class="slot.status.toLowerCase()">{{ slot.id }}</div></div>
    </template>

    <template v-else-if="page === 'vehicle-logs'">
      <div class="screen-header"><h1>Vehicle Logs</h1><p>Search entry and exit records by vehicle number.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Vehicle No</th><th>Type</th><th>Flat</th><th>Entry</th><th>Status</th></tr></thead><tbody><tr v-for="vehicle in vehicleLogs" :key="vehicle.id"><td>{{ vehicle.vehicleNo }}</td><td>{{ vehicle.type }}</td><td>{{ vehicle.flat }}</td><td>{{ vehicle.entry }}</td><td><span class="badge" :class="badgeClass(vehicle.status)">{{ vehicle.status }}</span></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'patrol-log'">
      <div class="screen-header"><h1>Patrol Log</h1><p>Checkpoint and patrol notes for the current shift.</p></div>
      <div class="stack"><article v-for="entry in patrolItems" :key="entry.title" class="card patrol-row"><strong>{{ entry.title }}</strong><p>{{ entry.time }} · {{ entry.note }}</p></article></div>
    </template>

    <template v-else-if="page === 'visitor-approval'">
      <div class="screen-header"><h1>Visitor Approval</h1><p>Pending visitor approvals and gate clearance.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Visitor</th><th>Flat</th><th>Purpose</th><th>Action</th></tr></thead><tbody><tr v-for="entry in visitorLogs.slice(0, 3)" :key="entry.id"><td>{{ entry.name }}</td><td>{{ entry.flat }}</td><td>{{ entry.purpose }}</td><td><button class="btn btn-secondary btn-sm">Approve</button></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'emergency-alerts'">
      <div class="screen-header"><h1>Emergency Alerts</h1><p>Critical society notifications and incidents.</p></div>
      <div class="stack"><article v-for="alert in emergencyAlerts" :key="alert.id" class="card alert-row"><strong>{{ alert.title }}</strong><p>{{ alert.description }}</p><span class="badge" :class="badgeClass(alert.priority)">{{ alert.priority }}</span></article></div>
    </template>

    <template v-else-if="page === 'incident-reports'">
      <div class="screen-header"><h1>Incident Reports</h1><p>Documented incidents for follow-up and investigation.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Type</th><th>Location</th><th>Severity</th><th>Status</th></tr></thead><tbody><tr v-for="incident in incidentReports" :key="incident.id"><td>{{ incident.type }}</td><td>{{ incident.location }}</td><td>{{ incident.severity }}</td><td><span class="badge" :class="badgeClass(incident.status)">{{ incident.status }}</span></td></tr></tbody></table></div>
    </template>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useNotificationStore } from '@/stores/notificationStore'
import { emergencyAlerts, incidentReports, parkingSlots, vehicleLogs, visitorLogs } from '@/data/mockData'
import { badgeClass } from './screenUtils'

const route = useRoute()
const notify = useNotificationStore()
const page = computed(() => route.meta.page || 'dashboard')

const securityStats = [
  { label: 'Visitors Today', value: 12 },
  { label: 'Security Score', value: '85%' },
  { label: 'Pending Approvals', value: 3 },
]

const patrolItems = [
  { title: 'Gate A Checkpoint', time: '06:00 AM', note: 'All clear' },
  { title: 'Basement Patrol', time: '09:00 AM', note: 'Vehicle entry monitored' },
  { title: 'Garden Round', time: '11:00 AM', note: 'No incident reported' },
]
</script>

<style scoped>
.portal-screen { display: grid; gap: var(--space-6); }
.screen-header { display: grid; gap: var(--space-2); }
.screen-header h1 { margin: 0; }
.screen-header p { color: var(--color-text-secondary); }
.stat-grid, .content-grid { display: grid; gap: var(--space-4); }
.stat-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.stat-card .stat-value { font-size: var(--text-3xl); font-weight: var(--font-bold); margin-top: var(--space-2); }
.content-grid.two-col { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.list-row, .patrol-row, .alert-row { padding: var(--space-4) 0; border-bottom: 1px solid var(--color-border); display: flex; justify-content: space-between; gap: var(--space-4); }
.list-row:last-child, .patrol-row:last-child, .alert-row:last-child { border-bottom: none; }
.chip-row { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.chip-link { padding: 6px 12px; border-radius: var(--radius-full); background: var(--color-gray-100); color: var(--color-text-secondary); text-decoration: none; }
.parking-grid { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: var(--space-3); }
.parking-slot { min-height: 68px; display: grid; place-items: center; border-radius: var(--radius-md); border: 1px solid var(--color-border); background: var(--color-gray-50); }
.parking-slot.available { background: var(--color-secondary-50); color: var(--color-secondary-dark); }
.parking-slot.occupied { background: var(--color-danger-50); color: var(--color-danger-dark); }
.parking-slot.reserved { background: var(--color-accent-50); color: var(--color-accent-dark); }
.table-wrap { overflow-x: auto; }
.form-card { display: grid; gap: var(--space-4); }
@media (max-width: 960px) { .stat-grid, .content-grid.two-col, .parking-grid { grid-template-columns: 1fr; } }
</style>