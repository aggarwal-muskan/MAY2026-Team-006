<template>
  <div class="landing-page">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-container">
        <div class="hero-content">
          <h1 class="hero-title">
            Smart Living,<br />
            <span class="gradient-text">Stronger Community</span>
          </h1>
          <p class="hero-subtitle">
            Manage your society, services, and connections in one place.
            SocioNeed brings residents and management together on one platform
            for a smarter and happier community.
          </p>
          <div class="hero-actions">
            <router-link to="/register" class="btn btn-primary btn-lg">Get Started</router-link>
            <router-link to="/about" class="btn btn-outline btn-lg">Learn More</router-link>
          </div>
          <div class="hero-stats">
            <div class="hero-stat"><span class="stat-num">250+</span><span class="stat-txt">Residents</span></div>
            <div class="hero-stat"><span class="stat-num">50+</span><span class="stat-txt">Services</span></div>
            <div class="hero-stat"><span class="stat-num">98%</span><span class="stat-txt">Satisfaction</span></div>
          </div>
        </div>
        <div class="hero-visual">
          <div class="buildings">
            <div class="building b1"></div>
            <div class="building b2"></div>
            <div class="building b3"></div>
            <div class="building b4"></div>
            <div class="building b5"></div>
          </div>
          <div class="trees">
            <div class="tree t1"></div>
            <div class="tree t2"></div>
            <div class="tree t3"></div>
          </div>
          <div class="floating-shapes">
            <div class="shape s1"></div>
            <div class="shape s2"></div>
            <div class="shape s3"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section class="services-section">
      <div class="section-container">
        <h2 class="section-title">Our Services</h2>
        <p class="section-subtitle">Everything you need to manage your community efficiently</p>
        <div class="services-grid">
          <button
            v-for="service in featureCards"
            :key="service.title"
            type="button"
            class="service-card card card-hover service-card-button"
          >
            <div class="service-icon" :style="{ background: service.bg }">{{ service.icon }}</div>
            <h3>{{ service.title }}</h3>
            <p>{{ service.desc }}</p>
          </button>
        </div>
      </div>
    </section>

    <!-- Facilities Section -->
    <section class="facilities-section">
      <div class="section-container">
        <h2 class="section-title">Our Facilities</h2>
        <div class="facilities-grid">
          <button v-for="f in facilities" :key="f.id" type="button" class="facility-item facility-button">
            <span class="facility-icon">{{ f.icon }}</span>
            <span class="facility-name">{{ f.name }}</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Committee Section -->
    <section class="committee-section">
      <div class="section-container">
        <h2 class="section-title">Management Committee</h2>
        <div class="committee-grid">
          <div v-for="m in committeeMembers" :key="m.id" class="member-card">
            <div class="avatar avatar-xl">{{ m.name.split(' ').map(n => n[0]).join('') }}</div>
            <h4>{{ m.name }}</h4>
            <p>{{ m.role }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="section-container">
        <div class="cta-card">
          <h2>Ready to Transform Your Community?</h2>
          <p>Join SocioNeed today and experience hassle-free society management.</p>
          <router-link to="/register" class="btn btn-primary btn-lg">Get Started Free</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { committeeMembers, facilities } from '@/data/mockData'

const featureCards = [
  { icon: '📢', title: 'Notices & Events', desc: 'Stay updated with society announcements, events, and important notices.', bg: 'var(--color-primary-100)' },
  { icon: '📅', title: 'Service Booking', desc: 'Book amenities and hire service providers with just a few clicks.', bg: 'var(--color-secondary-100)' },
  { icon: '📋', title: 'Complaint Management', desc: 'Report issues and track complaint resolution in real-time.', bg: 'var(--color-accent-100)' },
  { icon: '🅿️', title: 'Parking Tracking', desc: 'Manage parking slots, visitor parking, and vehicle tracking.', bg: 'var(--color-info-100)' },
]
</script>

<style scoped>
.landing-page { overflow-x: hidden; }

/* Hero */
.hero {
  background: linear-gradient(135deg, var(--color-primary-50) 0%, var(--color-surface) 40%, var(--color-info-50) 100%);
  padding: var(--space-20) 0 var(--space-16);
  position: relative;
  overflow: hidden;
}

.hero-container {
  max-width: var(--max-content-width);
  margin: 0 auto;
  padding: 0 var(--space-6);
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-12);
  align-items: center;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: var(--font-bold);
  line-height: 1.1;
  margin-bottom: var(--space-6);
}

