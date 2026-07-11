<template>
  <div class="dashboard">
    <div class="page-title-row"><h1>Good Morning, Priya! 👋</h1><p class="subtitle">Here's what's happening in your society today</p></div>
    <div class="stats-grid">
      <div v-for="s in stats" :key="s.label" class="stat-card" @click="$router.push(s.to)">
        <div class="stat-icon" :style="{ background: s.bg, color: s.color }">{{ s.icon }}</div>
        <div class="stat-content"><div class="stat-value">{{ s.value }}</div><div class="stat-label">{{ s.label }}</div><a class="stat-link">View all →</a></div>
      </div>
    </div>
    <div class="dashboard-grid">
      <div class="card">
        <div class="card-header"><span class="card-title">Upcoming Events</span><router-link to="/resident/events" class="text-link">View All</router-link></div>
        <div v-for="e in events.slice(0,3)" :key="e.id" class="event-item">
          <div class="event-dot" :style="{ background: e.category === 'Wellness' ? 'var(--color-secondary)' : e.category === 'Health' ? 'var(--color-danger)' : 'var(--color-primary)' }"></div>
          <div class="event-info"><strong>{{ e.title }}</strong><span class="event-meta">📅 {{ e.date }}, {{ e.time }} · {{ e.venue }}</span></div>
          <button class="btn btn-primary btn-sm">Join</button>
        </div>
      </div>
      <div class="card">
        <div class="card-header"><span class="card-title">Recent Notices</span><router-link to="/resident/notices" class="text-link">View All</router-link></div>
        <div v-for="n in notices.slice(0,4)" :key="n.id" class="notice-item">
          <div class="notice-info"><strong>{{ n.title }}</strong><span class="notice-date">{{ n.date }}</span></div>
        </div>
      </div>
    </div>
    <div class="card quick-actions-card">
      <div class="card-header"><span class="card-title">Quick Actions</span></div>
      <div class="quick-grid">
        <button v-for="a in actions" :key="a.label" class="quick-action" @click="$router.push(a.to)">
          <span class="qa-icon" :style="{ background: a.bg }">{{ a.icon }}</span>
          <span>{{ a.label }}</span>
        </button>
      </div>
    </div>
  </div>
</template>
<script setup>
import { events, notices } from '@/data/mockData'
const stats = [
  { icon: '📋', label: 'My Complaints', value: 3, bg: 'var(--color-primary-100)', color: 'var(--color-primary)', to: '/resident/complaints' },
  { icon: '📅', label: 'My Bookings', value: 4, bg: 'var(--color-secondary-100)', color: 'var(--color-secondary)', to: '/resident/my-bookings' },
  { icon: '🎉', label: 'Upcoming Events', value: 5, bg: 'var(--color-accent-100)', color: 'var(--color-accent)', to: '/resident/events' },
  { icon: '🔔', label: 'New Notices', value: 7, bg: 'var(--color-info-100)', color: 'var(--color-info)', to: '/resident/notices' },
]
const actions = [
  { icon: '📝', label: 'Raise Complaint', to: '/resident/complaints/new', bg: 'var(--color-primary-100)' },
  { icon: '🔍', label: 'Browse Services', to: '/resident/services', bg: 'var(--color-secondary-100)' },
  { icon: '🅿️', label: 'Parking', to: '/resident/parking', bg: 'var(--color-accent-100)' },
  { icon: '👨‍👩‍👧‍👦', label: 'My Family', to: '/resident/family', bg: 'var(--color-info-100)' },
]
</script>
<style scoped>
.page-title-row { margin-bottom: var(--space-6); }
.page-title-row h1 { font-size: var(--text-2xl); }
.subtitle { color: var(--color-text-secondary); font-size: var(--text-sm); margin-top: var(--space-1); }
.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-5); margin-bottom: var(--space-6); }
.stat-card { cursor: pointer; }
.stat-link { font-size: var(--text-xs); color: var(--color-primary); margin-top: var(--space-1); display: inline-block; }
.dashboard-grid { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-6); margin-bottom: var(--space-6); }
.text-link { font-size: var(--text-sm); color: var(--color-primary); text-decoration: none; }
.event-item { display: flex; align-items: center; gap: var(--space-3); padding: var(--space-3) 0; border-bottom: 1px solid var(--color-border); }
.event-item:last-child { border-bottom: none; }
.event-dot { width: 8px; height: 8px; border-radius: var(--radius-full); flex-shrink: 0; }
.event-info { flex: 1; }
.event-info strong { font-size: var(--text-sm); display: block; }
.event-meta { font-size: var(--text-xs); color: var(--color-text-muted); }
.notice-item { padding: var(--space-3) 0; border-bottom: 1px solid var(--color-border); }
.notice-item:last-child { border-bottom: none; }
.notice-info { display: flex; justify-content: space-between; align-items: center; }
.notice-info strong { font-size: var(--text-sm); }
.notice-date { font-size: var(--text-xs); color: var(--color-text-muted); }
.quick-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-4); }
.quick-action { display: flex; flex-direction: column; align-items: center; gap: var(--space-2); padding: var(--space-4); border: 1px solid var(--color-border); border-radius: var(--radius-md); background: var(--color-surface); font-size: var(--text-sm); font-weight: var(--font-medium); color: var(--color-text-primary); cursor: pointer; transition: all var(--transition-fast); }
.quick-action:hover { box-shadow: var(--shadow-md); transform: translateY(-2px); }
.qa-icon { width: 40px; height: 40px; border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center; font-size: 1.25rem; }
@media (max-width: 1024px) { .stats-grid { grid-template-columns: repeat(2, 1fr); } .dashboard-grid { grid-template-columns: 1fr; } }
@media (max-width: 768px) { .quick-grid { grid-template-columns: repeat(2, 1fr); } }
</style>
