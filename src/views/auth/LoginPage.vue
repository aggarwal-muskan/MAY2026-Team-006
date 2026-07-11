<template>
  <div class="login-page">
    <div class="login-left">
      <div class="brand-panel">
        <router-link to="/" class="logo"><div class="logo-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div><span>SocioNeed</span></router-link>
        <div class="brand-content">
          <h2>Welcome Back!</h2>
          <p>Login to continue managing your community</p>
          <div class="brand-illustration">
            <div class="ill-buildings"><div class="ill-b" style="width:40px;height:120px"></div><div class="ill-b" style="width:50px;height:160px"></div><div class="ill-b" style="width:45px;height:140px"></div></div>
          </div>
        </div>
      </div>
    </div>
    <div class="login-right">
      <div class="login-form-wrapper">
        <h1>Welcome Back!</h1>
        <p class="login-subtitle">Please login to your account</p>
        <div class="role-tabs">
          <button v-for="r in roles" :key="r.key" type="button" class="role-tab" :class="{ active: selectedRole === r.key }" @click="selectedRole = r.key">
            <span class="role-icon">{{ r.icon }}</span>
            <span>{{ r.label }}</span>
          </button>
        </div>
        <form @submit.prevent="handleLogin" novalidate>
          <div class="form-group">
            <label class="form-label">Email / Mobile Number</label>
            <input v-model="email" type="text" class="form-input" :class="{ error: errors.email }" placeholder="Enter email or mobile number" />
            <span v-if="errors.email" class="form-error">{{ errors.email }}</span>
          </div>
          <div class="form-group">
            <label class="form-label">Password</label>
            <div class="password-field">
              <input v-model="password" :type="showPassword ? 'text' : 'password'" class="form-input" :class="{ error: errors.password }" placeholder="Enter password" />
              <button type="button" class="eye-btn" @click="showPassword = !showPassword">
                <svg v-if="!showPassword" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                <svg v-else width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg>
              </button>
            </div>
            <span v-if="errors.password" class="form-error">{{ errors.password }}</span>
          </div>
          <div class="form-row">
            <label class="checkbox-label"><input type="checkbox" v-model="remember" /> <span>Remember me</span></label>
            <a href="#" class="forgot-link">Forgot Password?</a>
          </div>
          <span v-if="errors.general" class="form-error form-error-general">{{ errors.general }}</span>
          <button type="submit" class="btn btn-primary btn-lg w-full" :disabled="isSubmitting">{{ isSubmitting ? 'Logging in...' : 'Login' }}</button>
        </form>
        <p class="register-link">Don't have an account? <router-link to="/register">Register</router-link></p>
      </div>
    </div>
  </div>
</template>
<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'
import { useNotificationStore } from '@/stores/notificationStore'

const router = useRouter()
const authStore = useAuthStore()
const notify = useNotificationStore()

const selectedRole = ref('resident')
const email = ref('')
const password = ref('')
const showPassword = ref(false)
const remember = ref(false)
const isSubmitting = ref(false)
const errors = reactive({
  email: '',
  password: '',
  general: '',
})

const roles = [
  { key: 'resident', label: 'Resident', icon: '🏠' },
  { key: 'admin', label: 'Admin', icon: '👨‍💼' },
  { key: 'provider', label: 'Service Provider', icon: '🔧' },
  { key: 'security', label: 'Security', icon: '🛡️' },
]

function clearErrors() {
  errors.email = ''
  errors.password = ''
  errors.general = ''
}

function validateForm() {
  clearErrors()

  const trimmedEmail = email.value.trim()
  if (!trimmedEmail) {
    errors.email = 'Email is required.'
  } else if (!/\S+@\S+\.\S+/.test(trimmedEmail)) {
    errors.email = 'Enter a valid email address.'
  }

  if (!password.value) {
    errors.password = 'Password is required.'
  }

  return !errors.email && !errors.password
}

