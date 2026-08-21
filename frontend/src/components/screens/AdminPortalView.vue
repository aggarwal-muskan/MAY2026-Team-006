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
        <button class="btn btn-primary" @click="showResidentForm = !showResidentForm">{{ showResidentForm ? 'Cancel' : 'Add Resident' }}</button>
      </div>
      <form v-if="showResidentForm" class="card form-card" @submit.prevent="submitResident">
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Full Name</span><input v-model="residentForm.full_name" type="text" /></label><label class="form-group"><span class="form-label">Email</span><input v-model="residentForm.email" type="email" /></label></div>
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Phone</span><input v-model="residentForm.phone" type="text" /></label><label class="form-group"><span class="form-label">Password</span><input v-model="residentForm.password" type="password" /></label></div>
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Flat Number</span><input v-model="residentForm.flat_number" type="text" placeholder="A-101" /></label></div>
        <button class="btn btn-primary">Create Resident</button>
      </form>
      <div class="card toolbar"><input v-model="userSearchQuery" type="text" placeholder="Search users (name, email, phone, role)" /></div>
      <div class="card table-wrap">
        <table class="data-table">
          <thead><tr><th>Name</th><th>Flat No</th><th>Phone</th><th>Email</th><th>Status</th></tr></thead>
          <tbody><tr v-for="resident in residentRows" :key="resident.id"><td>{{ resident.name }}</td><td>{{ resident.flat }}</td><td>{{ resident.phone }}</td><td>{{ resident.email }}</td><td><span class="badge" :class="badgeClass(resident.status)">{{ resident.status }}</span></td></tr><tr v-if="!residentRows.length"><td colspan="5">No residents match your search.</td></tr></tbody>
        </table>
      </div>
    </template>

    <template v-else-if="page === 'tenants'">
      <div class="screen-header row-between">
        <div><h1>Tenants</h1><p>Track tenant leases and contact details.</p></div>
        <button class="btn btn-primary" @click="openTenantForm()">{{ showTenantForm ? 'Cancel' : 'Add Tenant' }}</button>
      </div>
      <form v-if="showTenantForm" class="card form-card" @submit.prevent="submitTenant">
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Full Name</span><input v-model="tenantForm.full_name" type="text" /></label><label class="form-group"><span class="form-label">Email</span><input v-model="tenantForm.email" type="email" /></label></div>
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Phone</span><input v-model="tenantForm.phone" type="text" /></label><label class="form-group"><span class="form-label">Flat Number</span><input v-model="tenantForm.flat_number" type="text" placeholder="B-204" /></label></div>
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Lease Start</span><input v-model="tenantForm.leaseStart" type="date" /></label><label class="form-group"><span class="form-label">Lease End</span><input v-model="tenantForm.leaseEnd" type="date" /></label></div>
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Status</span><select v-model="tenantForm.status"><option value="active">Active</option><option value="inactive">Inactive</option></select></label><label class="form-group"><span class="form-label">Password {{ editingTenantId ? '(leave blank to keep unchanged)' : '' }}</span><input v-model="tenantForm.password" type="password" /></label></div>
        <button class="btn btn-primary">{{ editingTenantId ? 'Update Tenant' : 'Create Tenant' }}</button>
      </form>
      <div class="card toolbar"><input v-model="tenantSearchQuery" type="text" placeholder="Search tenant by name, email, phone, flat, owner, status" /></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Name</th><th>Email</th><th>Phone</th><th>Flat No</th><th>Owner</th><th>Lease Start</th><th>Lease End</th><th>Status</th><th>Actions</th></tr></thead><tbody><tr v-for="tenant in tenantRows" :key="tenant.id"><td>{{ tenant.name }}</td><td>{{ tenant.email || '-' }}</td><td>{{ tenant.phone || '-' }}</td><td>{{ tenant.flat }}</td><td>{{ tenant.owner }}</td><td>{{ tenant.leaseStart || '-' }}</td><td>{{ tenant.leaseEnd || '-' }}</td><td><span class="badge" :class="badgeClass(tenant.status)">{{ tenant.status }}</span></td><td><button class="btn btn-outline btn-sm" @click="openTenantForm(tenant)">Edit</button></td></tr><tr v-if="!tenantRows.length"><td colspan="9">No tenants found</td></tr></tbody></table></div>
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
      <div class="screen-header row-between">
        <div>
          <h1>Complaints Management</h1>
          <p>Assign, classify, and track complaint resolution powered by AI priority assessment.</p>
        </div>
        <div class="row-actions">
          <button
            class="btn btn-primary"
            type="button"
            :disabled="isAiBusy('complaint-classify-all') || !complaintRows.length"
            @click="runAiClassifyAllComplaints"
          >
            {{ isAiBusy('complaint-classify-all') ? 'Classifying All…' : '🤖 AI Classify & Sort Priority' }}
          </button>
        </div>
      </div>

      <div class="card toolbar"><input v-model="userSearchQuery" type="text" placeholder="Search assign users (name, email, phone, role)" /></div>

      <div class="emerging-issues-wrapper">
        <div v-if="!emergingIssuesLoaded && !isLoadingEmergingIssues" class="card emerging-issues-trigger">
          <div>
            <h3 class="card-title">Emerging Issues</h3>
            <p>Let AI review current complaints and group recurring issues into cards.</p>
          </div>
          <button class="btn btn-primary" type="button" @click="loadEmergingIssues">
            🤖 Load Emerging Issues with AI
          </button>
        </div>

        <div v-else-if="isLoadingEmergingIssues" class="card emerging-issues-loading">
          <div class="thinking-dots"><span></span><span></span><span></span></div>
          <p>Thinking… please wait around 30s while AI reviews and clusters complaints.</p>
        </div>

        <div v-else-if="emergingIssues.length > 0" class="emerging-issues">
          <div class="emerging-issues-header">
            <h3 class="card-title">Emerging Issues</h3>
            <button class="btn btn-outline btn-sm" type="button" @click="loadEmergingIssues">Refresh</button>
          </div>
          <div class="card-grid issue-grid">
            <button
              v-for="issue in emergingIssues"
              :key="issue.category + issue.title"
              class="card issue-card"
              type="button"
              @click="openCluster(issue)"
            >
              <div class="issue-icon">{{ categoryIcon(issue.category) }}</div>
              <div class="issue-category">{{ issue.category }}</div>
              <div class="issue-title">{{ issue.title }}</div>
              <div class="issue-count">Review similar complaints</div>
            </button>
          </div>
        </div>

        <div v-else class="card emerging-issues-empty">
          <p>No emerging issues detected right now.</p>
          <button class="btn btn-outline btn-sm" type="button" @click="loadEmergingIssues">Re-check</button>
        </div>
      </div>

      <div v-if="activeCluster" class="modal-overlay" @click.self="closeClusterModal">
        <div class="modal-panel">
          <div class="modal-header">
            <div>
              <h3>{{ categoryIcon(activeCluster.category) }} {{ activeCluster.category }} — {{ activeCluster.title }}</h3>
              <p>{{ activeCluster.count }} complaints in this cluster</p>
            </div>
            <button class="btn btn-outline btn-sm" @click="closeClusterModal">Close</button>
          </div>
          <div class="modal-body">
            <div v-for="complaint in clusterComplaints" :key="complaint.id" class="cluster-row">
              <div class="cluster-row-main">
                <strong>#{{ complaint.id }} — {{ complaint.subject }}</strong>
                <p>{{ complaint.description }}</p>
                <span class="badge" :class="badgeClass(complaint.status)">{{ complaint.status }}</span>
              </div>
              <div class="cluster-row-actions">
                <div class="row-actions" v-if="canAssignComplaint(complaint)">
                  <select v-model="complaintAssignments[complaint.id]">
                    <option disabled value="">Select provider</option>
                    <option v-for="person in assignableUsers" :key="person.id" :value="person.id">{{ person.name }}</option>
                  </select>
                  <button class="btn btn-secondary btn-sm" @click="assignComplaintToUser(complaint)">{{ complaint.assigned_to_user_id ? 'Reassign' : 'Assign' }}</button>
                </div>
                <span v-else class="chip">Closed</span>
              </div>
            </div>
            <div v-if="clusterComplaints.length === 0" class="list-row">These complaints have since moved out of this cluster's list.</div>
          </div>
        </div>
      </div>

      <div class="card toolbar complaints-filter-toolbar">
        <div class="filter-controls-group">
          <label class="filter-label">
            <span class="filter-label-text">Filter Priority:</span>
            <select v-model="selectedPriorityFilter" class="form-select-sm">
              <option value="All">All Priorities</option>
              <option value="High">High / Urgent</option>
              <option value="Medium">Medium</option>
              <option value="Low">Low</option>
            </select>
          </label>
          <label class="filter-label">
            <span class="filter-label-text">Sort By:</span>
            <select v-model="selectedSortOrder" class="form-select-sm">
              <option value="priority-desc">AI Priority (High → Low)</option>
              <option value="id-desc">Latest First</option>
              <option value="status">Status</option>
            </select>
          </label>
        </div>
        <span class="badge badge-info">{{ sortedComplaints.length }} Complaints</span>
      </div>

      <div class="card table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Title / Description</th>
              <th>Category</th>
              <th>Resident</th>
              <th>AI Priority</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="complaint in sortedComplaints" :key="complaint.id">
              <td>#{{ complaint.id }}</td>
              <td>
                <strong>{{ complaint.subject || complaint.title }}</strong>
                <p v-if="complaint.description" style="font-size: 0.825rem; color: #666; margin: 2px 0 0 0;">{{ complaint.description }}</p>
              </td>
              <td><span class="badge badge-outline">{{ complaint.category || 'General' }}</span></td>
              <td>{{ getResidentName(complaint.raised_by_user_id || complaint.resident) }}</td>
              <td>
                <span class="badge" :class="priorityBadgeClass(complaint.priority)">
                  {{ complaint.priority || 'Medium' }}
                </span>
              </td>
              <td><span class="badge" :class="badgeClass(complaint.status)">{{ complaint.status }}</span></td>
              <td>
                <div class="row-actions" style="display: flex; gap: var(--space-2); align-items: center;">
                  <template v-if="canAssignComplaint(complaint)">
                    <select v-model="complaintAssignments[complaint.id]">
                      <option disabled value="">Select provider</option>
                      <option v-for="person in assignableUsers" :key="person.id" :value="person.id">{{ person.name }}</option>
                    </select>
                    <button class="btn btn-secondary btn-sm" @click="assignComplaintToUser(complaint)">{{ complaint.assigned_to_user_id ? 'Reassign' : 'Assign' }}</button>
                  </template>
                  <span v-else class="chip">Closed</span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </template>

    <template v-else-if="page === 'notices'">
      <div class="screen-header row-between">
        <div><h1>Notice Management</h1><p>Publish, edit, or remove notices.</p></div>
        <div class="row-actions">
          <button
            class="btn btn-secondary"
            type="button"
            :disabled="isAiBusy('notices-summarize-all') || !noticeRows.length"
            @click.stop="summarizeAllNotices"
          >
            {{ isAiBusy('notices-summarize-all') ? 'Summarizing…' : 'AI Summarize All' }}
          </button>
          <router-link to="/admin/notices/create" class="btn btn-primary">Create Notice</router-link>
        </div>
      </div>
      <div v-if="allNoticesSummary" class="card ai-summary-card">
        <h3 class="card-title">{{ allNoticesSummary.headline || 'Notices summary' }}</h3>
        <pre class="ai-output">{{ formatAllNoticesSummary(allNoticesSummary) }}</pre>
      </div>
      <div class="stack">
        <article v-for="notice in noticeRows" :key="`notice-${notice.id}`" class="card notice-row">
          <div>
            <strong>{{ notice.title }}</strong>
            <p class="notice-body-formatted">{{ formatNoticeBodyText(notice.body || notice.content) }}</p>
          </div>
          <div class="row-actions">
            <button class="btn btn-danger btn-sm" type="button" @click.stop="removeNotice(notice.id)">Delete</button>
          </div>
        </article>
      </div>
    </template>

    <template v-else-if="page === 'create-notice'">
      <div class="screen-header"><h1>Create Notice</h1><p>Write and publish a new society notice. Use AI to draft or translate.</p></div>
      <form class="card form-card" @submit.prevent="submitNotice">
        <div class="form-grid two-col">
          <label class="form-group"><span class="form-label">AI Topic</span><input v-model="aiNoticeDraft.topic" type="text" placeholder="Water Tank Cleaning" /></label>
          <label class="form-group"><span class="form-label">Date</span><input v-model="aiNoticeDraft.date" type="text" placeholder="Sunday" /></label>
        </div>
        <div class="form-grid two-col">
          <label class="form-group"><span class="form-label">Time</span><input v-model="aiNoticeDraft.time" type="text" placeholder="9:00 AM – 1:00 PM" /></label>
          <label class="form-group"><span class="form-label">Extra info</span><input v-model="aiNoticeDraft.extra" type="text" placeholder="Water supply may be affected" /></label>
        </div>
        <div class="row-actions">
          <button type="button" class="btn btn-secondary" :disabled="isAiBusy('notice-generate')" @click="generateNoticeWithAI">{{ isAiBusy('notice-generate') ? 'Generating…' : 'Generate with AI' }}</button>
          <button type="button" class="btn btn-outline" :disabled="isAiBusy('notice-translate') || !noticeForm.body" @click="translateNoticeWithAI">{{ isAiBusy('notice-translate') ? 'Translating…' : 'Translate (EN/HI/TE)' }}</button>
        </div>
        <label class="form-group"><span class="form-label">Title</span><input v-model="noticeForm.title" type="text" /></label>
        <label class="form-group"><span class="form-label">Category</span><select v-model="noticeForm.notice_type"><option value="maintenance">Maintenance</option><option value="event">Event</option><option value="rules">Rules</option><option value="security">Security</option></select></label>
        <label class="form-group"><span class="form-label">Priority</span><select v-model="noticeForm.priority"><option value="low">Low</option><option value="normal">Normal</option><option value="high">High</option><option value="urgent">Urgent</option></select></label>
        <label class="form-group"><span class="form-label">Content</span><textarea v-model="noticeForm.body" rows="8"></textarea></label>
        <div v-if="noticeTranslations" class="ai-panel">
          <h3 class="card-title">AI Translations (review before publishing)</h3>
          <div v-for="(text, lang) in noticeTranslations" :key="lang" class="translation-block">
            <strong>{{ lang }}</strong>
            <pre class="ai-output">{{ text }}</pre>
          </div>
        </div>
        <button class="btn btn-primary">Publish</button>
      </form>
    </template>

    <template v-else-if="page === 'events'">
      <div class="screen-header row-between"><div><h1>Events Management</h1><p>Monitor event listings and attendance.</p></div><router-link to="/admin/events/create" class="btn btn-primary">Create Event</router-link></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Event</th><th>Date</th><th>Venue</th><th>Status</th><th>Action</th></tr></thead><tbody><tr v-for="event in eventRows" :key="event.id"><td>{{ event.title }}</td><td>{{ event.event_date || event.date }}</td><td>{{ event.venue }}</td><td><span class="badge" :class="badgeClass(event.status || 'scheduled')">{{ event.status || 'scheduled' }}</span></td><td><button class="btn btn-danger btn-sm" @click="removeEvent(event.id)">Delete</button></td></tr></tbody></table></div>
    </template>

    <template v-else-if="page === 'create-event'">
      <div class="screen-header"><h1>Create Event</h1><p>Set up a new community activity. Use AI Event Planner for a structured draft.</p></div>
      <form class="card form-card" @submit.prevent="submitEvent">
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Event Name</span><input v-model="eventForm.title" type="text" /></label><label class="form-group"><span class="form-label">Date</span><input v-model="eventForm.event_date" type="date" /></label></div>
        <div class="form-grid two-col"><label class="form-group"><span class="form-label">Start Time</span><input v-model="eventForm.start_time" type="time" /></label><label class="form-group"><span class="form-label">Venue</span><input v-model="eventForm.venue" type="text" /></label></div>
        <div class="form-grid two-col">
          <label class="form-group"><span class="form-label">Expected residents</span><input v-model="eventPlanDraft.expected_residents" type="number" min="1" placeholder="200" /></label>
          <label class="form-group"><span class="form-label">Budget</span><input v-model="eventPlanDraft.budget" type="text" placeholder="₹50,000" /></label>
        </div>
        <label class="form-group"><span class="form-label">Duration / notes</span><input v-model="eventPlanDraft.duration" type="text" placeholder="4 hours · cultural + refreshments" /></label>
        <div class="row-actions"><button type="button" class="btn btn-secondary" :disabled="isAiBusy('event-plan')" @click="planEventWithAI">{{ isAiBusy('event-plan') ? 'Planning…' : 'Generate Event Plan with AI' }}</button></div>
        <label class="form-group"><span class="form-label">Description</span><textarea v-model="eventForm.description" rows="6"></textarea></label>
        <pre v-if="eventPlanResult" class="ai-output">{{ eventPlanResult.plan_markdown || JSON.stringify(eventPlanResult, null, 2) }}</pre>
        <button class="btn btn-primary">Create Event</button>
      </form>
    </template>



    <template v-else-if="page === 'settings'">
      <div class="screen-header"><h1>Admin Settings</h1><p>Basic administrative preferences.</p></div>
      <form class="card form-card" @submit.prevent="saveSettings"><label class="switch-row"><span>Maintenance reminders</span><input v-model="settingsForm.maintenance_reminders" type="checkbox" /></label><label class="switch-row"><span>Email alerts</span><input v-model="settingsForm.email_alerts" type="checkbox" /></label><label class="switch-row"><span>Auto approvals</span><input v-model="settingsForm.auto_approvals" type="checkbox" /></label><button class="btn btn-primary">Save Settings</button></form>
    </template>

    <template v-else-if="page === 'roles'">
      <div class="screen-header"><h1>Roles & Permissions</h1><p>Define access control by role.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Role</th><th>Scope</th><th>Access</th></tr></thead><tbody><tr v-for="role in roles" :key="role.name"><td>{{ role.name }}</td><td>{{ role.scope }}</td><td>{{ role.access }}</td></tr></tbody></table></div>
    </template>


    <template v-else-if="page === 'reports'">
      <div class="screen-header"><h1>Reports & Export</h1><p>Download operational summaries.</p></div>
      <div class="stat-grid admin-stats"><div class="card stat-card" v-for="item in reportSummaryCards" :key="item.label"><div class="stat-label">{{ item.label }}</div><div class="stat-value">{{ item.value }}</div></div></div>
      <div class="card report-card"><h3>Monthly Report Export</h3><p>Download current month operations snapshot in CSV format.</p><button class="btn btn-outline btn-sm" :disabled="isExporting" @click="exportMonthlyReport">{{ isExporting ? 'Exporting...' : 'Export CSV' }}</button></div>
    </template>

    <template v-else-if="page === 'logs'">
      <div class="screen-header"><h1>System Logs</h1><p>Audit trail of key admin actions.</p></div>
      <div class="card table-wrap"><table class="data-table"><thead><tr><th>Action</th><th>User</th><th>Timestamp</th><th>Details</th></tr></thead><tbody><tr v-for="log in systemLogRows" :key="log.id"><td>{{ log.action }}</td><td>{{ log.user }}</td><td>{{ log.timestamp }}</td><td>{{ log.details }}</td></tr><tr v-if="!systemLogRows.length"><td colspan="4">No system logs available</td></tr></tbody></table></div>
    </template>


  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'
