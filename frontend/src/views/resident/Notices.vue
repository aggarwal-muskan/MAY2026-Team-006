<template>
  <div class="notices-page">
    <h1>Notice Board</h1>
    <div class="filters"><button v-for="c in categories" :key="c" class="btn btn-sm" :class="activeFilter === c ? 'btn-primary' : 'btn-ghost'" @click="activeFilter = c">{{ c }}</button></div>
    <div class="notices-list">
      <div v-for="n in filtered" :key="n.id" class="notice-card card">
        <div class="notice-header">
          <span class="badge" :class="priorityClass(n.priority)">{{ n.priority }}</span>
          <span class="badge badge-gray">{{ n.category }}</span>
          <span class="notice-date">{{ n.date }}</span>
        </div>
        <h3>{{ n.title }}</h3>
        <p>{{ n.content }}</p>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, computed } from 'vue'
import { notices } from '@/data/mockData'
const activeFilter = ref('All')
const categories = ['All', 'Maintenance', 'Event', 'Rules', 'Security', 'Finance', 'Safety']
const filtered = computed(() => activeFilter.value === 'All' ? notices : notices.filter(n => n.category === activeFilter.value))
function priorityClass(p) { return p === 'High' ? 'badge-danger' : p === 'Medium' ? 'badge-warning' : 'badge-info' }
</script>
<style scoped>
h1 { font-size: var(--text-2xl); margin-bottom: var(--space-5); }
.filters { display: flex; gap: var(--space-2); margin-bottom: var(--space-6); flex-wrap: wrap; }
.notices-list { display: flex; flex-direction: column; gap: var(--space-4); }
.notice-card { padding: var(--space-5); }
.notice-header { display: flex; align-items: center; gap: var(--space-3); margin-bottom: var(--space-3); }
.notice-date { margin-left: auto; font-size: var(--text-xs); color: var(--color-text-muted); }
.notice-card h3 { font-size: var(--text-base); margin-bottom: var(--space-2); }
.notice-card p { font-size: var(--text-sm); color: var(--color-text-secondary); line-height: var(--leading-relaxed); }
</style>
