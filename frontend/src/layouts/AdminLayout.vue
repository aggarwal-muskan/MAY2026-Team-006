<template>
  <div class="portal-layout">
    <!-- Sidebar -->
    <aside class="sidebar" :class="{ collapsed: sidebarCollapsed, 'mobile-open': mobileOpen }">
      <div class="sidebar-header">
        <router-link to="/" class="sidebar-logo">
          <div class="logo-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
              <polyline points="9 22 9 12 15 12 15 22"></polyline>
            </svg>
          </div>
          <span v-show="!sidebarCollapsed" class="logo-text">SocioNeed</span>
        </router-link>
        <button class="sidebar-collapse-btn" @click="sidebarCollapsed = !sidebarCollapsed" v-show="!sidebarCollapsed">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="11 17 6 12 11 7"></polyline>
            <polyline points="18 17 13 12 18 7"></polyline>
          </svg>
        </button>
      </div>

      <nav class="sidebar-nav">
        <div v-for="group in sidebarItems" :key="group.label" class="nav-group">
          <div v-if="group.label && !sidebarCollapsed" class="nav-group-label">{{ group.label }}</div>
          <router-link
            v-for="item in group.items"
            :key="item.to"
            :to="item.to"
            class="nav-item"
            :class="{ active: isActive(item.to) }"
            @click="mobileOpen = false"
          >
            <span class="nav-icon" v-html="item.icon"></span>
            <span v-show="!sidebarCollapsed" class="nav-label">{{ item.label }}</span>
            <span v-if="item.badge && !sidebarCollapsed" class="nav-badge">{{ item.badge }}</span>
          </router-link>
        </div>
      </nav>

      <div class="sidebar-footer">
        <div class="sidebar-user" v-show="!sidebarCollapsed">
          <div class="avatar avatar-sm">A</div>
          <div class="user-info">
            <div class="user-name">Admin User</div>
            <div class="user-role">Administrator</div>
          </div>
        </div>
        <button class="nav-item logout-btn" @click="handleLogout">
          <span class="nav-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
              <polyline points="16 17 21 12 16 7"></polyline>
              <line x1="21" y1="12" x2="9" y2="12"></line>
            </svg>
          </span>
          <span v-show="!sidebarCollapsed" class="nav-label">Logout</span>
        </button>
      </div>
    </aside>

    <!-- Mobile Overlay -->
    <div v-if="mobileOpen" class="sidebar-overlay" @click="mobileOpen = false"></div>

    <!-- Main Content Area -->
    <div class="portal-main" :class="{ 'sidebar-collapsed': sidebarCollapsed }">
      <!-- Top Bar -->
      <header class="topbar admin-topbar">
        <div class="topbar-left">
          <button class="mobile-menu-btn" @click="mobileOpen = true">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="3" y1="12" x2="21" y2="12"></line>
              <line x1="3" y1="6" x2="21" y2="6"></line>
              <line x1="3" y1="18" x2="21" y2="18"></line>
            </svg>
          </button>
          <button v-if="sidebarCollapsed" class="expand-btn" @click="sidebarCollapsed = false">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="13 17 18 12 13 7"></polyline>
              <polyline points="6 17 11 12 6 7"></polyline>
            </svg>
          </button>
          <div class="admin-breadcrumb">
            <span class="breadcrumb-item active">Admin Dashboard</span>
          </div>
        </div>
        <div class="topbar-right">
          <div class="search-box">
            <span class="search-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="8"></circle>
                <path d="m21 21-4.35-4.35"></path>
              </svg>
            </span>
            <input type="text" placeholder="Search anything..." v-model="searchQuery" @keydown.enter.prevent="submitSearch" />
          </div>
          <div class="topbar-user">
            <div class="avatar avatar-sm">A</div>
            <div class="user-meta hide-mobile">
              <span class="user-name">Admin User</span>
              <span class="user-flat">Administrator</span>
            </div>
          </div>
        </div>
      </header>

      <!-- Page Content -->
      <div class="portal-content">
        <slot />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()

const sidebarCollapsed = ref(false)
const mobileOpen = ref(false)
const searchQuery = ref('')
const complaintBadgeCount = ref(0)

function isActive(path) {
  return route.path === path || route.path.startsWith(path + '/')
}

function handleLogout() {
  authStore.logout()
  router.push('/login')
}

function submitSearch() {
  const trimmed = String(searchQuery.value || '').trim()
  router.push({
    path: route.path,
    query: trimmed ? { ...route.query, q: trimmed } : { ...route.query, q: undefined },
  })
}