import { useNotificationStore } from '@/stores/notificationStore'
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
const backendTenants = ref([])
const backendSystemLogs = ref([])
const backendMaintenanceBills = ref([])
const adminDashboardStats = ref({})
const complaintAssignments = ref({})
const bookingStatusBreakdown = ref({})
const complaintStatusBreakdown = ref({})
const emergingIssues = ref([])
const activeCluster = ref(null)
const isLoadingEmergingIssues = ref(false)
const emergingIssuesLoaded = ref(false)
const serviceCategories = ref([])
const monthlyReport = ref({})
const showResidentForm = ref(false)
const showProviderForm = ref(false)
const showTenantForm = ref(false)
const editingTenantId = ref(null)
const isExporting = ref(false)
const userSearchQuery = ref('')
const tenantSearchQuery = ref('')

const activeSearchQuery = computed(() => {
  const local = String(userSearchQuery.value || '').trim()
  if (local) return local
  return String(route.query.q || '').trim()
})

const selectedPriorityFilter = ref('All')
const selectedSortOrder = ref('priority-desc')

const noticeForm = reactive({ title: '', body: '', notice_type: 'maintenance', priority: 'normal' })
const eventForm = reactive({ title: '', description: '', event_date: '', start_time: '', venue: '' })
const residentForm = reactive({ full_name: '', email: '', phone: '', password: '', flat_number: '' })
const providerForm = reactive({ full_name: '', email: '', phone: '', password: '', category_id: '', business_name: '', service_description: '' })
const tenantForm = reactive({ full_name: '', email: '', phone: '', password: '', flat_number: '', leaseStart: '', leaseEnd: '', status: 'active' })
const aiBusyKey = ref(null)
const aiNoticeDraft = reactive({ topic: '', date: '', time: '', extra: '' })
const noticeTranslations = ref(null)
const allNoticesSummary = ref(null)
const eventPlanDraft = reactive({ expected_residents: '', duration: '', budget: '' })
const eventPlanResult = ref(null)
const settingsForm = reactive({ maintenance_reminders: true, email_alerts: true, auto_approvals: false })

