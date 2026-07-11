<template>
  <div class="register-page">
    <div class="register-card card">
      <div class="register-header">
        <router-link to="/" class="logo"><div class="logo-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div><span>SocioNeed</span></router-link>
        <h1>Create Account</h1>
        <p>Join your community platform</p>
      </div>
      <form @submit.prevent="handleRegister">
        <div class="form-group"><label class="form-label">Full Name *</label><input v-model="form.name" class="form-input" :class="{ error: errors.name }" placeholder="Enter your full name" /><span v-if="errors.name" class="form-error">{{ errors.name }}</span></div>
        <div class="form-row-2">
          <div class="form-group"><label class="form-label">Email *</label><input v-model="form.email" type="email" class="form-input" :class="{ error: errors.email }" placeholder="Enter email" /><span v-if="errors.email" class="form-error">{{ errors.email }}</span></div>
          <div class="form-group"><label class="form-label">Mobile Number *</label><input v-model="form.phone" class="form-input" :class="{ error: errors.phone }" placeholder="Enter mobile number" /><span v-if="errors.phone" class="form-error">{{ errors.phone }}</span></div>
        </div>
        <div class="form-row-2">
          <div class="form-group"><label class="form-label">Password *</label><input v-model="form.password" type="password" class="form-input" :class="{ error: errors.password }" placeholder="Create password" /><span v-if="errors.password" class="form-error">{{ errors.password }}</span></div>
          <div class="form-group"><label class="form-label">Confirm Password *</label><input v-model="form.confirmPassword" type="password" class="form-input" :class="{ error: errors.confirmPassword }" placeholder="Confirm password" /><span v-if="errors.confirmPassword" class="form-error">{{ errors.confirmPassword }}</span></div>
        </div>
        <div class="form-group">
          <label class="form-label">Register As *</label>
          <div class="role-options">
            <label class="role-option" :class="{ active: form.role === 'resident' }"><input type="radio" v-model="form.role" value="resident" /><span class="role-icon">🏠</span><span>Resident</span></label>
            <label class="role-option" :class="{ active: form.role === 'provider' }"><input type="radio" v-model="form.role" value="provider" /><span class="role-icon">🔧</span><span>Service Provider</span></label>
          </div>
        </div>
        <div v-if="form.role === 'resident'" class="form-group"><label class="form-label">Flat Number *</label><input v-model="form.flat" class="form-input" placeholder="e.g., A-101" /></div>
        <div v-if="form.role === 'provider'" class="form-group">
          <label class="form-label">Service Category *</label>
          <select v-model="form.category" class="form-input">
            <option value="">Select category</option>
            <option v-for="c in categories" :key="c" :value="c">{{ c }}</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary btn-lg w-full">Submit Registration</button>
      </form>
      <p class="login-link">Already have an account? <router-link to="/login">Login</router-link></p>
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

const categories = ['Plumber', 'Electrician', 'House Maid', 'Laundry', 'Car Wash', 'Gardener', 'Tailor', 'Cook']
const form = reactive({ name: '', email: '', phone: '', password: '', confirmPassword: '', role: 'resident', flat: '', category: '' })
const errors = reactive({})

function validate() {
  Object.keys(errors).forEach(k => delete errors[k])
  if (!form.name) errors.name = 'Name is required'
  if (!form.email) errors.email = 'Email is required'
  else if (!/\S+@\S+\.\S+/.test(form.email)) errors.email = 'Invalid email'
  if (!form.phone) errors.phone = 'Mobile number is required'
  if (!form.password) errors.password = 'Password is required'
  else if (form.password.length < 6) errors.password = 'Min 6 characters'
  if (form.password !== form.confirmPassword) errors.confirmPassword = 'Passwords do not match'
  return Object.keys(errors).length === 0
}

function handleRegister() {
  if (!validate()) return
  authStore.register(form)
  notify.success('Registration successful! Welcome to SocioNeed.')
  const route = form.role === 'provider' ? '/provider/dashboard' : '/resident/dashboard'
  router.push(route)
}
</script>
<style scoped>
.register-page { min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: var(--space-8); background: linear-gradient(135deg, var(--color-primary-50), var(--color-background), var(--color-info-50)); }
.register-card { max-width: 560px; width: 100%; padding: var(--space-10); }
.register-header { text-align: center; margin-bottom: var(--space-8); }
.logo { display: inline-flex; align-items: center; gap: var(--space-2); text-decoration: none; margin-bottom: var(--space-6); }
.logo-icon { width: 36px; height: 36px; background: var(--color-primary); color: white; border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center; }
.logo span { font-family: var(--font-heading); font-size: var(--text-xl); font-weight: var(--font-bold); color: var(--color-primary); }
.register-header h1 { font-size: var(--text-2xl); margin-bottom: var(--space-2); }
.register-header p { color: var(--color-text-secondary); }
.form-row-2 { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); }
.role-options { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-3); }
.role-option { display: flex; align-items: center; gap: var(--space-2); padding: var(--space-3) var(--space-4); border: 2px solid var(--color-border); border-radius: var(--radius-md); cursor: pointer; transition: all var(--transition-fast); font-size: var(--text-sm); font-weight: var(--font-medium); }
.role-option:hover { border-color: var(--color-primary-200); }
.role-option.active { border-color: var(--color-primary); background: var(--color-primary-50); }
.role-option input { display: none; }
.role-icon { font-size: 1.25rem; }
.w-full { width: 100%; }
.login-link { text-align: center; margin-top: var(--space-6); font-size: var(--text-sm); color: var(--color-text-secondary); }
.login-link a { color: var(--color-primary); font-weight: var(--font-medium); }
@media (max-width: 480px) { .form-row-2 { grid-template-columns: 1fr; } }
</style>
