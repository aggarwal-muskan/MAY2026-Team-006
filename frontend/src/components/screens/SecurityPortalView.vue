<template>
  <div class="portal-screen security-screen">
    <template v-if="page === 'dashboard'">
      <div class="dashboard-shell">
      <div class="screen-header"><h1>Security Dashboard</h1><p>Monitor visitor flow, patrol activity, and incident response.</p></div>
      <div v-if="securityError" class="card error-state">{{ securityError }}</div>
      <div class="stat-grid"><div v-for="stat in securityStats" :key="stat.label" class="card stat-card"><div class="stat-label">{{ stat.label }}</div><div class="stat-value">{{ stat.value }}</div></div></div>
      <div class="content-grid two-col"><section class="card"><h3 class="card-title">Recent Entries</h3><div v-if="isLoading && !filteredVisitorLogs.length" class="list-row">Loading entries...</div><div v-else-if="!filteredVisitorLogs.length" class="list-row">No visitor entries yet.</div><div v-for="entry in filteredVisitorLogs.slice(0, 4)" :key="entry.id" class="list-row"><div><strong>{{ entry.name }}</strong><p>{{ entry.purpose || '-' }} · {{ entry.flat || '-' }}</p></div><span class="badge" :class="badgeClass(entry.status)">{{ entry.status }}</span></div></section><section class="card"><h3 class="card-title">Quick Actions</h3><div class="chip-row"><router-link to="/security/visitor-entry" class="chip-link">Visitor Entry</router-link><router-link to="/security/vehicles" class="chip-link">Vehicle Logs</router-link><router-link to="/security/visitor-approval" class="chip-link">Approvals</router-link></div></section></div>
      </div>
    </template>

    <template v-else-if="page === 'visitor-entry'">
      <div class="screen-header"><h1>Visitor Entry</h1><p>Log visitors and approve access.</p></div>
      <div class="content-grid two-col"><form class="card form-card" @submit.prevent="saveVisitorEntry"><label class="form-group"><span class="form-label">Name</span><input v-model="visitorForm.visitor_name" type="text" /></label><label class="form-group"><span class="form-label">Purpose</span><input v-model="visitorForm.purpose" type="text" /></label><label class="form-group"><span class="form-label">Flat Visiting</span><input v-model="visitorForm.flat_number" type="text" /></label><label class="form-group"><span class="form-label">Contact Number</span><input v-model="visitorForm.contact_number" type="text" /></label><label class="form-group"><span class="form-label">Vehicle Number</span><input v-model="visitorForm.vehicle_number" type="text" /></label><label class="form-group"><span class="form-label">Vehicle Type</span><input v-model="visitorForm.vehicle_type" type="text" /></label><label class="form-group"><span class="form-label">Remarks</span><textarea v-model="visitorForm.remarks" rows="3"></textarea></label><button class="btn btn-primary" :disabled="isSavingVisitor">{{ isSavingVisitor ? 'Saving...' : 'Save Entry' }}</button></form><section class="card table-wrap"><h3 class="card-title">Recent Visitor Log</h3><table class="data-table"><thead><tr><th>Name</th><th>Purpose</th><th>Status</th></tr></thead><tbody><tr v-if="!filteredVisitorLogs.length"><td colspan="3">No visitor entries found</td></tr><tr v-for="entry in filteredVisitorLogs" :key="entry.id"><td>{{ entry.name }}</td><td>{{ entry.purpose || '-' }}</td><td><span class="badge" :class="badgeClass(entry.status)">{{ entry.status }}</span></td></tr></tbody></table></section></div>
    </template>

    <template v-else-if="page === 'vehicle-logs'">
      <div class="screen-header"><h1>Vehicle Logs</h1><p>Search entry and exit records by vehicle number.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Vehicle No</th><th>Type</th><th>Flat</th><th>Entry</th><th>Status</th></tr></thead><tbody><tr v-if="!filteredVehicleLogs.length"><td colspan="5">No vehicle records found</td></tr><tr v-for="vehicle in filteredVehicleLogs" :key="vehicle.id"><td>{{ vehicle.vehicleNo }}</td><td>{{ vehicle.type || '-' }}</td><td>{{ vehicle.flat || '-' }}</td><td>{{ vehicle.entry }}</td><td><span class="badge" :class="badgeClass(vehicle.status)">{{ vehicle.status }}</span></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'patrol-log'">
      <div class="screen-header"><h1>Patrol Log</h1><p>Checkpoint and patrol notes for the current shift.</p></div>
      <form class="card form-card" @submit.prevent="savePatrolLog"><label class="form-group"><span class="form-label">Checkpoint</span><input v-model="patrolForm.checkpoint" type="text" /></label><label class="form-group"><span class="form-label">Note</span><textarea v-model="patrolForm.note" rows="3"></textarea></label><button class="btn btn-primary">Add Patrol Log</button></form><div class="stack"><article v-for="entry in filteredPatrolItems" :key="entry.id || entry.title" class="card patrol-row"><strong>{{ entry.title }}</strong><p>{{ entry.time }} · {{ entry.note }}</p></article><article v-if="!filteredPatrolItems.length" class="card patrol-row">No patrol logs recorded.</article></div>
    </template>

    <template v-else-if="page === 'visitor-approval'">
      <div class="screen-header"><h1>Visitor Approval</h1><p>Pending visitor approvals and gate clearance.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Visitor</th><th>Flat</th><th>Purpose</th><th>Action</th></tr></thead><tbody><tr v-if="!pendingVisitorApprovals.length"><td colspan="4">No pending approvals.</td></tr><tr v-for="entry in pendingVisitorApprovals" :key="entry.id"><td>{{ entry.name }}</td><td>{{ entry.flat || '-' }}</td><td>{{ entry.purpose || '-' }}</td><td><div class="row-actions"><button class="btn btn-secondary btn-sm" @click="approveEntry(entry.id)">Approve</button><button class="btn btn-outline btn-sm" @click="rejectEntry(entry.id)">Reject</button></div></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'emergency-alerts'">
      <div class="screen-header"><h1>Emergency Alerts</h1><p>Critical society notifications and incidents.</p></div>
      <form class="card form-card" @submit.prevent="saveEmergencyAlert"><label class="form-group"><span class="form-label">Title</span><input v-model="alertForm.title" type="text" /></label><label class="form-group"><span class="form-label">Priority</span><select v-model="alertForm.priority"><option value="low">Low</option><option value="medium">Medium</option><option value="high">High</option><option value="critical">Critical</option></select></label><label class="form-group"><span class="form-label">Description</span><textarea v-model="alertForm.description" rows="3"></textarea></label><button class="btn btn-primary">Create Alert</button></form><div class="stack"><article v-for="alert in filteredEmergencyAlerts" :key="alert.id" class="card alert-row"><strong>{{ alert.title }}</strong><p>{{ alert.description }}</p><span class="badge" :class="badgeClass(alert.priority)">{{ alert.priority }}</span></article><article v-if="!filteredEmergencyAlerts.length" class="card alert-row">No alerts available.</article></div>
    </template>

    <template v-else-if="page === 'incident-reports'">
      <div class="screen-header"><h1>Incident Reports</h1><p>Documented incidents for follow-up and investigation.</p></div>
      <form class="card form-card" @submit.prevent="saveIncidentReport"><label class="form-group"><span class="form-label">Type</span><input v-model="incidentForm.incident_type" type="text" /></label><label class="form-group"><span class="form-label">Location</span><input v-model="incidentForm.location" type="text" /></label><label class="form-group"><span class="form-label">Severity</span><select v-model="incidentForm.severity"><option value="low">Low</option><option value="medium">Medium</option><option value="high">High</option></select></label><label class="form-group"><span class="form-label">Description</span><textarea v-model="incidentForm.description" rows="3"></textarea></label><button class="btn btn-primary">Create Incident</button></form><div class="card table-wrap"><table class="data-table"><thead><tr><th>Type</th><th>Location</th><th>Severity</th><th>Status</th></tr></thead><tbody><tr v-if="!filteredIncidentReports.length"><td colspan="4">No incident reports found</td></tr><tr v-for="incident in filteredIncidentReports" :key="incident.id"><td>{{ incident.type }}</td><td>{{ incident.location }}</td><td>{{ incident.severity }}</td><td><span class="badge" :class="badgeClass(incident.status)">{{ incident.status }}</span></td></tr></tbody></table></div>
    </template>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'