function isAiBusy(key) {
  return aiBusyKey.value === key
}
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

function matchesSearch(item, query) {
  if (!query) return true
  const token = String(query).toLowerCase()
  const values = Object.values(item || {}).map((value) => String(value || '').toLowerCase())
  return values.some((value) => value.includes(token))
}

const filteredUsers = computed(() => {
  const query = String(activeSearchQuery.value || '').trim().toLowerCase()
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
  const query = String(activeSearchQuery.value || '').trim().toLowerCase()
  if (!query) return backendProviders.value
  return backendProviders.value.filter((item) => matchesSearch(item, query))
})

const tenantRows = computed(() => {
  const query = String(tenantSearchQuery.value || '').trim().toLowerCase()
  if (!query) return backendTenants.value
  return backendTenants.value.filter((item) => {
    const values = [item.name, item.email, item.phone, item.flat, item.owner, item.status].map((value) => String(value || '').toLowerCase())
    return values.some((value) => value.includes(query))
  })
})


const systemLogRows = computed(() => backendSystemLogs.value.map((log) => ({
  id: log.id,
  action: log.action,
  user: log.user_id ? `User #${log.user_id}` : 'System',
  timestamp: log.created_at,
  details: log.details,
})))

const complaintRows = computed(() => {
  const query = String(activeSearchQuery.value || '').trim().toLowerCase()
  if (!query) return backendComplaints.value
  return backendComplaints.value.filter((item) => matchesSearch(item, query))
})