async function loadAdminBadgeCounts() {
  if (!authStore.token) return
  try {
    const complaintsPayload = await authStore.listComplaints({ withMeta: true })
    complaintBadgeCount.value = complaintsPayload?.pagination?.total ?? complaintsPayload?.items?.length ?? 0
  } catch {
    complaintBadgeCount.value = 0
  }
}

const iconDashboard = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>'
const iconUsers = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>'
const iconFile = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>'
const iconBell = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>'
const iconCalendar = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>'
const iconChart = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>'
const iconSettings = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>'
const iconShield = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'
const iconDollar = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>'
const iconDownload = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>'
const iconList = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>'
const iconTool = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>'

const sidebarItems = computed(() => [
  {
    label: 'Overview',
    items: [
      { label: 'Admin Dashboard', to: '/admin/dashboard', icon: iconDashboard },
    ]
  },
  {
    label: 'People',
    items: [
      { label: 'Residents', to: '/admin/residents', icon: iconUsers },
      { label: 'Tenants', to: '/admin/tenants', icon: iconUsers },
      { label: 'Providers', to: '/admin/providers', icon: iconTool },
    ]
  },
  {
    label: 'Management',
    items: [
      { label: 'Complaints', to: '/admin/complaints', icon: iconFile, badge: complaintBadgeCount.value },
      { label: 'Amenities', to: '/admin/events', icon: iconCalendar },
      { label: 'Notices', to: '/admin/notices', icon: iconBell },
      { label: 'Events', to: '/admin/events', icon: iconCalendar },
    ]
  },
  {
    label: 'Finance & Reports',
    items: [
      { label: 'Maintenance Fees', to: '/admin/maintenance-fees', icon: iconDollar },
      { label: 'Analytics', to: '/admin/analytics', icon: iconChart },
      { label: 'Reports & Export', to: '/admin/reports', icon: iconDownload },
    ]
  },
  {
    label: 'System',
    items: [
      { label: 'Roles & Permissions', to: '/admin/roles', icon: iconShield },
      { label: 'System Logs', to: '/admin/logs', icon: iconList },
      { label: 'Settings', to: '/admin/settings', icon: iconSettings },
    ]
  },
])

onMounted(() => {
  loadAdminBadgeCounts()
})

watch(
  () => route.fullPath,
  () => {
    loadAdminBadgeCounts()
  }
)

watch(
  () => route.query.q,
  (value) => {
    searchQuery.value = String(value || '')
  },
  { immediate: true }
)
</script>

<style scoped>
.portal-layout {
  display: flex;
  min-height: 100vh;
  background:
    radial-gradient(circle at top left, rgba(37, 99, 235, 0.08), transparent 26%),
    var(--color-background);
}

.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  z-index: var(--z-sticky);
  display: flex;
  flex-direction: column;
  width: var(--sidebar-width);
  overflow-x: hidden;
  overflow-y: auto;
  border-right: 1px solid rgba(229, 231, 235, 0.9);
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(18px);
  box-shadow: 14px 0 40px rgba(15, 23, 42, 0.04);
  transition: width var(--transition-base), transform var(--transition-base);
}

.sidebar::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: linear-gradient(180deg, rgba(37, 99, 235, 0.03), transparent 30%);
}

.sidebar.collapsed {
  width: var(--sidebar-collapsed-width);
}

.sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-3);
  padding: var(--space-5) var(--space-4);
  border-bottom: 1px solid var(--color-border);
}

.sidebar-logo {
  display: inline-flex;
  align-items: center;
  gap: var(--space-3);
  text-decoration: none;
}

.sidebar-logo .logo-icon {
  width: 36px;
  height: 36px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-lg);
  color: white;
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light));
  box-shadow: 0 14px 28px rgba(37, 99, 235, 0.24);
}

.sidebar-logo .logo-text {
  font-family: var(--font-heading);
  font-size: var(--text-lg);
  font-weight: var(--font-bold);
  color: var(--color-text-primary);
  white-space: nowrap;
}

.sidebar-collapse-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-full);
  color: var(--color-text-secondary);
  background: var(--color-surface);
}

.sidebar-collapse-btn:hover {
  color: var(--color-text-primary);
  border-color: var(--color-primary-100);
  background: var(--color-primary-50);
}

.sidebar-nav {
  flex: 1;
  padding: var(--space-3);
}

.nav-group {
  margin-bottom: var(--space-2);
}