import { useNotificationStore } from '@/stores/notificationStore'
import { badgeClass } from './screenUtils'

const route = useRoute()
const authStore = useAuthStore()
const notify = useNotificationStore()
const page = computed(() => route.meta.page || 'dashboard')
const globalSearchQuery = computed(() => String(route.query.q || '').trim().toLowerCase())
const isLoading = ref(false)
const isSavingVisitor = ref(false)
const securityError = ref('')
const dashboardData = ref({ stats: {}, recent_entries: [] })
const visitorEntries = ref([])
const patrolLogs = ref([])
const emergencyAlerts = ref([])
const incidentReports = ref([])
const visitorForm = reactive({ visitor_name: '', purpose: '', flat_number: '', contact_number: '', vehicle_number: '', vehicle_type: '', remarks: '' })
const patrolForm = reactive({ checkpoint: '', note: '' })
const alertForm = reactive({ title: '', priority: 'medium', description: '' })
const incidentForm = reactive({ incident_type: '', location: '', severity: 'medium', description: '' })

function matchesSearch(values, query) {
  if (!query) return true
  return values
    .map((value) => String(value || '').toLowerCase())
    .some((value) => value.includes(query))
}

const securityStats = computed(() => ([
  { label: 'Visitors Today', value: dashboardData.value?.stats?.visitors_today ?? 0 },
  { label: 'Currently Inside', value: dashboardData.value?.stats?.currently_inside ?? 0 },
  { label: 'Pending Approvals', value: dashboardData.value?.stats?.pending_approvals ?? 0 },
]))

