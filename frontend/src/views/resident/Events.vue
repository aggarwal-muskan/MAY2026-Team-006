<template>
  <div class="events-page">
    <h1>Upcoming Events</h1>
    <div class="events-grid">
      <div v-for="e in events" :key="e.id" class="event-card card card-hover">
        <div class="event-banner" :style="{ background: bannerColor(e.category) }"><span class="event-category">{{ e.category }}</span></div>
        <div class="event-body">
          <h3>{{ e.title }}</h3>
          <p class="event-meta">📅 {{ e.date }}, {{ e.time }}</p>
          <p class="event-meta">📍 {{ e.venue }}</p>
          <p class="event-desc">{{ e.description }}</p>
          <div class="event-footer">
            <span class="registered">{{ e.registered }}/{{ e.capacity }} registered</span>
            <button class="btn btn-primary btn-sm" @click="joinEvent(e)">{{ e.joined ? 'Joined ✓' : 'Join Event' }}</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { reactive } from 'vue'
import { events as rawEvents } from '@/data/mockData'
import { useNotificationStore } from '@/stores/notificationStore'
const notify = useNotificationStore()
const events = reactive(rawEvents.map(e => ({ ...e, joined: false })))
function bannerColor(cat) { const c = { Wellness: 'linear-gradient(135deg,#10B981,#34D399)', Health: 'linear-gradient(135deg,#EF4444,#F87171)', Festival: 'linear-gradient(135deg,#F59E0B,#FBBF24)', Sports: 'linear-gradient(135deg,#2563EB,#3B82F6)', Meeting: 'linear-gradient(135deg,#6366F1,#818CF8)' }; return c[cat] || c.Meeting }
function joinEvent(e) { e.joined = true; e.registered++; notify.success(`You've joined "${e.title}"!`) }
</script>
<style scoped>
h1 { font-size: var(--text-2xl); margin-bottom: var(--space-6); }
.events-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-6); }
.event-card { overflow: hidden; padding: 0; }
.event-banner { padding: var(--space-5) var(--space-5) var(--space-4); color: white; }
.event-category { font-size: var(--text-xs); font-weight: var(--font-semibold); background: rgba(255,255,255,0.2); padding: 2px 10px; border-radius: var(--radius-full); }
.event-body { padding: var(--space-5); }
.event-body h3 { font-size: var(--text-lg); margin-bottom: var(--space-2); }
.event-meta { font-size: var(--text-sm); color: var(--color-text-secondary); margin-bottom: var(--space-1); }
.event-desc { font-size: var(--text-sm); color: var(--color-text-secondary); margin-top: var(--space-3); margin-bottom: var(--space-4); line-height: var(--leading-relaxed); }
.event-footer { display: flex; align-items: center; justify-content: space-between; }
.registered { font-size: var(--text-xs); color: var(--color-text-muted); }
@media (max-width: 1024px) { .events-grid { grid-template-columns: 1fr 1fr; } }
@media (max-width: 768px) { .events-grid { grid-template-columns: 1fr; } }
</style>
