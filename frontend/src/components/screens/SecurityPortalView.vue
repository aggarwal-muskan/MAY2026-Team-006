<template>
  <div class="portal-screen security-screen">
    <template v-if="page === 'dashboard'">
      <div class="dashboard-shell">
      <div class="screen-header"><h1>Security Dashboard</h1><p>Monitor visitor flow, patrol activity, and incident response.</p></div>
      <div class="stat-grid"><div v-for="stat in securityStats" :key="stat.label" class="card stat-card"><div class="stat-label">{{ stat.label }}</div><div class="stat-value">{{ stat.value }}</div></div></div>
      <div class="content-grid two-col"><section class="card"><h3 class="card-title">Recent Entries</h3><div v-for="entry in filteredVisitorLogs.slice(0, 4)" :key="entry.id" class="list-row"><div><strong>{{ entry.name }}</strong><p>{{ entry.purpose }} · {{ entry.flat }}</p></div><span class="badge" :class="badgeClass(entry.status)">{{ entry.status }}</span></div></section><section class="card"><h3 class="card-title">Quick Actions</h3><div class="chip-row"><router-link to="/security/visitor-entry" class="chip-link">Visitor Entry</router-link><router-link to="/security/vehicles" class="chip-link">Vehicle Logs</router-link></div></section></div>
      </div>
    </template>

    <template v-else-if="page === 'visitor-entry'">
      <div class="screen-header"><h1>Visitor Entry</h1><p>Log visitors and approve access.</p></div>
      <div class="content-grid two-col"><form class="card form-card" @submit.prevent="notify.success('Visitor entry saved')"><label class="form-group"><span class="form-label">Name</span><input type="text" /></label><label class="form-group"><span class="form-label">Purpose</span><input type="text" /></label><label class="form-group"><span class="form-label">Flat Visiting</span><input type="text" /></label><label class="form-group"><span class="form-label">Entry Time</span><input type="text" /></label><button class="btn btn-primary">Save Entry</button></form><section class="card table-wrap"><h3 class="card-title">Recent Visitor Log</h3><table class="data-table"><thead><tr><th>Name</th><th>Purpose</th><th>Status</th></tr></thead><tbody><tr v-for="entry in filteredVisitorLogs" :key="entry.id"><td>{{ entry.name }}</td><td>{{ entry.purpose }}</td><td><span class="badge" :class="badgeClass(entry.status)">{{ entry.status }}</span></td></tr></tbody></table></section></div>
    </template>

    <template v-else-if="page === 'vehicle-logs'">
      <div class="screen-header"><h1>Vehicle Logs</h1><p>Search entry and exit records by vehicle number.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Vehicle No</th><th>Type</th><th>Flat</th><th>Entry</th><th>Status</th></tr></thead><tbody><tr v-for="vehicle in filteredVehicleLogs" :key="vehicle.id"><td>{{ vehicle.vehicleNo }}</td><td>{{ vehicle.type }}</td><td>{{ vehicle.flat }}</td><td>{{ vehicle.entry }}</td><td><span class="badge" :class="badgeClass(vehicle.status)">{{ vehicle.status }}</span></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'patrol-log'">
      <div class="screen-header"><h1>Patrol Log</h1><p>Checkpoint and patrol notes for the current shift.</p></div>
      <div class="stack"><article v-for="entry in filteredPatrolItems" :key="entry.title" class="card patrol-row"><strong>{{ entry.title }}</strong><p>{{ entry.time }} · {{ entry.note }}</p></article></div>
    </template>

    <template v-else-if="page === 'visitor-approval'">
      <div class="screen-header"><h1>Visitor Approval</h1><p>Pending visitor approvals and gate clearance.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Visitor</th><th>Flat</th><th>Purpose</th><th>Action</th></tr></thead><tbody><tr v-for="entry in filteredVisitorLogs.slice(0, 3)" :key="entry.id"><td>{{ entry.name }}</td><td>{{ entry.flat }}</td><td>{{ entry.purpose }}</td><td><button class="btn btn-secondary btn-sm">Approve</button></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'emergency-alerts'">
      <div class="screen-header"><h1>Emergency Alerts</h1><p>Critical society notifications and incidents.</p></div>
      <div class="stack"><article v-for="alert in filteredEmergencyAlerts" :key="alert.id" class="card alert-row"><strong>{{ alert.title }}</strong><p>{{ alert.description }}</p><span class="badge" :class="badgeClass(alert.priority)">{{ alert.priority }}</span></article></div>
    </template>

    <template v-else-if="page === 'incident-reports'">
      <div class="screen-header"><h1>Incident Reports</h1><p>Documented incidents for follow-up and investigation.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Type</th><th>Location</th><th>Severity</th><th>Status</th></tr></thead><tbody><tr v-for="incident in filteredIncidentReports" :key="incident.id"><td>{{ incident.type }}</td><td>{{ incident.location }}</td><td>{{ incident.severity }}</td><td><span class="badge" :class="badgeClass(incident.status)">{{ incident.status }}</span></td></tr></tbody></table></div>
    </template>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useNotificationStore } from '@/stores/notificationStore'