function normalizeVisitor(entry) {
  return {
    id: entry.id,
    name: entry.visitor_name,
    purpose: entry.purpose,
    flat: entry.flat_number,
    status: entry.exit_time ? 'Exited' : (entry.approval_status === 'pending' ? 'Pending' : 'Inside'),
    entryTime: entry.entry_time,
    vehicleNo: entry.vehicle_number,
    vehicleType: entry.vehicle_type,
    approvalStatus: entry.approval_status,
  }
}

const filteredVisitorLogs = computed(() => {
  const query = globalSearchQuery.value
  const list = visitorEntries.value.map(normalizeVisitor)
  if (!query) return list
  return list.filter((entry) => matchesSearch([
    entry?.name,
    entry?.purpose,
    entry?.flat,
    entry?.status,
  ], query))
})

const pendingVisitorApprovals = computed(() => filteredVisitorLogs.value.filter((entry) => entry.approvalStatus === 'pending'))

const filteredVehicleLogs = computed(() => {
  const query = globalSearchQuery.value
  const vehicles = visitorEntries.value
    .filter((entry) => entry.vehicle_number)
    .map((entry) => ({
      id: entry.id,
      vehicleNo: entry.vehicle_number,
      type: entry.vehicle_type,
      flat: entry.flat_number,
      entry: entry.entry_time,
      status: entry.exit_time ? 'Exited' : 'Inside',
    }))
  if (!query) return vehicles
  return vehicles.filter((vehicle) => matchesSearch([
    vehicle?.vehicleNo,
    vehicle?.type,
    vehicle?.flat,
    vehicle?.entry,
    vehicle?.status,
  ], query))
})

const filteredPatrolItems = computed(() => {
  const query = globalSearchQuery.value
  const list = patrolLogs.value.map((item) => ({ id: item.id, title: item.checkpoint, time: item.patrol_time, note: item.note }))
  if (!query) return list
  return list.filter((item) => matchesSearch([
    item?.title,
    item?.time,
    item?.note,
  ], query))
})

