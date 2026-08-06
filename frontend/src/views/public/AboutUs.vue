<template>
  <div class="about-page">
    <section class="page-header">
      <div class="container">
        <h1>About Our Society</h1>
        <p>Green Valley Society is a premium residential community providing top-notch amenities and services. We strive to create a safe, comfortable, and vibrant living environment for all our residents.</p>
      </div>
    </section>
    <section class="facilities-section">
      <div class="container">
        <h2>Our Facilities</h2>
        <div class="facilities-grid">
          <div v-for="f in facilities" :key="f.id" class="facility-card card card-hover">
            <span class="ficon">{{ f.icon }}</span>
            <h3>{{ f.name }}</h3>
            <p>{{ f.description }}</p>
          </div>
        </div>
      </div>
    </section>
    <section class="committee-section">
      <div class="container">
        <h2>Management Committee</h2>
        <div class="committee-grid">
          <div v-for="m in committeeMembers" :key="m.id" class="member-card card">
            <div class="avatar avatar-xl">{{ m.name.split(' ').map(n=>n[0]).join('') }}</div>
            <h4>{{ m.name }}</h4>
            <p class="role">{{ m.role }}</p>
            <p class="phone">📞 {{ m.phone }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script setup>
import { facilities, committeeMembers } from '@/data/mockData'
</script>
<style scoped>
.container { max-width: var(--max-content-width); margin: 0 auto; padding: 0 var(--space-6); }
.page-header { padding: var(--space-16) 0; background: linear-gradient(135deg, var(--color-primary-50), var(--color-info-50)); text-align: center; }
.page-header h1 { font-size: var(--text-4xl); margin-bottom: var(--space-4); }
.page-header p { font-size: var(--text-lg); color: var(--color-text-secondary); max-width: 700px; margin: 0 auto; line-height: var(--leading-relaxed); }
.facilities-section, .committee-section { padding: var(--space-16) 0; }
.facilities-section h2, .committee-section h2 { text-align: center; margin-bottom: var(--space-10); }
.facilities-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-6); }
.facility-card { text-align: center; padding: var(--space-8) var(--space-4); }
.ficon { font-size: 2.5rem; display: block; margin-bottom: var(--space-4); }
.facility-card h3 { font-size: var(--text-base); margin-bottom: var(--space-2); }
.facility-card p { font-size: var(--text-sm); color: var(--color-text-secondary); }
.committee-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: var(--space-6); }
.member-card { text-align: center; padding: var(--space-6); }
.member-card h4 { margin-top: var(--space-3); font-size: var(--text-sm); }
.role { font-size: var(--text-xs); color: var(--color-primary); font-weight: var(--font-medium); margin-top: var(--space-1); }
.phone { font-size: var(--text-xs); color: var(--color-text-muted); margin-top: var(--space-2); }
@media (max-width: 768px) { .facilities-grid { grid-template-columns: 1fr 1fr; } .committee-grid { grid-template-columns: 1fr 1fr; } }
</style>
