<template>
  <div class="login-page">
    <aside class="login-hero card">
      <router-link to="/" class="brand-link">
        <div class="logo-icon" aria-hidden="true">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
            <polyline points="9 22 9 12 15 12 15 22" />
          </svg>
        </div>
        <span>SocioNeed</span>
      </router-link>

      <div class="hero-copy">
        <p class="eyebrow">Welcome Back</p>
        <h1>Sign in to your community workspace</h1>
        <p>
          A calmer, cleaner login experience designed to feel like a premium SaaS product while keeping the same mocked auth flow.
        </p>
      </div>

      <div class="hero-surface" aria-hidden="true">
        <div class="city-card">
          <span class="city-card__label">Community status</span>
          <strong>All systems ready</strong>
          <div class="city-meter"><span></span></div>
        </div>
        <div class="login-city">
          <span class="tower tower-a"></span>
          <span class="tower tower-b"></span>
          <span class="tower tower-c"></span>
          <span class="tower tower-d"></span>
          <span class="person person-a"></span>
          <span class="person person-b"></span>
        </div>
      </div>
    </aside>

    <main class="login-panel">
      <div class="login-card card">
        <div class="login-header">
          <p class="eyebrow">Access Portal</p>
          <h2>Welcome Back!</h2>
          <p>Please login to your account</p>
        </div>

        <div class="role-tabs" role="tablist" aria-label="Select login role">
          <button
            v-for="r in roles"
            :key="r.key"
            type="button"
            class="role-tab"
            :class="{ active: selectedRole === r.key }"
            @click="selectedRole = r.key"
          >
            <span class="role-icon" v-html="r.icon"></span>
            <span>{{ r.label }}</span>
          </button>
        </div>

        <form class="login-form" @submit.prevent="handleLogin" novalidate>
          <div class="form-group">
            <label class="form-label">Email / Mobile Number</label>
            <div class="field-shell" :class="{ error: errors.email }">
              <span class="field-icon" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M4 4h16v16H4z" />
                  <path d="m4 7 8 5 8-5" />
                </svg>
              </span>
              <input
                v-model="email"
                type="text"
                class="form-input auth-input"
                :class="{ error: errors.email }"
                placeholder="Enter email or mobile number"
                autocomplete="username"
              />
            </div>
            <span v-if="errors.email" class="form-error">{{ errors.email }}</span>
          </div>

          <div class="form-group">
            <label class="form-label">Password</label>
            <div class="field-shell password-shell" :class="{ error: errors.password }">
              <span class="field-icon" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="11" width="18" height="10" rx="2" />
                  <path d="M7 11V8a5 5 0 0 1 10 0v3" />
                </svg>
              </span>
              <input
                v-model="password"
                :type="showPassword ? 'text' : 'password'"
                class="form-input auth-input"
                :class="{ error: errors.password }"
                placeholder="Enter password"
                autocomplete="current-password"
              />
              <button type="button" class="password-toggle" @click="showPassword = !showPassword" :aria-label="showPassword ? 'Hide password' : 'Show password'">
                <svg v-if="!showPassword" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                  <circle cx="12" cy="12" r="3" />
                </svg>
                <svg v-else width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24" />
                  <line x1="1" y1="1" x2="23" y2="23" />
                </svg>
              </button>
            </div>
            <span v-if="errors.password" class="form-error">{{ errors.password }}</span>
          </div>

          <div class="form-row">
            <label class="checkbox-label">
              <input type="checkbox" v-model="remember" />
              <span>Remember me</span>
            </label>
            <a href="#" class="forgot-link" @click.prevent="handleForgotPassword">Forgot Password?</a>
          </div>

          <span v-if="errors.general" class="form-error form-error-general">{{ errors.general }}</span>

          <button type="submit" class="btn btn-primary btn-lg login-button w-full" :disabled="isSubmitting">
            <span v-if="isSubmitting" class="button-spinner" aria-hidden="true"></span>
            <span>{{ isSubmitting ? 'Logging in...' : 'Login' }}</span>
          </button>
        </form>

        <p class="register-link">
          Don't have an account?
          <router-link to="/register">Register</router-link>
        </p>
      </div>
    </main>
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
  {
    key: 'resident',
    label: 'Resident',
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 20h18"></path><path d="M5 20V9l7-5 7 5v11"></path><path d="M9 20v-6h6v6"></path></svg>',
  },
  {
    key: 'admin',
    label: 'Admin',
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2 2 7l10 5 10-5-10-5z"></path><path d="M2 17l10 5 10-5"></path><path d="M2 12l10 5 10-5"></path></svg>',
  },
  {
    key: 'provider',
    label: 'Service Provider',
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16"></path><path d="M6 7v10a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V7"></path><path d="M9 11h6"></path></svg>',
  },
  {
    key: 'security',
    label: 'Security',
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>',
  },
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
  } else {
    const isEmail = /\S+@\S+\.\S+/.test(trimmedEmail)
    const isPhone = /^\+?[0-9]{8,15}$/.test(trimmedEmail)
    if (!isEmail && !isPhone) {
      errors.email = 'Enter a valid email or mobile number.'
    }
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

async function handleForgotPassword() {
  const identifier = window.prompt('Enter your registered email or mobile number:')
  if (!identifier) return

  const phone = window.prompt('Optional: enter your registered phone for extra verification (or leave empty):', '') || ''
  const newPassword = window.prompt('Enter your new password:')
  if (!newPassword) return

  try {
    await authStore.forgotPassword(identifier, newPassword, phone)
    notify.success('Password reset successful. Please login with your new password.')
  } catch (error) {
    notify.error(error instanceof Error ? error.message : 'Password reset failed. Please try again.')
  }
}
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  display: grid;
  grid-template-columns: minmax(320px, 0.95fr) minmax(380px, 1.05fr);
  background:
    radial-gradient(circle at top left, rgba(37, 99, 235, 0.12), transparent 32%),
    radial-gradient(circle at bottom right, rgba(59, 130, 246, 0.1), transparent 30%),
    var(--color-background);
}