const noticeRows = computed(() => {
  const query = String(activeSearchQuery.value || '').trim().toLowerCase()
  if (!query) return backendNotices.value
  return backendNotices.value.filter((item) => matchesSearch(item, query))
})

const eventRows = computed(() => {
  const query = String(activeSearchQuery.value || '').trim().toLowerCase()
  if (!query) return backendEvents.value
  return backendEvents.value.filter((item) => matchesSearch(item, query))
})

const assignableUsers = computed(() => {
  const roles = new Set(['service_provider'])
  return filteredUsers.value
    .filter((user) => roles.has(String(user.role || '').toLowerCase()))
    .map((user) => ({ id: user.id, name: user.full_name || user.name || `User #${user.id}` }))
})

const clusterComplaints = computed(() => {
  if (!activeCluster.value) return []
  const ids = new Set(activeCluster.value.complaint_ids || [])
  return backendComplaints.value.filter((complaint) => ids.has(complaint.id))
})

function categoryIcon(category) {
  const icons = { Electrical: '⚡', Plumbing: '🔧', Maintenance: '🛠', Security: '🛡' }
  return icons[category] || '📋'
}

function openCluster(issue) {
  activeCluster.value = issue
}

function closeClusterModal() {
  activeCluster.value = null
}

async function loadEmergingIssues() {
  isLoadingEmergingIssues.value = true
  try {
    emergingIssues.value = await authStore.getEmergingIssues()
  } catch (error) {
    emergingIssues.value = []
    notify.error(error instanceof Error ? error.message : 'Unable to load emerging issues')
  } finally {
    isLoadingEmergingIssues.value = false
    emergingIssuesLoaded.value = true
  }
}