.gradient-text {
  background: linear-gradient(135deg, var(--color-primary), var(--color-info));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: var(--text-lg);
  color: var(--color-text-secondary);
  line-height: var(--leading-relaxed);
  margin-bottom: var(--space-8);
  max-width: 500px;
}

.hero-actions { display: flex; gap: var(--space-4); margin-bottom: var(--space-10); }

.hero-stats { display: flex; gap: var(--space-10); }
.hero-stat { display: flex; flex-direction: column; }
.stat-num { font-size: var(--text-2xl); font-weight: var(--font-bold); color: var(--color-primary); font-family: var(--font-heading); }
.stat-txt { font-size: var(--text-sm); color: var(--color-text-muted); }

/* Buildings Illustration */
.hero-visual {
  position: relative;
  height: 400px;
}

.buildings {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: flex-end;
  gap: 12px;
}

.building {
  border-radius: var(--radius-md) var(--radius-md) 0 0;
  background: linear-gradient(180deg, var(--color-primary-200) 0%, var(--color-primary) 100%);
  position: relative;
}

.building::after {
  content: '';
  position: absolute;
  inset: 8px;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 12px,
    rgba(255,255,255,0.3) 12px,
    rgba(255,255,255,0.3) 14px
  ),
  repeating-linear-gradient(
    90deg,
    transparent,
    transparent 10px,
    rgba(255,255,255,0.3) 10px,
    rgba(255,255,255,0.3) 12px
  );
  border-radius: var(--radius-sm);
}

.b1 { width: 60px; height: 180px; opacity: 0.7; }
.b2 { width: 50px; height: 250px; background: linear-gradient(180deg, var(--color-info-100) 0%, var(--color-info) 100%); }
.b3 { width: 70px; height: 300px; }
.b4 { width: 55px; height: 220px; background: linear-gradient(180deg, var(--color-secondary-100) 0%, var(--color-secondary) 100%); }
.b5 { width: 45px; height: 160px; opacity: 0.7; }

.trees {
  position: absolute;
  bottom: 0;
  width: 100%;
  display: flex;
  justify-content: space-around;
}

.tree {
  width: 30px;
  height: 50px;
  background: var(--color-secondary);
  border-radius: 50% 50% 0 0;
  position: relative;
  opacity: 0.6;
}

.tree::after {
  content: '';
  position: absolute;
  bottom: -15px;
  left: 50%;
  transform: translateX(-50%);
  width: 6px;
  height: 15px;
  background: #8B6914;
  border-radius: 2px;
}

.t1 { left: 10%; }
.t2 { left: 70%; height: 40px; width: 25px; }
.t3 { left: 90%; height: 35px; width: 22px; }

.floating-shapes { position: absolute; inset: 0; }
.shape {
  position: absolute;
  border-radius: var(--radius-full);
  animation: float 6s ease-in-out infinite;
}
.s1 { width: 60px; height: 60px; background: var(--color-primary-100); top: 10%; right: 10%; }
.s2 { width: 40px; height: 40px; background: var(--color-accent-100); top: 40%; right: 30%; animation-delay: 2s; }
.s3 { width: 30px; height: 30px; background: var(--color-secondary-100); top: 20%; right: 60%; animation-delay: 4s; }

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

/* Sections */
.section-container {
  max-width: var(--max-content-width);
  margin: 0 auto;
  padding: 0 var(--space-6);
}

.section-title {
  text-align: center;
  font-size: var(--text-3xl);
  margin-bottom: var(--space-3);
}

