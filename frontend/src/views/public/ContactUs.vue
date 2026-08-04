<template>
  <div class="contact-page">
    <section class="page-header"><div class="container"><h1>Contact Us</h1><p>We are here to help and answer any questions you might have</p></div></section>
    <section class="contact-section"><div class="container">
      <div class="contact-grid">
        <div class="contact-info">
          <h2>Get In Touch</h2>
          <div class="info-item"><span class="info-icon">📞</span><div><strong>Phone</strong><p>+91 98765 43210</p></div></div>
          <div class="info-item"><span class="info-icon">📧</span><div><strong>Email</strong><p>support@socioneed.com</p></div></div>
          <div class="info-item"><span class="info-icon">📍</span><div><strong>Address</strong><p>Green Avenue Society, Sector 45, Noida, UP 201301</p></div></div>
          <div class="map-placeholder"><div class="map-inner">📍 Green Avenue Society, Sector 45, Noida</div></div>
        </div>
        <div class="contact-form card">
          <h2>Send Message</h2>
          <form @submit.prevent="submitForm">
            <div class="form-group"><label class="form-label">Your Name</label><input v-model="form.name" class="form-input" placeholder="Enter your name" required /></div>
            <div class="form-group"><label class="form-label">Email Address</label><input v-model="form.email" type="email" class="form-input" placeholder="Enter your email" required /></div>
            <div class="form-group"><label class="form-label">Subject</label><input v-model="form.subject" class="form-input" placeholder="Enter subject" required /></div>
            <div class="form-group"><label class="form-label">Message</label><textarea v-model="form.message" class="form-input" rows="5" placeholder="Write your message..." required></textarea></div>
            <button type="submit" class="btn btn-primary w-full">Send Message</button>
          </form>
        </div>
      </div>
    </div></section>
  </div>
</template>
<script setup>
import { reactive } from 'vue'
import { useNotificationStore } from '@/stores/notificationStore'
const notify = useNotificationStore()
const form = reactive({ name: '', email: '', subject: '', message: '' })
function submitForm() {
  notify.success('Message sent successfully! We will get back to you soon.')
  Object.assign(form, { name: '', email: '', subject: '', message: '' })
}
</script>
<style scoped>
.container { max-width: var(--max-content-width); margin: 0 auto; padding: 0 var(--space-6); }
.page-header { padding: var(--space-16) 0; background: linear-gradient(135deg, var(--color-primary-50), var(--color-info-50)); text-align: center; }
.page-header h1 { font-size: var(--text-4xl); margin-bottom: var(--space-3); }
.page-header p { color: var(--color-text-secondary); font-size: var(--text-lg); }
.contact-section { padding: var(--space-16) 0; }
.contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-10); }
.contact-info h2 { margin-bottom: var(--space-6); }
.info-item { display: flex; gap: var(--space-4); margin-bottom: var(--space-5); }
.info-icon { font-size: 1.5rem; }
.info-item strong { display: block; font-size: var(--text-sm); margin-bottom: var(--space-1); }
.info-item p { font-size: var(--text-sm); color: var(--color-text-secondary); margin: 0; }
.map-placeholder { margin-top: var(--space-6); background: var(--color-gray-100); border-radius: var(--radius-lg); height: 200px; display: flex; align-items: center; justify-content: center; border: 1px solid var(--color-border); }
.map-inner { color: var(--color-text-muted); font-size: var(--text-sm); }
.contact-form { padding: var(--space-8); }
.contact-form h2 { margin-bottom: var(--space-6); }
.w-full { width: 100%; }
@media (max-width: 768px) { .contact-grid { grid-template-columns: 1fr; } }
</style>
