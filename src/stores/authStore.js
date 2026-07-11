// ============================================
// SocioNeed — Auth Store (Pinia)
// ============================================
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { currentUser, adminUser, providerUser, securityUser } from '@/data/mockData'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const role = ref(null)
  const isAuthenticated = ref(false)

  const dashboardRoutes = {
    resident: '/resident/dashboard',
    admin: '/admin/dashboard',
    provider: '/provider/dashboard',
    security: '/security/dashboard',
  }

  const roleUsers = {
    resident: { ...currentUser, role: 'resident' },
    admin: { ...adminUser, role: 'admin' },
    provider: { ...providerUser, role: 'provider' },
    security: { ...securityUser, role: 'security' },
  }

  const userInitials = computed(() => {
    if (!user.value?.name) return '?'
    return user.value.name.split(' ').map(n => n[0]).join('').toUpperCase()
  })

  function normalizeEmail(email) {
    return String(email || '').trim().toLowerCase()
  }

  function getMatchingAccount(email) {
    const normalizedEmail = normalizeEmail(email)
    return Object.values(roleUsers).find(account => normalizeEmail(account.email) === normalizedEmail) || null
  }

  async function login(selectedRole, email, password) {
    const normalizedEmail = normalizeEmail(email)
    const normalizedPassword = String(password || '')

    const selectedAccount = roleUsers[selectedRole]
    if (!selectedAccount) {
      throw new Error('Please select a valid role.')
    }

    const matchingAccount = getMatchingAccount(normalizedEmail)
    if (!matchingAccount) {
      throw new Error('Invalid email or password.')
    }

    if (matchingAccount.role !== selectedRole) {
      throw new Error(`This account belongs to the ${matchingAccount.role} role. Please select the correct role.`)
    }

    if (normalizeEmail(selectedAccount.email) !== normalizedEmail || selectedAccount.password !== normalizedPassword) {
      throw new Error('Invalid email or password.')
    }

    await new Promise(resolve => setTimeout(resolve, 800))

    user.value = { ...selectedAccount }
    role.value = selectedRole
    isAuthenticated.value = true

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
  }

  function register(userData) {
    // Simulate registration
    user.value = { ...userData, id: Date.now() }
    role.value = userData.role
    isAuthenticated.value = true
    return true
  }

  return {
    user,
    role,
    isAuthenticated,
    userInitials,
    login,
    logout,
    register,
  }
})