.section-subtitle {
  text-align: center;
  color: var(--color-text-secondary);
  margin-bottom: var(--space-10);
}

/* Services */
.services-section { padding: var(--space-20) 0; }
.services-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-6); }
.service-card { text-align: center; padding: var(--space-8) var(--space-6); }
.service-card-button {
  width: 100%;
  appearance: none;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  cursor: pointer;
  transition: transform var(--transition-base), box-shadow var(--transition-base), border-color var(--transition-base);
}
.service-card-button:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-primary-100);
}
.service-card-button:focus-visible {
  outline: 3px solid var(--color-primary-100);
  outline-offset: 2px;
}
.service-icon {
  width: 64px; height: 64px;
  border-radius: var(--radius-lg);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.75rem;
  margin: 0 auto var(--space-5);
}
.service-card h3 { font-size: var(--text-lg); margin-bottom: var(--space-3); }
.service-card p { font-size: var(--text-sm); color: var(--color-text-secondary); }

/* Facilities */
.facilities-section { padding: var(--space-16) 0; background: var(--color-gray-50); }
.facilities-section .section-title { margin-bottom: var(--space-6); }
.facilities-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-6); max-width: 760px; margin: var(--space-6) auto 0; }
.facility-item {
  display: flex; flex-direction: column; align-items: center; gap: var(--space-2);
  padding: var(--space-5);
  background: var(--color-surface);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-xs);
  transition: transform var(--transition-base), box-shadow var(--transition-base), border-color var(--transition-base);
  border: 1px solid var(--color-border);
}
.facility-button {
  width: 100%;
  appearance: none;
  cursor: pointer;
}
.facility-button:hover {
  box-shadow: var(--shadow-md);
  transform: scale(1.03);
  border-color: var(--color-primary-100);
}
.facility-button:focus-visible {
  outline: 3px solid var(--color-primary-100);
  outline-offset: 2px;
}
.facility-icon { font-size: 2rem; }
.facility-name { font-size: var(--text-sm); font-weight: var(--font-medium); color: var(--color-text-primary); }

.btn-primary {
  box-shadow: var(--shadow-sm);
  transition: transform var(--transition-base), box-shadow var(--transition-base), filter var(--transition-base);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  filter: brightness(1.02);
}

.btn-outline {
  transition: transform var(--transition-base), background-color var(--transition-base), box-shadow var(--transition-base);
}

.btn-outline:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-sm);
}

.section-container, .hero-container, .cta-card, .service-card, .facility-item {
  scroll-margin-top: var(--header-height);
}

/* Committee */
.committee-section { padding: var(--space-20) 0; }
.committee-grid { display: flex; justify-content: center; gap: var(--space-8); flex-wrap: wrap; }
.member-card { text-align: center; }
.member-card h4 { margin-top: var(--space-3); font-size: var(--text-sm); }
.member-card p { font-size: var(--text-xs); color: var(--color-text-muted); }

/* CTA */
.cta-section { padding: 0 0 var(--space-20); }
.cta-card {
  background: linear-gradient(135deg, var(--color-primary), var(--color-info));
  color: white;
  text-align: center;
  padding: var(--space-16) var(--space-8);
  border-radius: var(--radius-2xl);
}
.cta-card h2 { color: white; font-size: var(--text-3xl); margin-bottom: var(--space-4); }
.cta-card p { color: rgba(255,255,255,0.85); margin-bottom: var(--space-8); font-size: var(--text-lg); }
.cta-card .btn { background: white; color: var(--color-primary); }
.cta-card .btn:hover { background: var(--color-gray-100); }

@media (max-width: 768px) {
  .hero-container { grid-template-columns: 1fr; }
  .hero-visual { display: none; }
  .hero-title { font-size: 2.5rem; }
  .services-grid { grid-template-columns: 1fr 1fr; }
  .facilities-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (prefers-reduced-motion: reduce) {
  .shape,
  .service-card-button,
  .facility-button,
  .btn-primary,
  .btn-outline {
    animation: none;
    transition: none;
  }
}
</style>
