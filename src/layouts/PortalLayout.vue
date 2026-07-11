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
          <div class="avatar avatar-sm">{{ userInitials }}</div>
          <div class="user-info">
            <div class="user-name">{{ userName }}</div>
            <div class="user-role">{{ userRoleLabel }}</div>
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
      <header class="topbar">
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
          <div class="search-box">
            <span class="search-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="8"></circle>
                <path d="m21 21-4.35-4.35"></path>
              </svg>
            </span>
            <input type="text" placeholder="Search anything..." v-model="searchQuery" />
          </div>
        </div>
        <div class="topbar-right">
          <button class="topbar-icon-btn" @click="$router.push(notifRoute)">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
            </svg>
            <span class="notif-dot"></span>
          </button>
          <div class="topbar-user" @click="$router.push(profileRoute)">
            <div class="avatar avatar-sm">{{ userInitials }}</div>
            <div class="user-meta hide-mobile">
              <span class="user-name">{{ userName }}</span>
              <span class="user-flat">{{ userFlat }}</span>
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
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

const props = defineProps({
  sidebarType: { type: String, default: 'resident' }
})

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()

const sidebarCollapsed = ref(false)
const mobileOpen = ref(false)
const searchQuery = ref('')

const userName = computed(() => authStore.user?.name || 'Guest User')
const userInitials = computed(() => authStore.userInitials || 'G')
const userFlat = computed(() => authStore.user?.flat || authStore.user?.category || '')
const userRoleLabel = computed(() => {
  const labels = { resident: 'Resident', provider: 'Service Provider', security: 'Security' }
  return labels[props.sidebarType] || 'User'
})

const notifRoute = computed(() => {
  const routes = { resident: '/resident/notifications', provider: '/provider/notifications', security: '/security/dashboard' }
  return routes[props.sidebarType] || '/resident/notifications'
})

const profileRoute = computed(() => {
  const routes = { resident: '/resident/profile', provider: '/provider/profile', security: '/security/dashboard' }
  return routes[props.sidebarType] || '/resident/profile'
})

function isActive(path) {
  return route.path === path || route.path.startsWith(path + '/')
}

function handleLogout() {
  authStore.logout()
  router.push('/login')
}

