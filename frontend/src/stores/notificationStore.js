// ============================================
// SocioNeed — Notification Store (Pinia)
// ============================================
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useNotificationStore = defineStore('notification', () => {
  const toasts = ref([])
  let toastId = 0

  function showToast(message, type = 'info', duration = 4000) {
    const id = ++toastId
    toasts.value.push({ id, message, type })
    setTimeout(() => {
      removeToast(id)
    }, duration)
  }

  function removeToast(id) {
    toasts.value = toasts.value.filter(t => t.id !== id)
  }

  function success(message) { showToast(message, 'success') }
  function error(message) { showToast(message, 'error') }
  function warning(message) { showToast(message, 'warning') }
  function info(message) { showToast(message, 'info') }

  return { toasts, showToast, removeToast, success, error, warning, info }
})
