<template>
  <div class="public-layout">
    <!-- Header -->
    <header class="public-header">
      <div class="header-container">
        <router-link to="/" class="logo">
          <div class="logo-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
              <polyline points="9 22 9 12 15 12 15 22"></polyline>
            </svg>
          </div>
          <span class="logo-text">SocioNeed</span>
        </router-link>

        <nav class="header-nav" :class="{ active: mobileMenuOpen }">
          <router-link to="/" class="nav-link" @click="mobileMenuOpen = false">Home</router-link>
          <router-link to="/about" class="nav-link" @click="mobileMenuOpen = false">About Us</router-link>
          <router-link to="/services" class="nav-link" @click="mobileMenuOpen = false">Services</router-link>
          <router-link to="/how-it-works" class="nav-link" @click="mobileMenuOpen = false">How It Works</router-link>
          <router-link to="/contact" class="nav-link" @click="mobileMenuOpen = false">Contact</router-link>
        </nav>

        <div class="header-actions">
          <button
            type="button"
            class="theme-toggle"
            :aria-label="theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'"
            @click="toggleTheme"
          >
            <svg v-if="theme === 'dark'" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="4"></circle>
              <path d="M12 2v2"></path>
              <path d="M12 20v2"></path>
              <path d="m4.93 4.93 1.41 1.41"></path>
              <path d="m17.66 17.66 1.41 1.41"></path>
              <path d="M2 12h2"></path>
              <path d="M20 12h2"></path>
              <path d="m6.34 17.66-1.41 1.41"></path>
              <path d="m19.07 4.93-1.41 1.41"></path>
            </svg>
            <svg v-else width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"></path>
            </svg>
          </button>
          <router-link to="/login" class="btn btn-outline btn-sm">Login</router-link>
          <router-link to="/register" class="btn btn-primary btn-sm">Register</router-link>
          <button class="mobile-toggle" @click="mobileMenuOpen = !mobileMenuOpen">
            <svg v-if="!mobileMenuOpen" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="3" y1="12" x2="21" y2="12"></line>
              <line x1="3" y1="6" x2="21" y2="6"></line>
              <line x1="3" y1="18" x2="21" y2="18"></line>
            </svg>
            <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="public-main">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="public-footer">
      <div class="footer-container">
        <div class="footer-grid">
          <div class="footer-brand">
            <div class="logo">
              <div class="logo-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                  <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
              </div>
              <span class="logo-text">SocioNeed</span>
            </div>
            <p>Manage your society, services, and connections in one place.</p>
          </div>
          <div class="footer-links">
            <h4>Quick Links</h4>
            <router-link to="/">Home</router-link>
            <router-link to="/about">About Us</router-link>
            <router-link to="/services">Services</router-link>
            <router-link to="/contact">Contact</router-link>
          </div>
          <div class="footer-links">
            <h4>Portals</h4>
            <router-link to="/login">Resident Login</router-link>
            <router-link to="/login">Admin Login</router-link>
            <router-link to="/login">Service Provider</router-link>
            <router-link to="/login">Security</router-link>
          </div>
          <div class="footer-links">
            <h4>Contact</h4>
            <p>📧 support@socioneed.com</p>
            <p>📞 +91 98765 43210</p>
            <p>📍 Green Avenue Society, Sector 45, Noida</p>
          </div>
        </div>
        <div class="footer-meta">
          <div class="footer-legal">
            <span>&copy; 2026 SocioNeed</span>
            <span>Privacy Policy</span>
            <span>Terms</span>
            <router-link to="/contact">Support</router-link>
          </div>
          <div class="footer-socials" aria-label="Social links">
            <a href="https://www.linkedin.com" target="_blank" rel="noreferrer" aria-label="LinkedIn">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4V8h4v2"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
            </a>
            <a href="https://github.com" target="_blank" rel="noreferrer" aria-label="GitHub">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-4.5 1.5-4.5-2-6-2m12 4v-3.5c0-1 .1-1.5-.5-2 2-.2 4-1 4-4a3.1 3.1 0 0 0-.9-2.2 2.9 2.9 0 0 0-.1-2.2s-.8-.2-2.6 1a9 9 0 0 0-4.8 0c-1.8-1.2-2.6-1-2.6-1a2.9 2.9 0 0 0-.1 2.2A3.1 3.1 0 0 0 5 11c0 3 2 3.8 4 4-.6.5-.5 1.2-.5 2V21"></path></svg>
            </a>
            <a href="https://www.instagram.com" target="_blank" rel="noreferrer" aria-label="Instagram">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.5" y2="6.5"></line></svg>
            </a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { computed, onMounted, ref, watch } from 'vue'

