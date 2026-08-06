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

.public-header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  height: var(--header-height);
  border-bottom: 1px solid rgba(229, 231, 235, 0.8);
  background: rgba(248, 250, 252, 0.8);
  backdrop-filter: blur(18px);
  box-shadow: 0 12px 36px rgba(15, 23, 42, 0.06);
}

.header-container {
  max-width: var(--max-content-width);
  height: 100%;
  margin: 0 auto;
  padding: 0 var(--space-6);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-5);
}

.logo {
  display: inline-flex;
  align-items: center;
  gap: var(--space-3);
  color: var(--color-text-primary);
  text-decoration: none;
}

.logo-icon {
  width: 42px;
  height: 42px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-lg);
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light));
  color: white;
  box-shadow: 0 14px 30px rgba(37, 99, 235, 0.22);
  transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.logo:hover .logo-icon {
  transform: translateY(-1px) rotate(-4deg);
  box-shadow: 0 18px 34px rgba(37, 99, 235, 0.26);
}

.logo-text {
  font-size: 1.1rem;
  font-weight: var(--font-bold);
  letter-spacing: -0.02em;
}

.header-nav {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.nav-link {
  position: relative;
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-full);
  color: var(--color-text-secondary);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  transition: all var(--transition-fast);
}

.nav-link:hover,
.nav-link.router-link-active {
  color: var(--color-text-primary);
  background: var(--color-primary-50);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.theme-toggle {
  width: 42px;
  height: 42px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.9);
  box-shadow: var(--shadow-xs);
}

.theme-toggle:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-sm);
}

.mobile-toggle {
  display: none;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.9);
}

.public-main {
  flex: 1;
}

.public-footer {
  padding: var(--space-16) 0 0;
  color: rgba(226, 232, 240, 0.95);
  background:
    linear-gradient(180deg, rgba(15, 23, 42, 0.98), rgba(15, 23, 42, 1)),
    radial-gradient(circle at top, rgba(37, 99, 235, 0.18), transparent 40%);
}

.footer-container {
  max-width: var(--max-content-width);
  margin: 0 auto;
  padding: 0 var(--space-6);
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1.3fr;
  gap: var(--space-10);
  padding-bottom: var(--space-10);
}

.footer-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  flex-wrap: wrap;
  padding: var(--space-5) 0 var(--space-6);
  border-top: 1px solid rgba(148, 163, 184, 0.2);
}

.footer-legal {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--space-4);
}

.footer-legal span,
.footer-legal a {
  font-size: var(--text-sm);
  color: rgba(203, 213, 225, 0.8);
}

.footer-legal a:hover {
  color: white;
}

.footer-socials {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.footer-socials a {
  width: 38px;
  height: 38px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(148, 163, 184, 0.22);
  border-radius: var(--radius-md);
  color: rgba(226, 232, 240, 0.9);
  background: rgba(255, 255, 255, 0.02);
}

.footer-socials a:hover {
  color: white;
  background: rgba(255, 255, 255, 0.08);
}

.footer-brand p {
  margin-top: var(--space-4);
  color: rgba(203, 213, 225, 0.72);
  font-size: var(--text-sm);
}

.footer-brand .logo-text {
  color: white;
}

.footer-links h4 {
  margin-bottom: var(--space-4);
  color: white;
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.footer-links a,
.footer-links p {
  display: block;
  margin-bottom: var(--space-3);
  color: rgba(203, 213, 225, 0.8);
  font-size: var(--text-sm);
}

.footer-links a:hover {
  color: white;
}

.footer-bottom {
  padding: var(--space-6) 0;
  text-align: center;
  border-top: 1px solid rgba(148, 163, 184, 0.2);
}

.footer-bottom p {
  color: rgba(148, 163, 184, 0.8);
  font-size: var(--text-sm);
}

@media (max-width: 768px) {
  .header-container {
    padding-inline: var(--space-4);
  }

  .header-nav {
    position: absolute;
    top: var(--header-height);
    left: var(--space-4);
    right: var(--space-4);
    display: none;
    flex-direction: column;
    padding: var(--space-4);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-xl);
    background: rgba(255, 255, 255, 0.96);
    box-shadow: var(--shadow-lg);
  }

  .header-nav.active {
    display: flex;
  }

  .header-actions .btn {
    display: none;
  }

  .mobile-toggle {
    display: inline-flex;
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
