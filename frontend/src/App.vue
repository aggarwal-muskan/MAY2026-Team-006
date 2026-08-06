<template>
  <div id="socioneed-app">
    <!-- Toast Notifications -->
    <TransitionGroup name="toast" tag="div" class="toast-container" v-if="notificationStore.toasts.length" aria-live="polite" aria-atomic="true">
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
    </TransitionGroup>

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
  max-width: min(92vw, 420px);
}

.toast {
  position: relative;
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  padding: var(--space-4);
  min-width: 320px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(16px);
  box-shadow: var(--shadow-lg);
}

.toast-message {
  flex: 1;
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
  color: var(--color-text-primary);
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
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: var(--radius-full);
  background: var(--color-primary-50);
  color: var(--color-primary);
  font-size: var(--text-lg);
  line-height: 1;
}

.toast-success .toast-icon {
  background: var(--color-secondary-50);
  color: var(--color-secondary-dark);
}

.toast-error .toast-icon {
  background: var(--color-danger-50);
  color: var(--color-danger-dark);
}

.toast-warning .toast-icon {
  background: var(--color-accent-50);
  color: var(--color-accent-dark);
}

.toast-info .toast-icon {
  background: var(--color-info-50);
  color: var(--color-info-dark);
}

.toast-enter-active,
.toast-leave-active {
  transition: transform var(--transition-base), opacity var(--transition-base);
}

.toast-enter-from,
.toast-leave-to {
  transform: translateY(-10px) scale(0.98);
  opacity: 0;
}

.auth-wrapper {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background:
    radial-gradient(circle at top left, rgba(37, 99, 235, 0.1), transparent 30%),
    radial-gradient(circle at bottom right, rgba(59, 130, 246, 0.1), transparent 24%),
    var(--color-background);
}
</style>