const mobileMenuOpen = ref(false)
const theme = ref('light')

function applyTheme(nextTheme) {
  theme.value = nextTheme
  document.documentElement.dataset.theme = nextTheme
  localStorage.setItem('socioneed-theme', nextTheme)
}

function toggleTheme() {
  applyTheme(theme.value === 'dark' ? 'light' : 'dark')
}

onMounted(() => {
  const savedTheme = localStorage.getItem('socioneed-theme')
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
  applyTheme(savedTheme || (prefersDark ? 'dark' : 'light'))
})
</script>

<style scoped>
.public-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* ── Header ── */
.public-header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--color-border);
  height: var(--header-height);
}

.header-container {
  max-width: var(--max-content-width);
  margin: 0 auto;
  padding: 0 var(--space-6);
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  text-decoration: none;
  color: var(--color-text-primary);
}

.logo-icon {
  width: 36px;
  height: 36px;
  background: var(--color-primary);
  color: white;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-text {
  font-family: var(--font-heading);
  font-size: var(--text-xl);
  font-weight: var(--font-bold);
  color: var(--color-primary);
}

.header-nav {
  display: flex;
  align-items: center;
  gap: var(--space-1);
}

.nav-link {
  padding: var(--space-2) var(--space-4);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--color-text-secondary);
  border-radius: var(--radius-md);
  transition: all var(--transition-fast);
  text-decoration: none;
}

.nav-link:hover,
.nav-link.router-link-active {
  color: var(--color-primary);
  background: var(--color-primary-50);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.theme-toggle {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-md);
  border: 1px solid var(--color-border);
  background: var(--color-surface);
  color: var(--color-text-primary);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-xs);
}

.theme-toggle:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-sm);
}

.mobile-toggle {
  display: none;
  background: none;
  color: var(--color-text-primary);
  padding: var(--space-2);
}

/* ── Main ── */
.public-main {
  flex: 1;
}

/* ── Footer ── */
.public-footer {
  background: var(--color-gray-900);
  color: var(--color-gray-300);
  padding: var(--space-16) 0 0;
}

.footer-container {
  max-width: var(--max-content-width);
  margin: 0 auto;
  padding: 0 var(--space-6);
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1.5fr;
  gap: var(--space-10);
  padding-bottom: var(--space-10);
}

.footer-meta {
  border-top: 1px solid var(--color-gray-700);
  padding: var(--space-5) 0 var(--space-6);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  flex-wrap: wrap;
}

.footer-legal {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  flex-wrap: wrap;
}

.footer-legal span,
.footer-legal a {
  font-size: var(--text-sm);
  color: var(--color-gray-400);
}

.footer-legal a:hover {
  color: var(--color-text-inverse);
}

.footer-socials {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.footer-socials a {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-md);
  border: 1px solid var(--color-gray-700);
  color: var(--color-gray-300);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.footer-socials a:hover {
  color: var(--color-text-inverse);
  background: rgba(255, 255, 255, 0.06);
}

.footer-brand p {
  color: var(--color-gray-400);
  margin-top: var(--space-4);
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
}

.footer-brand .logo-icon {
  background: var(--color-primary);
}

.footer-brand .logo-text {
  color: var(--color-text-inverse);
}

.footer-links h4 {
  color: var(--color-text-inverse);
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
  margin-bottom: var(--space-4);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.footer-links a,
.footer-links p {
  display: block;
  color: var(--color-gray-400);
  font-size: var(--text-sm);
  margin-bottom: var(--space-3);
  text-decoration: none;
  transition: color var(--transition-fast);
}

.footer-links a:hover {
  color: var(--color-text-inverse);
}

.footer-bottom {
  border-top: 1px solid var(--color-gray-700);
  padding: var(--space-6) 0;
  text-align: center;
}

.footer-bottom p {
  font-size: var(--text-sm);
  color: var(--color-gray-500);
}

/* ── Responsive ── */
@media (max-width: 768px) {
  .header-nav {
    display: none;
    position: absolute;
    top: var(--header-height);
    left: 0;
    right: 0;
    background: var(--color-surface);
    flex-direction: column;
    padding: var(--space-4);
    border-bottom: 1px solid var(--color-border);
    box-shadow: var(--shadow-lg);
  }

  .header-nav.active {
    display: flex;
  }

  .header-actions .btn {
    display: none;
  }

  .mobile-toggle {
    display: flex;
  }

  .footer-grid {
    grid-template-columns: 1fr;
    gap: var(--space-8);
  }

  .footer-meta {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
