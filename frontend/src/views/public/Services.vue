<template>
  <div class="services-page">
    <section class="page-header"><div class="container"><h1>Our Services</h1><p>Find trusted professionals for all your home service needs</p></div></section>
    <section class="services-section"><div class="container">
      <div class="services-grid">
        <div v-for="s in serviceCategories" :key="s.id" class="service-card card card-hover" @click="$router.push('/login')">
          <span class="sicon">{{ s.icon }}</span>
          <h3>{{ s.name }}</h3>
          <p>{{ s.description }}</p>
          <span class="arrow">→</span>
        </div>
      </div>
      <div class="cta-center"><router-link to="/login" class="btn btn-primary btn-lg">View All Services</router-link></div>
    </div></section>
  </div>
</template>
<script setup>
import { serviceCategories } from '@/data/mockData'
</script>
<style scoped>
.container { max-width: var(--max-content-width); margin: 0 auto; padding: 0 var(--space-6); }
.page-header { padding: var(--space-16) 0; background: linear-gradient(135deg, var(--color-primary-50), var(--color-info-50)); text-align: center; }
.page-header h1 { font-size: var(--text-4xl); margin-bottom: var(--space-3); }
.page-header p { color: var(--color-text-secondary); font-size: var(--text-lg); }
.services-section { padding: var(--space-16) 0; }
.services-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-6); margin-bottom: var(--space-10); }
.service-card { text-align: center; padding: var(--space-8) var(--space-5); cursor: pointer; position: relative; }
.sicon { font-size: 2.5rem; display: block; margin-bottom: var(--space-4); }
.service-card h3 { font-size: var(--text-base); margin-bottom: var(--space-2); }
.service-card p { font-size: var(--text-sm); color: var(--color-text-secondary); }
.arrow { position: absolute; top: var(--space-4); right: var(--space-4); color: var(--color-primary); font-size: var(--text-lg); opacity: 0; transition: opacity var(--transition-fast); }
.service-card:hover .arrow { opacity: 1; }
.cta-center { text-align: center; }
@media (max-width: 768px) { .services-grid { grid-template-columns: 1fr 1fr; } }
</style>