const filteredEmergencyAlerts = computed(() => {
  const query = globalSearchQuery.value
  const list = emergencyAlerts.value.map((alert) => ({ ...alert, priority: alert.priority, title: alert.title, description: alert.description }))
  if (!query) return list
  return list.filter((alert) => matchesSearch([
    alert?.title,
    alert?.description,
    alert?.priority,
  ], query))
})

const filteredIncidentReports = computed(() => {
  const query = globalSearchQuery.value
  const list = incidentReports.value.map((incident) => ({ id: incident.id, type: incident.incident_type, location: incident.location, severity: incident.severity, status: incident.status }))
  if (!query) return list
  return list.filter((incident) => matchesSearch([
    incident?.type,
    incident?.location,
    incident?.severity,
    incident?.status,
  ], query))
})

async function loadSecurityData() {
  try {
    isLoading.value = true
    securityError.value = ''
    const [dashboard, visitors, patrol, alerts, incidents] = await Promise.all([
      authStore.getSecurityDashboardStats(),
      authStore.listVisitors({ withMeta: true }),
      authStore.listPatrolLogs({ withMeta: true }),
      authStore.listEmergencyAlerts({ withMeta: true }),
      authStore.listIncidentReports({ withMeta: true }),
    ])
    dashboardData.value = dashboard || { stats: {}, recent_entries: [] }
    visitorEntries.value = visitors.items || []
    patrolLogs.value = patrol.items || []
    emergencyAlerts.value = alerts.items || []
    incidentReports.value = incidents.items || []
  } catch (error) {
    securityError.value = error instanceof Error ? error.message : 'Unable to load security data'
  } finally {
    isLoading.value = false
  }
}

async function saveVisitorEntry() {
  try {
    isSavingVisitor.value = true
    await authStore.createVisitor({
      visitor_name: String(visitorForm.visitor_name || '').trim(),
      purpose: String(visitorForm.purpose || '').trim(),
      flat_number: String(visitorForm.flat_number || '').trim(),
      contact_number: String(visitorForm.contact_number || '').trim(),
      vehicle_number: String(visitorForm.vehicle_number || '').trim(),
      vehicle_type: String(visitorForm.vehicle_type || '').trim(),
      remarks: String(visitorForm.remarks || '').trim(),
    })
    Object.assign(visitorForm, { visitor_name: '', purpose: '', flat_number: '', contact_number: '', vehicle_number: '', vehicle_type: '', remarks: '' })
    await loadSecurityData()
    notify.success('Visitor entry saved')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to save visitor entry')
  } finally {
    isSavingVisitor.value = false
  }
}

async function approveEntry(entryId) {
  try {
    await authStore.approveVisitor(entryId)
    await loadSecurityData()
    notify.success('Visitor approved')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to approve visitor')
  }
}

async function rejectEntry(entryId) {
  try {
    await authStore.rejectVisitor(entryId)
    await loadSecurityData()
    notify.success('Visitor rejected')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to reject visitor')
  }
}

async function savePatrolLog() {
  try {
    await authStore.createPatrolLog({ checkpoint: patrolForm.checkpoint, note: patrolForm.note })
    patrolForm.checkpoint = ''
    patrolForm.note = ''
    await loadSecurityData()
    notify.success('Patrol log added')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to add patrol log')
  }
}

async function saveEmergencyAlert() {
  try {
    await authStore.createEmergencyAlert({ title: alertForm.title, priority: alertForm.priority, description: alertForm.description })
    alertForm.title = ''
    alertForm.priority = 'medium'
    alertForm.description = ''
    await loadSecurityData()
    notify.success('Emergency alert created')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to create emergency alert')
  }
}

async function saveIncidentReport() {
  try {
    await authStore.createIncidentReport({ incident_type: incidentForm.incident_type, location: incidentForm.location, severity: incidentForm.severity, description: incidentForm.description })
    incidentForm.incident_type = ''
    incidentForm.location = ''
    incidentForm.severity = 'medium'
    incidentForm.description = ''
    await loadSecurityData()
    notify.success('Incident report created')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to create incident report')
  }
}

onMounted(loadSecurityData)

watch(() => route.query.q, loadSecurityData)
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