.nav-group-label {
  padding: var(--space-3) var(--space-3) var(--space-2);
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--color-text-muted);
}

.nav-item {
  position: relative;
  display: flex;
  align-items: center;
  gap: var(--space-3);
  width: 100%;
  padding: var(--space-3);
  border: 1px solid transparent;
  border-radius: var(--radius-lg);
  color: var(--color-text-secondary);
  text-align: left;
  background: transparent;
}

.nav-item::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  width: 4px;
  height: 60%;
  border-radius: 0 var(--radius-full) var(--radius-full) 0;
  background: var(--color-primary);
  transform: translateY(-50%) scaleY(0);
  transform-origin: center;
  transition: transform var(--transition-base);
}

.nav-item:hover {
  color: var(--color-text-primary);
  background: var(--color-gray-50);
}

.nav-item.active {
  color: var(--color-primary);
  background: var(--color-primary-50);
  border-color: rgba(37, 99, 235, 0.08);
  box-shadow: inset 0 0 0 1px rgba(37, 99, 235, 0.06);
}

.nav-item.active::before {
  transform: translateY(-50%) scaleY(1);
}

.nav-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  color: inherit;
}

.nav-label {
  flex: 1;
  white-space: nowrap;
}

.nav-badge {
  padding: 2px 8px;
  border-radius: var(--radius-full);
  color: white;
  background: linear-gradient(135deg, var(--color-danger), var(--color-danger-light));
  font-size: 10px;
  font-weight: var(--font-bold);
  line-height: 1.4;
}

.sidebar-footer {
  padding: var(--space-3);
  border-top: 1px solid var(--color-border);
}

.sidebar-user {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  margin-bottom: var(--space-2);
  padding: var(--space-3);
  border-radius: var(--radius-lg);
  background: var(--color-gray-50);
}

.user-info {
  overflow: hidden;
}

.user-info .user-name {
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.user-info .user-role {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
}

.logout-btn:hover {
  color: var(--color-danger-dark) !important;
  background: var(--color-danger-50) !important;
}

.portal-main {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  margin-left: var(--sidebar-width);
  transition: margin-left var(--transition-base);
}

.portal-main.sidebar-collapsed {
  margin-left: var(--sidebar-collapsed-width);
}

.topbar {
  position: sticky;
  top: 0;
  z-index: calc(var(--z-sticky) - 1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  height: var(--topbar-height);
  padding: 0 var(--space-6);
  border-bottom: 1px solid rgba(229, 231, 235, 0.9);
  background: rgba(248, 250, 252, 0.82);
  backdrop-filter: blur(18px);
}

.topbar-left,
.topbar-right {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.admin-breadcrumb {
  display: inline-flex;
  align-items: center;
  padding: var(--space-2) var(--space-3);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-full);
  background: var(--color-surface);
  box-shadow: var(--shadow-xs);
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
}

.breadcrumb-item.active {
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
}

.mobile-menu-btn,
.expand-btn {
  display: none;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.9);
  color: var(--color-text-secondary);
}

.expand-btn {
  display: inline-flex;
}

.search-box {
  width: min(360px, 36vw);
}

.search-box input {
  background: rgba(255, 255, 255, 0.95);
}

.topbar-user {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-lg);
  cursor: pointer;
}

.topbar-user:hover {
  background: var(--color-gray-50);
}

.user-meta {
  display: flex;
  flex-direction: column;
}

.user-meta .user-name {
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
  line-height: 1.2;
}

.user-meta .user-flat {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
}

.portal-content {
  flex: 1;
  padding: var(--space-6);
}

.sidebar-overlay {
  position: fixed;
  inset: 0;
  z-index: calc(var(--z-sticky) - 1);
  background: rgba(15, 23, 42, 0.42);
  backdrop-filter: blur(4px);
}

@media (max-width: 1024px) {
  .sidebar {
    transform: translateX(-100%);
  }

  .sidebar.mobile-open {
    transform: translateX(0);
  }

  .portal-main,
  .portal-main.sidebar-collapsed {
    margin-left: 0;
  }

  .mobile-menu-btn,
  .expand-btn {
    display: inline-flex;
  }

  .expand-btn {
    display: none;
  }
}

@media (max-width: 768px) {
  .topbar {
    padding-inline: var(--space-4);
  }

  .portal-content {
    padding: var(--space-4);
  }

  .hide-mobile {
    display: none !important;
  }

  .search-box {
    display: none;
  }
}
</style>
