<template>
  <div class="how-page">
    <section class="page-header"><div class="container"><h1>How It Works</h1><p>Get started with SocioNeed in just 3 simple steps</p></div></section>
    <section class="steps-section"><div class="container">
      <div class="steps">
        <div v-for="(step, i) in steps" :key="i" class="step">
          <div class="step-number" :style="{ background: step.bg }">{{ i + 1 }}</div>
          <div class="step-content"><h3>{{ step.title }}</h3><p>{{ step.desc }}</p></div>
        </div>
      </div>
      <div class="cta-center"><router-link to="/register" class="btn btn-primary btn-lg">Get Started Now</router-link></div>
    </div></section>
  </div>
</template>
<script setup>
const steps = [
  { title: 'Register', desc: 'Create your account as a resident, admin, or service provider. Fill in your details and get verified.', bg: 'var(--color-primary)' },
  { title: 'Explore', desc: 'Browse services, notices, events, and community updates. Discover everything your society offers.', bg: 'var(--color-secondary)' },
  { title: 'Connect & Manage', desc: 'Book services, raise complaints, pay bills, and stay connected with your community.', bg: 'var(--color-accent)' },
]
</script>
<style scoped>
.container { max-width: var(--max-content-width); margin: 0 auto; padding: 0 var(--space-6); }
.page-header { padding: var(--space-16) 0; background: linear-gradient(135deg, var(--color-primary-50), var(--color-info-50)); text-align: center; }
.page-header h1 { font-size: var(--text-4xl); margin-bottom: var(--space-3); }
.page-header p { color: var(--color-text-secondary); font-size: var(--text-lg); }
.steps-section { padding: var(--space-20) 0; }
.steps { max-width: 600px; margin: 0 auto var(--space-12); position: relative; }
.steps::before { content: ''; position: absolute; left: 32px; top: 70px; bottom: 70px; width: 3px; background: var(--color-border); }
.step { display: flex; gap: var(--space-6); margin-bottom: var(--space-10); position: relative; }
.step-number { width: 64px; height: 64px; border-radius: var(--radius-full); color: white; font-size: var(--text-2xl); font-weight: var(--font-bold); display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-family: var(--font-heading); box-shadow: var(--shadow-md); z-index: 1; }
.step-content { padding-top: var(--space-3); }
.step-content h3 { font-size: var(--text-xl); margin-bottom: var(--space-2); }
.step-content p { color: var(--color-text-secondary); line-height: var(--leading-relaxed); }
.cta-center { text-align: center; }
</style>
