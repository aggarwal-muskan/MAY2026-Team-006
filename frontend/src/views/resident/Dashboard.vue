<template>
  <div class="dashboard resident-dashboard">
    <div class="page-title-row hero-panel">
      <div>
        <p class="eyebrow">Resident Dashboard</p>
        <h1>Good Morning, Priya! 👋</h1>
        <p class="subtitle">Here's what's happening in your society today</p>
      </div>
      <div class="hero-badge">Active Resident</div>
    </div>
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
  { icon: '🎉', label: 'Events', to: '/resident/events', bg: 'var(--color-accent-100)' },
  { icon: '👨‍👩‍👧‍👦', label: 'My Family', to: '/resident/family', bg: 'var(--color-info-100)' },
]
</script>
<style scoped>
.resident-dashboard {
  display: grid;
  gap: var(--space-6);
}

.hero-panel {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  padding: var(--space-6);
  border: 1px solid rgba(37, 99, 235, 0.08);
  border-radius: var(--radius-2xl);
  background:
    radial-gradient(circle at top right, rgba(37, 99, 235, 0.12), transparent 28%),
    linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(248, 250, 252, 0.94));
  box-shadow: 0 24px 60px rgba(15, 23, 42, 0.08);
}

.hero-panel h1 {
  font-size: clamp(2rem, 3vw, 3rem);
  margin-bottom: var(--space-2);
}

.hero-panel .subtitle {
  margin-top: 0;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: var(--text-xs);
  color: var(--color-primary);
  font-weight: var(--font-bold);
  margin-bottom: var(--space-2);
}

.hero-badge {
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-full);
  background: rgba(37, 99, 235, 0.08);
  color: var(--color-primary);
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
  white-space: nowrap;
}

.page-title-row { margin-bottom: var(--space-6); }
.page-title-row h1 { font-size: var(--text-2xl); }
.subtitle { color: var(--color-text-secondary); font-size: var(--text-sm); margin-top: var(--space-1); }
.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-5); }
.stat-card {
  cursor: pointer;
  padding: var(--space-5);
  border-radius: var(--radius-xl);
  border: 1px solid rgba(229, 231, 235, 0.9);
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(248, 250, 252, 0.94));
  box-shadow: var(--shadow-sm);
  transition: transform var(--transition-base), box-shadow var(--transition-base);
}
.stat-card:hover { transform: translateY(-2px); box-shadow: 0 18px 36px rgba(15, 23, 42, 0.08); }
.stat-link { font-size: var(--text-xs); color: var(--color-primary); margin-top: var(--space-1); display: inline-block; }
.dashboard-grid { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-6); }
.text-link { font-size: var(--text-sm); color: var(--color-primary); text-decoration: none; }
.card {
  border: 1px solid rgba(229, 231, 235, 0.9);
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(248, 250, 252, 0.94));
  box-shadow: var(--shadow-sm);
}
.card-header { margin-bottom: var(--space-4); }
.event-item { display: flex; align-items: center; gap: var(--space-3); padding: var(--space-4) var(--space-5); border-bottom: 1px solid var(--color-border); }
.event-item:last-child { border-bottom: none; }
.event-dot { width: 8px; height: 8px; border-radius: var(--radius-full); flex-shrink: 0; }
.event-info { flex: 1; }
.event-info strong { font-size: var(--text-sm); display: block; }
.event-meta { font-size: var(--text-xs); color: var(--color-text-muted); }
.notice-item { padding: var(--space-4) var(--space-5); border-bottom: 1px solid var(--color-border); }
.notice-item:last-child { border-bottom: none; }
.notice-info { display: flex; justify-content: space-between; align-items: center; }
.notice-info strong { font-size: var(--text-sm); }
.notice-date { font-size: var(--text-xs); color: var(--color-text-muted); }
.quick-actions-card { margin-top: 0; }
.quick-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-4); }
.quick-action { display: flex; flex-direction: column; align-items: center; gap: var(--space-3); padding: var(--space-5); border: 1px solid rgba(229, 231, 235, 0.9); border-radius: var(--radius-xl); background: linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(248, 250, 252, 0.94)); font-size: var(--text-sm); font-weight: var(--font-semibold); color: var(--color-text-primary); cursor: pointer; transition: transform var(--transition-base), box-shadow var(--transition-base); }
.quick-action:hover { box-shadow: 0 18px 36px rgba(15, 23, 42, 0.08); transform: translateY(-2px); }
.qa-icon { width: 46px; height: 46px; border-radius: var(--radius-lg); display: flex; align-items: center; justify-content: center; font-size: 1.25rem; }
@media (max-width: 1024px) { .stats-grid { grid-template-columns: repeat(2, 1fr); } .dashboard-grid { grid-template-columns: 1fr; } .hero-panel { flex-direction: column; align-items: flex-start; } }
@media (max-width: 768px) { .quick-grid { grid-template-columns: repeat(2, 1fr); } }
</style>