.login-hero {
  position: relative;
  overflow: hidden;
  margin: var(--space-6);
  padding: var(--space-8);
  color: var(--color-text-inverse);
  background: linear-gradient(160deg, #1d4ed8 0%, #2563eb 46%, #0f172a 100%);
  border: none;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: calc(100vh - var(--space-12));
}

.login-hero::before,
.login-hero::after {
  content: '';
  position: absolute;
  border-radius: var(--radius-full);
  pointer-events: none;
}

.login-hero::before {
  inset: auto -10% 18% auto;
  width: 14rem;
  height: 14rem;
  background: rgba(255, 255, 255, 0.08);
  filter: blur(6px);
}

.login-hero::after {
  inset: 10% auto auto -8%;
  width: 12rem;
  height: 12rem;
  background: rgba(255, 255, 255, 0.05);
  filter: blur(10px);
}

.brand-link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-3);
  color: var(--color-text-inverse);
  text-decoration: none;
  font-size: var(--text-lg);
  font-weight: var(--font-semibold);
}

.logo-icon {
  width: 44px;
  height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-lg);
  background: rgba(255, 255, 255, 0.16);
  backdrop-filter: blur(10px);
}

.hero-copy {
  position: relative;
  z-index: 1;
  display: grid;
  gap: var(--space-4);
  max-width: 30rem;
}

.hero-copy h1 {
  color: var(--color-text-inverse);
  font-size: clamp(2.4rem, 4vw, 4rem);
  letter-spacing: -0.04em;
}

.hero-copy p {
  color: rgba(255, 255, 255, 0.82);
}

.hero-surface {
  position: relative;
  z-index: 1;
  min-height: 280px;
  margin-top: var(--space-8);
  border-radius: var(--radius-2xl);
  border: 1px solid rgba(255, 255, 255, 0.16);
  background: rgba(15, 23, 42, 0.2);
  backdrop-filter: blur(18px);
  overflow: hidden;
}

.city-card {
  position: absolute;
  top: var(--space-5);
  left: var(--space-5);
  display: grid;
  gap: var(--space-2);
  padding: var(--space-4) var(--space-5);
  border-radius: var(--radius-xl);
  background: rgba(255, 255, 255, 0.92);
  color: var(--color-text-primary);
  box-shadow: 0 18px 36px rgba(15, 23, 42, 0.18);
}

.city-card__label {
  font-size: var(--text-xs);
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.city-meter {
  width: 180px;
  height: 10px;
  border-radius: var(--radius-full);
  background: #e2e8f0;
  overflow: hidden;
}

.city-meter span {
  display: block;
  width: 82%;
  height: 100%;
  border-radius: inherit;
  background: linear-gradient(90deg, var(--color-primary), var(--color-primary-light));
}

.login-city {
  position: absolute;
  inset: auto 0 0;
  height: 210px;
}

.tower,
.person {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}

.tower {
  bottom: 0;
  border-radius: 20px 20px 0 0;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.18), rgba(255, 255, 255, 0.3));
  border: 1px solid rgba(255, 255, 255, 0.12);
}

.tower::before {
  content: '';
  position: absolute;
  inset: 10px;
  border-radius: 12px;
  background-image: linear-gradient(rgba(255, 255, 255, 0.6) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 0.6) 1px, transparent 1px);
  background-size: 14px 14px;
  opacity: 0.45;
}

.tower-a { width: 70px; height: 130px; left: 22%; }
.tower-b { width: 84px; height: 180px; left: 38%; }
.tower-c { width: 96px; height: 150px; left: 62%; }
.tower-d { width: 76px; height: 112px; left: 78%; }