// ── Sidebar Items by Role ──
const sidebarConfigs = {
  resident: [
    {
      label: 'Main',
      items: [
        { label: 'Dashboard', to: '/resident/dashboard', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>' },
        { label: 'My Complaints', to: '/resident/complaints', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>', badge: 3 },
        { label: 'Book Amenities', to: '/resident/amenities', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>' },
        { label: 'Browse Services', to: '/resident/services', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>' },
      ]
    },
    {
      label: 'Community',
      items: [
        { label: 'Events', to: '/resident/events', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>' },
        { label: 'Notices', to: '/resident/notices', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>', badge: 7 },
        { label: 'Parking', to: '/resident/parking', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>' },
        { label: 'My Family', to: '/resident/family', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>' },
      ]
    },
    {
      label: 'Account',
      items: [
        { label: 'Maintenance Bills', to: '/resident/maintenance-bills', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>' },
        { label: 'Help & Support', to: '/resident/help', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>' },
        { label: 'My Profile', to: '/resident/profile', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>' },
      ]
    },
  ],
  provider: [
    {
      label: 'Main',
      items: [
        { label: 'Dashboard', to: '/provider/dashboard', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>' },
        { label: 'Bookings', to: '/provider/bookings', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>', badge: 3 },
        { label: 'Availability', to: '/provider/availability', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>' },
        { label: 'My Services', to: '/provider/services', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>' },
      ]
    },
    {
      label: 'Performance',
      items: [
        { label: 'Reviews', to: '/provider/reviews', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>' },
        { label: 'Earnings', to: '/provider/earnings', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>' },
        { label: 'Completed Jobs', to: '/provider/completed-jobs', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>' },
        { label: 'Payouts', to: '/provider/payouts', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg>' },
      ]
    },
    {
      label: 'Account',
      items: [
        { label: 'Customer History', to: '/provider/customer-history', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>' },
        { label: 'Profile', to: '/provider/profile', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>' },
        { label: 'Settings', to: '/provider/settings', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>' },
        { label: 'Help & Support', to: '/provider/help', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>' },
      ]
    },
  ],
  security: [
    {
      label: 'Main',
      items: [
        { label: 'Dashboard', to: '/security/dashboard', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>' },
        { label: 'Visitor Entry', to: '/security/visitor-entry', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><polyline points="17 11 19 13 23 9"></polyline></svg>' },
        { label: 'Visitor Approval', to: '/security/visitor-approval', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><line x1="18" y1="8" x2="23" y2="13"></line><line x1="23" y1="8" x2="18" y2="13"></line></svg>', badge: 3 },
      ]
    },
    {
      label: 'Monitoring',
      items: [
        { label: 'Parking Monitor', to: '/security/parking', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>' },
        { label: 'Vehicle Logs', to: '/security/vehicles', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>' },
        { label: 'Patrol Log', to: '/security/patrol', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>' },
      ]
    },
    {
      label: 'Alerts',
      items: [
        { label: 'Emergency Alerts', to: '/security/emergency', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>' },
        { label: 'Incident Reports', to: '/security/incidents', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>' },
      ]
    },
  ],
}

const sidebarItems = computed(() => sidebarConfigs[props.sidebarType] || sidebarConfigs.resident)
</script>

<style scoped>
.portal-layout {
  display: flex;
  min-height: 100vh;
  background: var(--color-background);
}

/* ── Sidebar ── */
.sidebar {
  width: var(--sidebar-width);
  background: var(--color-surface);
  border-right: 1px solid var(--color-border);
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  z-index: var(--z-sticky);
  transition: width var(--transition-base);
  overflow-y: auto;
  overflow-x: hidden;
}

.sidebar.collapsed {
  width: var(--sidebar-collapsed-width);
}

.sidebar-header {
  padding: var(--space-5) var(--space-4);
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--color-border);
  flex-shrink: 0;
}

.sidebar-logo {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  text-decoration: none;
}

.sidebar-logo .logo-icon {
  width: 34px;
  height: 34px;
  background: var(--color-primary);
  color: white;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.sidebar-logo .logo-text {
  font-family: var(--font-heading);
  font-size: var(--text-lg);
  font-weight: var(--font-bold);
  color: var(--color-primary);
  white-space: nowrap;
}

.sidebar-collapse-btn {
  background: none;
  color: var(--color-text-muted);
  padding: var(--space-1);
  border-radius: var(--radius-sm);
}

.sidebar-collapse-btn:hover {
  background: var(--color-gray-100);
  color: var(--color-text-primary);
}

/* ── Sidebar Nav ── */
.sidebar-nav {
  flex: 1;
  padding: var(--space-3);
  overflow-y: auto;
}

.nav-group {
  margin-bottom: var(--space-2);
}

.nav-group-label {
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: var(--space-3) var(--space-3) var(--space-2);
}

.nav-item {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--color-text-secondary);
  border-radius: var(--radius-md);
  text-decoration: none;
  transition: all var(--transition-fast);
  cursor: pointer;
  border: none;
  background: none;
  width: 100%;
  text-align: left;
}

.nav-item:hover {
  background: var(--color-gray-50);
  color: var(--color-text-primary);
}

.nav-item.active {
  background: var(--color-primary-50);
  color: var(--color-primary);
}

.nav-item.active .nav-icon {
  color: var(--color-primary);
}

.nav-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  color: var(--color-text-muted);
}

.nav-label {
  white-space: nowrap;
  flex: 1;
}

.nav-badge {
  background: var(--color-danger);
  color: white;
  font-size: 10px;
  font-weight: var(--font-bold);
  padding: 1px 6px;
  border-radius: var(--radius-full);
  line-height: 1.4;
}

/* ── Sidebar Footer ── */
.sidebar-footer {
  padding: var(--space-3);
  border-top: 1px solid var(--color-border);
  flex-shrink: 0;
}

.sidebar-user {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3);
  margin-bottom: var(--space-2);
}

.sidebar-user .avatar {
  flex-shrink: 0;
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
  background: var(--color-danger-50) !important;
  color: var(--color-danger) !important;
}

/* ── Main Content ── */
.portal-main {
  flex: 1;
  margin-left: var(--sidebar-width);
  transition: margin-left var(--transition-base);
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.portal-main.sidebar-collapsed {
  margin-left: var(--sidebar-collapsed-width);
}

/* ── Top Bar ── */
.topbar {
  height: var(--topbar-height);
  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 var(--space-6);
  position: sticky;
  top: 0;
  z-index: calc(var(--z-sticky) - 1);
}

.topbar-left {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.topbar-right {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.mobile-menu-btn,
.expand-btn {
  display: none;
  background: none;
  color: var(--color-text-secondary);
  padding: var(--space-2);
  border-radius: var(--radius-md);
}

.expand-btn {
  display: flex;
}

.topbar-icon-btn {
  position: relative;
  background: none;
  color: var(--color-text-secondary);
  padding: var(--space-2);
  border-radius: var(--radius-md);
}

.topbar-icon-btn:hover {
  background: var(--color-gray-100);
  color: var(--color-text-primary);
}

.notif-dot {
  position: absolute;
  top: 6px;
  right: 6px;
  width: 8px;
  height: 8px;
  background: var(--color-danger);
  border-radius: var(--radius-full);
  border: 2px solid var(--color-surface);
}

.topbar-user {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  cursor: pointer;
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  transition: background var(--transition-fast);
}

.topbar-user:hover {
  background: var(--color-gray-50);
}

.topbar-user .avatar {
  flex-shrink: 0;
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

/* ── Portal Content ── */
.portal-content {
  flex: 1;
  padding: var(--space-6);
}

/* ── Overlay ── */
.sidebar-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  z-index: calc(var(--z-sticky) - 1);
}

/* ── Responsive ── */
@media (max-width: 1024px) {
  .sidebar {
    transform: translateX(-100%);
  }

  .sidebar.mobile-open {
    transform: translateX(0);
  }

  .portal-main {
    margin-left: 0;
  }

  .portal-main.sidebar-collapsed {
    margin-left: 0;
  }

  .mobile-menu-btn {
    display: flex;
  }

  .expand-btn {
    display: none;
  }
}

@media (max-width: 768px) {
  .portal-content {
    padding: var(--space-4);
  }

  .hide-mobile {
    display: none !important;
  }
}
</style>