async function loadAllUsers(searchTerm = '') {
  const limit = 100
  let page = 1
  let pages = 1
  const allItems = []

  do {
    const params = new URLSearchParams({ page: String(page), limit: String(limit) })
    if (searchTerm) params.set('search', searchTerm)
    const query = params.toString()
    const payload = await authStore.listUsers(query, { withMeta: true })
    const items = payload?.items || []
    allItems.push(...items)

    const totalPages = Number(payload?.pagination?.pages || 1)
    pages = Number.isFinite(totalPages) && totalPages > 0 ? totalPages : 1
    page += 1
  } while (page <= pages)

  return allItems
}

async function loadAllComplaints(searchTerm = '') {
  const limit = 100
  let page = 1
  let pages = 1
  const allItems = []

  do {
    const params = new URLSearchParams({ page: String(page), limit: String(limit) })
    if (searchTerm) params.set('search', searchTerm)
    const query = params.toString()
    const payload = await authStore.listComplaints(query, { withMeta: true })
    const items = payload?.items || []
    allItems.push(...items)

    const totalPages = Number(payload?.pagination?.pages || 1)
    pages = Number.isFinite(totalPages) && totalPages > 0 ? totalPages : 1
    page += 1
  } while (page <= pages)

  return allItems
}

function formatNoticeBodyText(rawText) {
  if (!rawText) return ''
  let text = String(rawText).trim()

  // Format English sections
  text = text.replace(/^(Dear Residents,?\s*|Notice:?\s*|Greeting:?\s*)/gi, '$1\n\n')
  text = text.replace(/([^\n])\s*(Date:\s*)/gi, '$1\n\n$2')
  text = text.replace(/([^\n])\s*(Time:\s*)/gi, '$1\n$2')
  text = text.replace(/([^\n])\s*(Location:\s*|Venue:\s*)/gi, '$1\n$2')
  text = text.replace(/([^\n])\s*(All residents|Please note|Note:)/gi, '$1\n\n$2')
  text = text.replace(/([^\n])\s*(Thank you[^\.\n]*[\.\!]?)/gi, '$1\n\n$2')
  text = text.replace(/([^\n])\s*(Warm regards,?|Regards,?|Best regards,?)/gi, '$1\n\n$2')
  text = text.replace(/(Warm regards,?|Regards,?|Best regards,?)\s*,?\s*([^\n]+)/gi, '$1\n$2')

  // Format Telugu sections
  text = text.replace(/^(గౌరవనీయ నివాసులకు,?\s*)/gi, '$1\n\n')
  text = text.replace(/([^\n])\s*(తేదీ:\s*)/gi, '$1\n\n$2')
  text = text.replace(/([^\n])\s*(సమయం:\s*)/gi, '$1\n$2')
  text = text.replace(/([^\n])\s*(స్థలం:\s*)/gi, '$1\n$2')
  text = text.replace(/([^\n])\s*(నివాసులందరూ)/gi, '$1\n\n$2')
  text = text.replace(/([^\n])\s*(ధన్యవాదాలు[^\.\n]*[\.\!]?|మీ సహకారానికి ధన్యవాదాలు[^\.\n]*[\.\!]?)/gi, '$1\n\n$2')
  text = text.replace(/([^\n])\s*(భవదీయులు,?|మేనేజ్‌మెంట్ కమిటీ)/gi, '$1\n\n$2')
  text = text.replace(/(భవదీయులు,?)\s*,?\s*([^\n]+)/gi, '$1\n$2')

  // Format Hindi sections
  text = text.replace(/^(प्रिय निवासियों,?\s*)/gi, '$1\n\n')
  text = text.replace(/([^\n])\s*(दिनांक:\s*)/gi, '$1\n\n$2')
  text = text.replace(/([^\n])\s*(समय:\s*)/gi, '$1\n$2')
  text = text.replace(/([^\n])\s*(स्थान:\s*)/gi, '$1\n$2')
  text = text.replace(/([^\n])\s*(सभी निवासियों)/gi, '$1\n\n$2')
  text = text.replace(/([^\n])\s*(धन्यवाद[^\.\n]*[\.\!]?|आपके सहयोग के लिए धन्यवाद[^\.\n]*[\.\!]?)/gi, '$1\n\n$2')
  text = text.replace(/([^\n])\s*(सादर,?|प्रबंध समिति)/gi, '$1\n\n$2')
  text = text.replace(/(सादर,?)\s*,?\s*([^\n]+)/gi, '$1\n$2')

  text = text.replace(/\n{3,}/g, '\n\n')
  return text
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
      const searchTerm = String(activeSearchQuery.value || '').trim()
      const searchQueryString = searchTerm ? new URLSearchParams({ search: searchTerm }).toString() : ''
      const tenantSearchTerm = String(tenantSearchQuery.value || '').trim()
      const tenantSearchQueryString = tenantSearchTerm ? new URLSearchParams({ search: tenantSearchTerm }).toString() : ''

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
        tenantsResult,
        logsResult,
        settingsResult,
        billsResult,
      ] = await Promise.allSettled([
        loadAllUsers(''),
        authStore.listProviders(searchQueryString),
        loadAllComplaints(searchTerm),
        authStore.listNotices(searchQueryString),
        authStore.listEvents(searchQueryString),
        authStore.getAdminDashboardStats(),
        authStore.getBookingsAnalytics(),
        authStore.getComplaintsAnalytics(),
        authStore.listServiceCategories(),
        authStore.getMonthlyReport(),
        authStore.listTenants(tenantSearchQueryString),
        authStore.listSystemLogs(),
        authStore.getSettings(),
        authStore.listMaintenanceBills(),
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
      if (tenantsResult.status === 'fulfilled') backendTenants.value = tenantsResult.value
      if (logsResult.status === 'fulfilled') backendSystemLogs.value = logsResult.value
      if (billsResult.status === 'fulfilled') backendMaintenanceBills.value = billsResult.value
      if (settingsResult.status === 'fulfilled') {
        settingsForm.maintenance_reminders = String(settingsResult.value.maintenance_reminders || 'true') === 'true'
        settingsForm.email_alerts = String(settingsResult.value.email_alerts || 'true') === 'true'
        settingsForm.auto_approvals = String(settingsResult.value.auto_approvals || 'false') === 'true'
      }
    }
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to load admin data')
  }
}

