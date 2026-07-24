// ============================================
// SocioNeed — Auth Store (Pinia)
// ============================================
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const storedToken = localStorage.getItem('socioneed.token')
  const storedRole = localStorage.getItem('socioneed.role')
  const storedUserRaw = localStorage.getItem('socioneed.user')
  let storedUser = null
  try {
    storedUser = storedUserRaw ? JSON.parse(storedUserRaw) : null
  } catch {
    storedUser = null
  }

  const user = ref(storedUser)
  const role = ref(storedRole || null)
  const token = ref(storedToken || null)
  const isAuthenticated = ref(Boolean(storedToken))

  const apiBase = (import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:5000/api').replace(/\/$/, '')

  const dashboardRoutes = {
    resident: '/resident/dashboard',
    admin: '/admin/dashboard',
    provider: '/provider/dashboard',
    security: '/security/dashboard',
  }

  const frontendToBackendRole = {
    resident: 'owner',
    admin: 'admin',
    provider: 'service_provider',
    security: 'security',
  }

  const userInitials = computed(() => {
    if (!user.value?.name) return '?'
    return user.value.name.split(' ').map(n => n[0]).join('').toUpperCase()
  })

  function normalizeBackendUser(rawUser) {
    if (!rawUser) return null
    return {
      ...rawUser,
      name: rawUser.name || rawUser.full_name || '',
      flat: rawUser.flat || rawUser.unit_number || '',
      category: rawUser.category || rawUser.service_category || '',
    }
  }

  async function parseApiResponse(response) {
    const payload = await response.json().catch(() => ({}))
    if (!response.ok || payload?.success === false) {
      const message = payload?.error?.message || payload?.message || `Request failed with status ${response.status}`
      throw new Error(message)
    }
    return payload
  }

  function persistSession() {
    if (token.value) {
      localStorage.setItem('socioneed.token', token.value)
    } else {
      localStorage.removeItem('socioneed.token')
    }

    if (role.value) {
      localStorage.setItem('socioneed.role', role.value)
    } else {
      localStorage.removeItem('socioneed.role')
    }

    if (user.value) {
      localStorage.setItem('socioneed.user', JSON.stringify(user.value))
    } else {
      localStorage.removeItem('socioneed.user')
    }
  }

  async function authFetch(path, options = {}) {
    if (!token.value) {
      throw new Error('Please login first.')
    }

    const response = await fetch(`${apiBase}${path}`, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token.value}`,
        ...(options.headers || {}),
      },
    })

    return parseApiResponse(response)
  }

  async function login(selectedRole, email, password) {
    const backendRole = frontendToBackendRole[selectedRole]
    if (!backendRole) {
      throw new Error('Please select a valid role.')
    }

    const response = await fetch(`${apiBase}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: String(email || '').trim(),
        password: String(password || ''),
        role: backendRole,
      }),
    })

    const payload = await parseApiResponse(response)
    token.value = payload.data.token
    user.value = normalizeBackendUser(payload.data.user)
    role.value = selectedRole
    isAuthenticated.value = true
    persistSession()

    if (selectedRole === 'provider') {
      try {
        await ensureProviderProfile()
      } catch {
        // Non-blocking: provider can still access portal even if profile bootstrap fails.
      }
    }

    return {
      user: user.value,
      role: selectedRole,
      dashboardRoute: dashboardRoutes[selectedRole],
    }
  }

  function logout() {
    user.value = null
    role.value = null
    isAuthenticated.value = false
    token.value = null
    persistSession()
  }

  async function register(userData) {
    const selectedRole = userData.role
    const backendRole = frontendToBackendRole[selectedRole]
    if (!backendRole) {
      throw new Error('Please select a valid role.')
    }

    const registerResponse = await fetch(`${apiBase}/auth/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        full_name: String(userData.name || '').trim(),
        email: String(userData.email || '').trim(),
        phone: String(userData.phone || '').trim(),
        password: String(userData.password || ''),
        role: backendRole,
        society_id: 1,
      }),
    })

    await parseApiResponse(registerResponse)
    const loginResult = await login(selectedRole, userData.email, userData.password)

    if (selectedRole === 'provider') {
      try {
        await ensureProviderProfile(userData.category)
      } catch {
        // Non-blocking: provider can complete profile later from portal.
      }
    }

    return loginResult
  }

  async function fetchMe() {
    const payload = await authFetch('/users/me', { method: 'GET' })
    user.value = normalizeBackendUser(payload.data)
    isAuthenticated.value = true
    persistSession()
    return user.value
  }

  async function updateMe(updatePayload) {
    const payload = await authFetch('/users/me', {
      method: 'PUT',
      body: JSON.stringify(updatePayload || {}),
    })
    user.value = normalizeBackendUser(payload.data)
    persistSession()
    return user.value
  }

  async function listEvents() {
    const payload = await authFetch('/events', { method: 'GET' })
    return payload?.data?.items || []
  }

  async function listNotices(options = {}) {
    const payload = await authFetch('/notices', { method: 'GET' })
    const items = payload?.data?.items || []
    if (options.withMeta) {
      return {
        items,
        pagination: payload?.data?.pagination || null,
      }
    }
    return items
  }

  async function createNotice(noticePayload) {
    const payload = await authFetch('/notices', {
      method: 'POST',
      body: JSON.stringify(noticePayload || {}),
    })
    return payload?.data || null
  }

  async function deleteNotice(noticeId) {
    await authFetch(`/notices/${noticeId}`, { method: 'DELETE' })
    return true
  }

  async function createEvent(eventPayload) {
    const payload = await authFetch('/events', {
      method: 'POST',
      body: JSON.stringify(eventPayload || {}),
    })
    return payload?.data || null
  }

  async function deleteEvent(eventId) {
    await authFetch(`/events/${eventId}`, { method: 'DELETE' })
    return true
  }

  async function registerEvent(eventId) {
    await authFetch(`/events/${eventId}/register`, { method: 'POST' })
    return true
  }

  async function unregisterEvent(eventId) {
    await authFetch(`/events/${eventId}/unregister`, { method: 'POST' })
    return true
  }

  async function listComplaints(options = {}) {
    const payload = await authFetch('/complaints', { method: 'GET' })
    const items = payload?.data?.items || []
    if (options.withMeta) {
      return {
        items,
        pagination: payload?.data?.pagination || null,
      }
    }
    return items
  }

  async function getComplaint(complaintId) {
    const payload = await authFetch(`/complaints/${complaintId}`, { method: 'GET' })
    return payload?.data || null
  }

  async function createComplaint(complaintPayload) {
    const payload = await authFetch('/complaints', {
      method: 'POST',
      body: JSON.stringify(complaintPayload || {}),
    })
    return payload?.data || null
  }

  async function assignComplaint(complaintId, assignedToUserId, comment = 'Complaint assigned') {
    const payload = await authFetch(`/complaints/${complaintId}/assign`, {
      method: 'PUT',
      body: JSON.stringify({ assigned_to_user_id: assignedToUserId, comment }),
    })
    return payload?.data || null
  }

  async function listProviders(options = {}) {
    const payload = await authFetch('/providers', { method: 'GET' })
    const items = payload?.data?.items || []
    if (options.withMeta) {
      return {
        items,
        pagination: payload?.data?.pagination || null,
      }
    }
    return items
  }

  async function ensureProviderProfile(preferredCategoryName = '') {
    if (!token.value || role.value !== 'provider' || !user.value?.id) {
      return null
    }

    const providers = await listProviders()
    const existing = providers.find((item) => Number(item.user_id) === Number(user.value.id))
    if (existing) return existing

    const categories = await listServiceCategories()
    if (!categories.length) {
      throw new Error('No service categories configured yet.')
    }

    const preferredName = String(preferredCategoryName || '').trim().toLowerCase()
    const chosenCategory = preferredName
      ? categories.find((item) => String(item.name || '').trim().toLowerCase() === preferredName)
      : null

    const category = chosenCategory || categories[0]
    const payload = await authFetch('/providers', {
      method: 'POST',
      body: JSON.stringify({
        category_id: category.id,
        business_name: `${user.value.name || 'Community'} Services`,
        service_description: 'Registered service provider profile',
      }),
    })

    return payload?.data || null
  }

  async function listServiceCategories() {
    const payload = await authFetch('/service-categories', { method: 'GET' })
    return payload?.data || []
  }

  async function getProvider(providerId) {
    const payload = await authFetch(`/providers/${providerId}`, { method: 'GET' })
    return payload?.data || null
  }

  async function createBooking(bookingPayload) {
    const payload = await authFetch('/bookings', {
      method: 'POST',
      body: JSON.stringify(bookingPayload || {}),
    })
    return payload?.data || null
  }

  async function listBookings() {
    const payload = await authFetch('/bookings', { method: 'GET' })
    return payload?.data?.items || []
  }

  async function getMyProviderProfile() {
    if (!token.value || role.value !== 'provider' || !user.value?.id) {
      return null
    }

    const providersPayload = await listProviders()
    return providersPayload.find((item) => Number(item.user_id) === Number(user.value.id)) || null
  }

  async function updateProvider(providerId, providerPayload) {
    const payload = await authFetch(`/providers/${providerId}`, {
      method: 'PUT',
      body: JSON.stringify(providerPayload || {}),
    })
    return payload?.data || null
  }

  async function listProviderSlots(providerId, availableOnly = false) {
    const suffix = availableOnly ? '?available_only=true' : ''
    const payload = await authFetch(`/slots/${providerId}${suffix}`, { method: 'GET' })
    return payload?.data || []
  }

  async function createProviderSlot(slotPayload) {
    const payload = await authFetch('/slots', {
      method: 'POST',
      body: JSON.stringify(slotPayload || {}),
    })
    return payload?.data || null
  }

  async function deleteProviderSlot(slotId) {
    await authFetch(`/slots/${slotId}`, { method: 'DELETE' })
    return true
  }

  async function acceptBooking(bookingId) {
    const payload = await authFetch(`/bookings/${bookingId}/accept`, { method: 'PUT' })
    return payload?.data || null
  }

  async function declineBooking(bookingId) {
    const payload = await authFetch(`/bookings/${bookingId}/decline`, { method: 'PUT' })
    return payload?.data || null
  }

  async function completeBooking(bookingId) {
    const payload = await authFetch(`/bookings/${bookingId}/complete`, { method: 'PUT' })
    return payload?.data || null
  }

  async function listUsers(query = '') {
    const suffix = query ? `?${query}` : ''
    const payload = await authFetch(`/users${suffix}`, { method: 'GET' })
    return payload?.data?.items || []
  }

  async function getAdminDashboardStats() {
    const payload = await authFetch('/analytics/dashboard/admin', { method: 'GET' })
    return payload?.data?.stats || {}
  }

  async function getProviderDashboardStats() {
    const payload = await authFetch('/analytics/dashboard/provider', { method: 'GET' })
    return payload?.data?.stats || {}
  }

  async function getProviderEarnings(providerId) {
    const payload = await authFetch(`/providers/${providerId}/earnings`, { method: 'GET' })
    return payload?.data || {}
  }

  async function getProviderReviews(providerId) {
    const payload = await authFetch(`/providers/${providerId}/reviews`, { method: 'GET' })
    return payload?.data || []
  }

  async function getBookingsAnalytics() {
    const payload = await authFetch('/analytics/bookings', { method: 'GET' })
    return payload?.data?.status_breakdown || {}
  }

  async function forgotPassword(emailOrPhone, newPassword, phone = '') {
    const response = await fetch(`${apiBase}/auth/forgot-password`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: String(emailOrPhone || '').trim(),
        phone: String(phone || '').trim(),
        new_password: String(newPassword || ''),
      }),
    })

    await parseApiResponse(response)
    return true
  }

  return {
    user,
    role,
    isAuthenticated,
    token,
    userInitials,
    login,
    logout,
    register,
    forgotPassword,
    fetchMe,
    updateMe,
    listEvents,
    listNotices,
    createNotice,
    deleteNotice,
    createEvent,
    deleteEvent,
    registerEvent,
    unregisterEvent,
    listComplaints,
    getComplaint,
    createComplaint,
    assignComplaint,
    listProviders,
    listServiceCategories,
    getProvider,
    ensureProviderProfile,
    getMyProviderProfile,
    updateProvider,
    listProviderSlots,
    createProviderSlot,
    deleteProviderSlot,
    createBooking,
    listBookings,
    acceptBooking,
    declineBooking,
    completeBooking,
    listUsers,
    getAdminDashboardStats,
    getProviderDashboardStats,
    getProviderEarnings,
    getProviderReviews,
    getBookingsAnalytics,
  }
})