import { emergencyAlerts, incidentReports, vehicleLogs, visitorLogs } from '@/data/mockData'
import { badgeClass } from './screenUtils'

const route = useRoute()
const notify = useNotificationStore()
const page = computed(() => route.meta.page || 'dashboard')
const globalSearchQuery = computed(() => String(route.query.q || '').trim().toLowerCase())

function matchesSearch(values, query) {
  if (!query) return true
  return values
    .map((value) => String(value || '').toLowerCase())
    .some((value) => value.includes(query))
}

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

const filteredVisitorLogs = computed(() => {
  const query = globalSearchQuery.value
  if (!query) return visitorLogs
  return visitorLogs.filter((entry) => matchesSearch([
    entry?.name,
    entry?.purpose,
    entry?.flat,
    entry?.status,
  ], query))
})

const filteredVehicleLogs = computed(() => {
  const query = globalSearchQuery.value
  if (!query) return vehicleLogs
  return vehicleLogs.filter((vehicle) => matchesSearch([
    vehicle?.vehicleNo,
    vehicle?.type,
    vehicle?.flat,
    vehicle?.entry,
    vehicle?.status,
  ], query))
})

const filteredPatrolItems = computed(() => {
  const query = globalSearchQuery.value
  if (!query) return patrolItems
  return patrolItems.filter((item) => matchesSearch([
    item?.title,
    item?.time,
    item?.note,
  ], query))
})

const filteredEmergencyAlerts = computed(() => {
  const query = globalSearchQuery.value
  if (!query) return emergencyAlerts
  return emergencyAlerts.filter((alert) => matchesSearch([
    alert?.title,
    alert?.description,
    alert?.priority,
  ], query))
})

const filteredIncidentReports = computed(() => {
  const query = globalSearchQuery.value
  if (!query) return incidentReports
  return incidentReports.filter((incident) => matchesSearch([
    incident?.type,
    incident?.location,
    incident?.severity,
    incident?.status,
  ], query))
})
</script>

<style scoped>
.portal-screen { display: grid; gap: var(--space-6); }
.screen-header { display: grid; gap: var(--space-2); }
.screen-header h1 { margin: 0; }
.screen-header p { color: var(--color-text-secondary); }
.stat-grid, .content-grid { display: grid; gap: var(--space-5); }
.stat-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.stat-card .stat-value { font-size: var(--text-3xl); font-weight: var(--font-bold); margin-top: var(--space-2); }
.content-grid.two-col { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.list-row, .patrol-row, .alert-row { padding: var(--space-4) var(--space-5); border-bottom: 1px solid var(--color-border); display: flex; justify-content: space-between; gap: var(--space-4); }
.list-row:last-child, .patrol-row:last-child, .alert-row:last-child { border-bottom: none; }
.chip-row { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.chip-link { padding: 6px 12px; border-radius: var(--radius-full); background: var(--color-gray-100); color: var(--color-text-secondary); text-decoration: none; }
.table-wrap { overflow-x: auto; }
.form-card { display: grid; gap: var(--space-5); }
@media (max-width: 960px) { .stat-grid, .content-grid.two-col { grid-template-columns: 1fr; } }

.dashboard-shell {
  display: grid;
  gap: var(--space-6);
}

.dashboard-shell .screen-header {
  padding: var(--space-6);
  border: 1px solid rgba(37, 99, 235, 0.08);
  border-radius: var(--radius-2xl);
  background:
    radial-gradient(circle at top right, rgba(239, 68, 68, 0.12), transparent 28%),
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

.dashboard-shell .list-row,
.dashboard-shell .patrol-row,
.dashboard-shell .alert-row {
  padding-block: var(--space-4);
}

.dashboard-shell .chip-link {
  background: rgba(37, 99, 235, 0.08);
  color: var(--color-primary);
}

.dashboard-shell .table-wrap {
  border: 1px solid rgba(229, 231, 235, 0.9);
  box-shadow: var(--shadow-sm);
}
</style>