async function saveSettings() {
  try {
    await authStore.updateSettings(settingsForm)
    notify.success('Settings saved successfully')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to save settings')
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
      flat_number: String(residentForm.flat_number || '').trim(),
      status: 'active',
    })
    residentForm.full_name = ''
    residentForm.email = ''
    residentForm.phone = ''
    residentForm.password = ''
    residentForm.flat_number = ''
    showResidentForm.value = false
    await loadAdminData()
    notify.success('Resident added successfully')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to add resident')
  }
}

function resetTenantForm() {
  tenantForm.full_name = ''
  tenantForm.email = ''
  tenantForm.phone = ''
  tenantForm.password = ''
  tenantForm.flat_number = ''
  tenantForm.leaseStart = ''
  tenantForm.leaseEnd = ''
  tenantForm.status = 'active'
}

function openTenantForm(tenant = null) {
  if (!tenant) {
    editingTenantId.value = null
    showTenantForm.value = !showTenantForm.value
    if (showTenantForm.value) resetTenantForm()
    return
  }

  editingTenantId.value = tenant.id
  showTenantForm.value = true
  tenantForm.full_name = tenant.name || ''
  tenantForm.email = tenant.email || ''
  tenantForm.phone = tenant.phone || ''
  tenantForm.password = ''
  tenantForm.flat_number = tenant.flat || ''
  tenantForm.leaseStart = tenant.leaseStart || ''
  tenantForm.leaseEnd = tenant.leaseEnd || ''
  tenantForm.status = tenant.status || 'active'
}

async function submitTenant() {
  try {
    const payload = {
      full_name: String(tenantForm.full_name || '').trim(),
      email: String(tenantForm.email || '').trim(),
      phone: String(tenantForm.phone || '').trim(),
      flat_number: String(tenantForm.flat_number || '').trim(),
      leaseStart: tenantForm.leaseStart || null,
      leaseEnd: tenantForm.leaseEnd || null,
      status: String(tenantForm.status || 'active').trim().toLowerCase(),
    }

    if (editingTenantId.value) {
      if (tenantForm.password) payload.password = String(tenantForm.password)
      await authStore.updateTenant(editingTenantId.value, payload)
      notify.success('Tenant updated successfully')
    } else {
      payload.password = String(tenantForm.password || '')
      await authStore.createTenant(payload)
      notify.success('Tenant created successfully')
    }

    showTenantForm.value = false
    editingTenantId.value = null
    resetTenantForm()
    await loadAdminData()
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to save tenant')
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
    backendComplaints.value = await loadAllComplaints()
    syncComplaintAssignments()
    complaintStatusBreakdown.value = await authStore.getComplaintsAnalytics()
    notify.success('Complaint assigned successfully')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Unable to assign complaint')
  }
}

