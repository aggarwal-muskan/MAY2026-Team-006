<template>
  <div id="socioneed-app">
    <!-- Toast Notifications -->
    <div class="toast-container" v-if="notificationStore.toasts.length">
      <div
        v-for="toast in notificationStore.toasts"
        :key="toast.id"
        class="toast"
        :class="'toast-' + toast.type"
      >
        <span class="toast-icon">
          <span v-if="toast.type === 'success'">✓</span>
          <span v-else-if="toast.type === 'error'">✕</span>
          <span v-else-if="toast.type === 'warning'">⚠</span>
          <span v-else>ℹ</span>
        </span>
        <span class="toast-message">{{ toast.message }}</span>
        <button class="toast-close" @click="notificationStore.removeToast(toast.id)">×</button>
      </div>
    </div>

    <!-- Public Layout -->
    <PublicLayout v-if="layout === 'public'">
      <router-view />
    </PublicLayout>

    <!-- Auth Layout (no header/sidebar) -->
    <div v-else-if="layout === 'auth'" class="auth-wrapper">
      <router-view />
    </div>

    <!-- Portal Layout (Resident / Provider / Security) -->
    <PortalLayout v-else-if="layout === 'portal'" :sidebar-type="route.meta.sidebar">
      <router-view />
    </PortalLayout>

    <!-- Admin Layout -->
    <AdminLayout v-else-if="layout === 'admin'">
      <router-view />
    </AdminLayout>

    <!-- Fallback -->
    <router-view v-else />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useNotificationStore } from '@/stores/notificationStore'
import PublicLayout from '@/layouts/PublicLayout.vue'
import PortalLayout from '@/layouts/PortalLayout.vue'
import AdminLayout from '@/layouts/AdminLayout.vue'

const route = useRoute()
const notificationStore = useNotificationStore()

const layout = computed(() => route.meta.layout || 'public')
</script>

<style>
.toast-container {
  position: fixed;
  top: var(--space-6);
  right: var(--space-6);
  z-index: var(--z-toast);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.toast {
  position: relative;
  min-width: 320px;
}

.toast-message {
  flex: 1;
  font-size: var(--text-sm);
}

.toast-close {
  background: none;
  border: none;
  font-size: 1.25rem;
  color: var(--color-text-muted);
  cursor: pointer;
  padding: 0;
  line-height: 1;
}

.toast-close:hover {
  color: var(--color-text-primary);
}

.toast-icon {
  font-size: var(--text-lg);
  line-height: 1;
}

.auth-wrapper {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--color-primary-50) 0%, var(--color-background) 50%, var(--color-info-50) 100%);
}
</style>
