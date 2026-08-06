<template>
  <div class="complaints-page">
    <div class="page-header-row"><h1>My Complaints</h1><router-link to="/resident/complaints/new" class="btn btn-primary">+ New Complaint</router-link></div>
    <div class="tabs"><button v-for="t in tabs" :key="t" class="tab" :class="{ active: activeTab === t }" @click="activeTab = t">{{ t }}</button></div>
    <div class="card table-card">
      <table class="data-table">
        <thead><tr><th>#</th><th>Title</th><th>Category</th><th>Status</th><th>Date</th></tr></thead>
        <tbody>
          <tr v-for="c in filtered" :key="c.id" @click="$router.push('/resident/complaints/' + c.id)" class="clickable-row">
            <td>{{ c.id }}</td><td>{{ c.title }}</td><td>{{ c.category }}</td>
            <td><span class="badge" :class="statusClass(c.status)">{{ c.status }}</span></td>
            <td>{{ c.date }}</td>
          </tr>
        </tbody>
      </table>
      <div v-if="!filtered.length" class="empty-state"><p>No complaints found</p></div>
    </div>
  </div>
</template>
<script setup>
import { ref, computed } from 'vue'
import { complaints } from '@/data/mockData'
const activeTab = ref('All')
const tabs = ['All', 'Pending', 'In Progress', 'Resolved']
const filtered = computed(() => activeTab.value === 'All' ? complaints : complaints.filter(c => c.status === activeTab.value))
function statusClass(s) { return s === 'In Progress' ? 'badge-warning' : s === 'Pending' ? 'badge-info' : s === 'Resolved' ? 'badge-success' : 'badge-danger' }
</script>
<style scoped>
.page-header-row { display: flex; align-items: center; justify-content: space-between; margin-bottom: var(--space-5); }
h1 { font-size: var(--text-2xl); }
.table-card { padding: 0; overflow: hidden; }
.table-card .data-table thead th:first-child, .table-card .data-table tbody td:first-child { padding-left: var(--space-6); }
.clickable-row { cursor: pointer; }
.clickable-row:hover { background: var(--color-primary-50) !important; }
</style>