async function submitNotice() {
  try {
    // Body stays the primary (English) text. Any AI translations are saved
    // separately so residents can pick their language — never concatenated.
    const translations = noticeTranslations.value && typeof noticeTranslations.value === 'object'
      ? noticeTranslations.value
      : null
    await authStore.createNotice({
      title: String(noticeForm.title || '').trim(),
      body: String(noticeForm.body || '').trim(),
      notice_type: noticeForm.notice_type,
      priority: noticeForm.priority,
      translations,
    })
    backendNotices.value = await authStore.listNotices()
    noticeForm.title = ''
    noticeForm.body = ''
    noticeTranslations.value = null
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

function formatAllNoticesSummary(summary) {
  if (!summary) return ''
  if (summary.digest_markdown) return summary.digest_markdown
  const groups = Array.isArray(summary.groups) ? summary.groups : []
  return groups
    .map((g) => {
      const items = Array.isArray(g.items) ? g.items.map((i) => `  • ${i}`).join('\n') : ''
      return `${g.theme || 'Notices'}:\n${items}`
    })
    .join('\n\n')
}

async function withAi(key, task) {
  if (aiBusyKey.value === key) return
  aiBusyKey.value = key
  try {
    await task()
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'AI request failed')
  } finally {
    if (aiBusyKey.value === key) {
      aiBusyKey.value = null
    }
  }
}

async function generateNoticeWithAI() {
  await withAi('notice-generate', async () => {
    const topic = String(aiNoticeDraft.topic || noticeForm.title || '').trim()
    if (!topic) {
      notify.error('Enter an AI topic or notice title first')
      return
    }
    const result = await authStore.aiGenerateNotice({
      topic,
      date: aiNoticeDraft.date,
      time: aiNoticeDraft.time,
      extra: aiNoticeDraft.extra,
    })
    noticeForm.title = result?.title || noticeForm.title
    noticeForm.body = result?.body || noticeForm.body
    notify.success('Notice draft generated — review before publishing')
  })
}

async function translateNoticeWithAI() {
  await withAi('notice-translate', async () => {
    const text = String(noticeForm.body || '').trim()
    if (!text) {
      notify.error('Write or generate notice content first')
      return
    }
    const result = await authStore.aiTranslateAnnouncement(text, ['English', 'Hindi', 'Telugu'])
    noticeTranslations.value = result?.translations || null
    notify.success('Translations ready — review before publishing')
  })
}

async function summarizeAllNotices() {
  await withAi('notices-summarize-all', async () => {
    const notices = (noticeRows.value || []).map((n) => ({
      title: n.title,
      body: n.body || n.content || '',
    }))
    if (!notices.length) {
      notify.error('No notices to summarize')
      return
    }
    allNoticesSummary.value = await authStore.aiSummarizeAllNotices(notices)
    notify.success('All notices summarized')
  })
}

async function planEventWithAI() {
  await withAi('event-plan', async () => {
    const eventName = String(eventForm.title || '').trim()
    if (!eventName) {
      notify.error('Enter an event name first')
      return
    }
    const result = await authStore.aiPlanEvent({
      event_name: eventName,
      expected_residents: Number(eventPlanDraft.expected_residents) || null,
      duration: eventPlanDraft.duration,
      budget: eventPlanDraft.budget,
      notes: eventForm.description,
    })
    eventPlanResult.value = result
    if (result?.announcement_draft && !eventForm.description) {
      eventForm.description = result.announcement_draft
    } else if (result?.plan_markdown) {
      eventForm.description = result.plan_markdown
    }
    notify.success('Event plan generated')
  })
}



function priorityWeight(priority) {
  const p = String(priority || '').toLowerCase()
  if (p === 'critical' || p === 'urgent' || p === 'high') return 3
  if (p === 'medium') return 2
  if (p === 'low') return 1
  return 2
}

function priorityBadgeClass(priority) {
  const p = String(priority || '').toLowerCase()
  if (p === 'critical' || p === 'urgent' || p === 'high') return 'badge-danger'
  if (p === 'medium') return 'badge-warning'
  return 'badge-info'
}

function getResidentName(userIdOrName) {
  if (!userIdOrName) return '-'
  if (typeof userIdOrName === 'string' && !/^\d+$/.test(userIdOrName)) return userIdOrName
  const idNum = Number(userIdOrName)
  const found = backendUsers.value.find((u) => u.id === idNum)
  return found ? (found.full_name || found.name || `Resident #${idNum}`) : `Resident #${userIdOrName}`
}

const sortedComplaints = computed(() => {
  let list = [...backendComplaints.value]
  if (selectedPriorityFilter.value !== 'All') {
    list = list.filter((c) => {
      const p = String(c.priority || 'Medium').toLowerCase()
      const target = selectedPriorityFilter.value.toLowerCase()
      if (target === 'high') return p === 'high' || p === 'critical' || p === 'urgent'
      return p === target
    })
  }
  if (selectedSortOrder.value === 'priority-desc') {
    list.sort((a, b) => priorityWeight(b.priority) - priorityWeight(a.priority))
  } else if (selectedSortOrder.value === 'id-desc') {
    list.sort((a, b) => (b.id || 0) - (a.id || 0))
  } else if (selectedSortOrder.value === 'status') {
    list.sort((a, b) => String(a.status || '').localeCompare(String(b.status || '')))
  }
  return list
})

async function runAiClassifySingleComplaint(complaint) {
  const key = `classify-${complaint.id}`
  await withAi(key, async () => {
    const subject = complaint.subject || complaint.title || 'Complaint'
    const description = complaint.description || subject
    const res = await authStore.aiClassifyComplaint({ subject, description })
    if (res) {
      complaint.priority = res.priority || 'Medium'
      complaint.category = res.category || complaint.category || 'General'
      notify.success(`AI Priority set to '${res.priority}' (${res.category})`)
    }
  })
}

async function runAiClassifyAllComplaints() {
  await withAi('complaint-classify-all', async () => {
    const list = backendComplaints.value
    if (!list.length) {
      notify.error('No complaints to classify')
      return
    }
    let count = 0
    for (const complaint of list) {
      const subject = complaint.subject || complaint.title || 'Complaint'
      const description = complaint.description || subject
      try {
        const res = await authStore.aiClassifyComplaint({ subject, description })
        if (res) {
          complaint.priority = res.priority || 'Medium'
          complaint.category = res.category || complaint.category || 'General'
          count++
        }
      } catch (e) {
        // continue for remaining complaints
      }
    }
    selectedSortOrder.value = 'priority-desc'
    notify.success(`AI classified ${count} complaints and sorted by Priority (High → Low)`)
  })
}

onMounted(() => {
  loadAdminData()
})

watch(
  () => route.query.q,
  () => {
    loadAdminData()
  }
)

watch(tenantSearchQuery, () => {
  if (page.value === 'tenants') {
    loadAdminData()
  }
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
.notice-row {
  padding: var(--space-5);
}
.row-actions { display: flex; gap: var(--space-2); }

.emerging-issues-wrapper { margin-bottom: var(--space-4); }
.emerging-issues { display: grid; gap: var(--space-3); }
.emerging-issues-header { display: flex; align-items: center; justify-content: space-between; }
.issue-grid { grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); }
.issue-card {
  display: grid;
  gap: var(--space-1);
  text-align: left;
  cursor: pointer;
  border: 1px solid var(--color-border);
  background: var(--color-surface, #fff);
  transition: box-shadow 0.15s ease, transform 0.15s ease;
}
.issue-card:hover { box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08); transform: translateY(-2px); }
.issue-icon { font-size: 1.5rem; }
.issue-category { font-size: var(--text-xs, 0.75rem); text-transform: uppercase; letter-spacing: 0.04em; color: var(--color-text-secondary); }
.issue-title { font-weight: var(--font-bold); font-size: var(--text-lg, 1.05rem); }
.issue-count { color: var(--color-text-secondary); font-size: var(--text-sm, 0.85rem); }

.emerging-issues-trigger {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  flex-wrap: wrap;
}
.emerging-issues-trigger h3 { margin: 0 0 var(--space-1) 0; }
.emerging-issues-trigger p { margin: 0; color: var(--color-text-secondary); }

.emerging-issues-loading {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}
.emerging-issues-loading p { margin: 0; color: var(--color-text-secondary); }

.emerging-issues-empty {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
}
.emerging-issues-empty p { margin: 0; color: var(--color-text-secondary); }

.thinking-dots {
  display: flex;
  gap: 6px;
  align-items: center;
  flex-shrink: 0;
}
.thinking-dots span {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--color-primary);
  animation: thinking-dot-wave 1.2s infinite ease-in-out;
}
.thinking-dots span:nth-child(2) { animation-delay: 0.15s; }
.thinking-dots span:nth-child(3) { animation-delay: 0.3s; }
@keyframes thinking-dot-wave {
  0%, 60%, 100% { transform: translateY(0); opacity: 0.5; }
  30% { transform: translateY(-8px); opacity: 1; }
}

.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 15, 20, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-4);
  z-index: 1000;
}
.modal-panel {
  background: var(--color-surface, #fff);
  border-radius: var(--radius-lg, 12px);
  max-width: 720px;
  width: 100%;
  max-height: 85vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.modal-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: var(--space-4);
  padding: var(--space-5);
  border-bottom: 1px solid var(--color-border);
}
.modal-header h3 { margin: 0 0 var(--space-1) 0; }
.modal-header p { margin: 0; color: var(--color-text-secondary); }
.modal-body { padding: var(--space-5); overflow-y: auto; display: grid; gap: var(--space-4); }
.cluster-row {
  display: grid;
  gap: var(--space-3);
  padding-bottom: var(--space-4);
  border-bottom: 1px solid var(--color-border);
}
.cluster-row:last-child { border-bottom: none; padding-bottom: 0; }
.cluster-row-main p { color: var(--color-text-secondary); margin: var(--space-1) 0; }
.cluster-row-actions { display: flex; }
.cluster-row-actions .row-actions { flex: 1; display: flex; gap: var(--space-2); }
.cluster-row-actions .row-actions select { flex: 1; }

.form-card { display: grid; gap: var(--space-5); }
.form-grid.two-col { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-5); }
.switch-row { display: flex; align-items: center; justify-content: space-between; gap: var(--space-4); padding: var(--space-2) 0; }
.ai-panel { display: grid; gap: var(--space-3); }
.ai-output {
  white-space: pre-wrap;
  margin: 0;
  padding: var(--space-4);
  border-radius: var(--radius-lg);
  background: var(--color-gray-50);
  border: 1px solid var(--color-border);
  font-family: inherit;
  font-size: var(--text-sm);
  line-height: 1.5;
}
.translation-block { display: grid; gap: var(--space-2); margin-top: var(--space-3); }
.muted { color: var(--color-text-secondary); }
.align-start { align-items: start; }
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

.complaints-filter-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  margin-bottom: var(--space-4);
  padding: 14px 20px;
}

.filter-controls-group {
  display: flex;
  align-items: center;
  gap: var(--space-6, 24px);
  flex-wrap: wrap;
}

.filter-label {
  display: flex;
  align-items: center;
  gap: var(--space-2, 8px);
  font-weight: 500;
  white-space: nowrap;
  font-size: var(--text-sm, 0.875rem);
}

.filter-label-text {
  white-space: nowrap;
}

.form-select-sm {
  padding: 6px 12px;
  border-radius: 6px;
  border: 1px solid var(--color-border, #cbd5e1);
  background-color: var(--color-surface, #ffffff);
  font-size: var(--text-sm, 0.875rem);
  color: var(--color-text-primary, #1e293b);
}
</style>
