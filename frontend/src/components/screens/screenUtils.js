export function badgeClass(value) {
  const normalized = String(value || '').toLowerCase()

  if (['resolved', 'completed', 'active', 'confirmed', 'paid', 'available', 'approved', 'success'].some(token => normalized.includes(token))) {
    return 'badge-success'
  }

  if (['pending', 'upcoming', 'scheduled', 'reserved', 'blocked', 'waiting', 'draft'].some(token => normalized.includes(token))) {
    return 'badge-warning'
  }

  if (['cancelled', 'rejected', 'inactive', 'failed', 'closed'].some(token => normalized.includes(token))) {
    return 'badge-danger'
  }

  if (['in progress', 'assigned', 'inside', 'accepted', 'under investigation'].some(token => normalized.includes(token))) {
    return 'badge-info'
  }

  return 'badge-gray'
}

export function currency(value) {
  return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(Number(value || 0))
}

export function stars(rating) {
  const full = Math.round(Number(rating || 0))
  return Array.from({ length: 5 }, (_, index) => (index < full ? '★' : '☆'))
}

export function days(count) {
  return Array.from({ length: count }, (_, index) => index + 1)
}