.person {
  bottom: 34px;
  width: 18px;
  height: 58px;
  border-radius: 999px;
  background: linear-gradient(180deg, #dbeafe 0 14px, transparent 14px 20px, #ffffff 20px 38px, #dbeafe 38px 100%);
}

.person::before,
.person::after {
  content: '';
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  border-radius: var(--radius-full);
}

.person::before {
  top: -10px;
  width: 12px;
  height: 12px;
  background: rgba(255, 255, 255, 0.9);
}

.person::after {
  bottom: -12px;
  width: 4px;
  height: 14px;
  background: rgba(255, 255, 255, 0.8);
}

.person-a { left: 46%; }
.person-b { left: 64%; }

.login-panel {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-8);
}

.login-card {
  width: min(100%, 520px);
  padding: clamp(var(--space-6), 4vw, var(--space-10));
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(18px);
  border: 1px solid rgba(229, 231, 235, 0.9);
  box-shadow: var(--shadow-xl);
}

.login-header {
  display: grid;
  gap: var(--space-2);
  margin-bottom: var(--space-6);
}

.login-header h2 {
  font-size: clamp(1.8rem, 2.8vw, 2.4rem);
  letter-spacing: -0.03em;
}

.role-tabs {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: var(--space-3);
  margin-bottom: var(--space-6);
}

.role-tab {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  min-height: 48px;
  padding: var(--space-3) var(--space-4);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  background: var(--color-surface);
  color: var(--color-text-secondary);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  box-shadow: var(--shadow-xs);
}

.role-tab:hover {
  transform: translateY(-1px);
  border-color: var(--color-primary-100);
  color: var(--color-text-primary);
}

.role-tab.active {
  border-color: var(--color-primary-100);
  background: linear-gradient(135deg, var(--color-primary-50), rgba(255, 255, 255, 0.96));
  color: var(--color-primary);
  box-shadow: var(--shadow-sm);
}

.role-icon {
  width: 20px;
  height: 20px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.role-icon :deep(svg) {
  width: 20px;
  height: 20px;
}

.login-form {
  display: grid;
  gap: var(--space-2);
}

.field-shell {
  position: relative;
  display: flex;
  align-items: center;
  gap: var(--space-3);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  background: var(--color-surface);
  padding: 0 var(--space-4);
  box-shadow: var(--shadow-xs);
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast), transform var(--transition-fast);
}

.field-shell:focus-within {
  border-color: var(--color-primary-100);
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.1);
  transform: translateY(-1px);
  outline: none;
}

.field-shell.error {
  border-color: var(--color-danger);
  box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.1);
}

.field-icon {
  width: 18px;
  height: 18px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-muted);
  flex-shrink: 0;
}

.auth-input {
  border: none;
  background: transparent;
  padding-inline: 0;
  box-shadow: none;
  outline: none;
}

.auth-input:focus,
.auth-input:focus-visible {
  box-shadow: none;
  outline: none;
}

.password-shell input[type='password']::-ms-reveal,
.password-shell input[type='password']::-ms-clear,
.password-shell input[type='password']::-webkit-textfield-decoration-container {
  display: none;
}

.password-shell .auth-input {
  padding-right: 0;
}

.password-toggle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  margin-left: auto;
  border-radius: var(--radius-full);
  color: var(--color-text-muted);
  flex-shrink: 0;
}

.password-toggle:hover {
  color: var(--color-text-primary);
  background: var(--color-gray-100);
}

.form-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  margin: var(--space-2) 0 var(--space-4);
}

.checkbox-label {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  cursor: pointer;
}

.checkbox-label input {
  width: 16px;
  height: 16px;
  accent-color: var(--color-primary);
}

.forgot-link {
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
}

.form-error {
  display: block;
  margin-top: var(--space-2);
  font-size: var(--text-sm);
  color: var(--color-danger-dark);
}

.form-error-general {
  margin-top: 0;
  margin-bottom: var(--space-2);
}

.login-button {
  position: relative;
  overflow: hidden;
  margin-top: var(--space-2);
}

.login-button:disabled {
  opacity: 0.8;
}

.button-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.35);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}

.w-full {
  width: 100%;
}

.register-link {
  margin-top: var(--space-6);
  text-align: center;
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
}

.register-link a {
  font-weight: var(--font-semibold);
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: 1024px) {
  .login-page {
    grid-template-columns: 1fr;
  }

  .login-hero {
    margin-bottom: 0;
    min-height: auto;
  }
}

@media (max-width: 768px) {
  .login-hero,
  .login-panel {
    margin: 0;
    padding: var(--space-4);
  }

  .login-hero {
    min-height: auto;
  }

  .role-tabs {
    grid-template-columns: 1fr;
  }

  .form-row {
    flex-direction: column;
    align-items: flex-start;
  }

  .city-meter {
    width: 140px;
  }
}
</style>