async function handleLogin() {
  if (isSubmitting.value) return
  if (!validateForm()) return

  isSubmitting.value = true

  try {
    const result = await authStore.login(selectedRole.value, email.value, password.value)
    notify.success(`Welcome back! Logged in as ${selectedRole.value}`)
    router.push(result.dashboardRoute)
  } catch (error) {
    errors.general = error instanceof Error ? error.message : 'Unable to log in. Please try again.'
    notify.error(errors.general)
  } finally {
    isSubmitting.value = false
  }
}
</script>
<style scoped>
.login-page { display: flex; min-height: 100vh; width: 100%; }
.login-left { width: 45%; background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-info-dark) 100%); display: flex; align-items: center; justify-content: center; padding: var(--space-8); }
.brand-panel { color: white; text-align: center; }
.brand-panel .logo { display: flex; align-items: center; gap: var(--space-2); justify-content: center; margin-bottom: var(--space-10); text-decoration: none; }
.brand-panel .logo-icon { width: 40px; height: 40px; background: rgba(255,255,255,0.2); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center; color: white; }
.brand-panel .logo span { font-family: var(--font-heading); font-size: var(--text-2xl); font-weight: var(--font-bold); color: white; }
.brand-content h2 { font-size: var(--text-3xl); color: white; margin-bottom: var(--space-3); }
.brand-content p { color: rgba(255,255,255,0.8); font-size: var(--text-lg); }
.brand-illustration { margin-top: var(--space-10); }
.ill-buildings { display: flex; align-items: flex-end; justify-content: center; gap: 8px; }
.ill-b { background: rgba(255,255,255,0.15); border-radius: var(--radius-md) var(--radius-md) 0 0; }

.login-right { flex: 1; display: flex; align-items: center; justify-content: center; padding: var(--space-8); background: var(--color-background); }
.login-form-wrapper { width: 100%; max-width: 420px; }
.login-form-wrapper h1 { font-size: var(--text-2xl); margin-bottom: var(--space-2); }
.login-subtitle { color: var(--color-text-secondary); margin-bottom: var(--space-6); }

.role-tabs { display: grid; grid-template-columns: repeat(2, 1fr); gap: var(--space-3); margin-bottom: var(--space-6); }
.role-tab { display: flex; align-items: center; gap: var(--space-2); padding: var(--space-3) var(--space-4); border: 2px solid var(--color-border); border-radius: var(--radius-md); background: var(--color-surface); font-size: var(--text-sm); font-weight: var(--font-medium); color: var(--color-text-secondary); transition: all var(--transition-fast); cursor: pointer; }
.role-tab:hover { border-color: var(--color-primary-200); }
.role-tab.active { border-color: var(--color-primary); background: var(--color-primary-50); color: var(--color-primary); }
.role-icon { font-size: 1.25rem; }

.password-field { position: relative; }
.password-field input { padding-right: 44px; }
.form-input.error { border-color: var(--color-error, #dc2626); box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.12); }
.form-error { display: block; margin-top: var(--space-1); font-size: var(--text-sm); color: var(--color-error, #dc2626); }
.form-error-general { margin-top: 0; margin-bottom: var(--space-3); }
.eye-btn { position: absolute; right: 12px; top: 50%; transform: translateY(-50%); background: none; color: var(--color-text-muted); padding: 2px; }

.form-row { display: flex; align-items: center; justify-content: space-between; margin-bottom: var(--space-6); }
.checkbox-label { display: flex; align-items: center; gap: var(--space-2); font-size: var(--text-sm); color: var(--color-text-secondary); cursor: pointer; }
.checkbox-label input { width: 16px; height: 16px; accent-color: var(--color-primary); }
.forgot-link { font-size: var(--text-sm); color: var(--color-primary); }
.w-full { width: 100%; }
.w-full:disabled { opacity: 0.7; cursor: not-allowed; }
.register-link { text-align: center; margin-top: var(--space-6); font-size: var(--text-sm); color: var(--color-text-secondary); }
.register-link a { color: var(--color-primary); font-weight: var(--font-medium); }

@media (max-width: 768px) {
  .login-left { display: none; }
  .login-page { flex-direction: column; }
}
</style>
