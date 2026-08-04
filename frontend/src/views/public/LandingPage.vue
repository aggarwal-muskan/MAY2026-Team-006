<template>
  <div class="landing-page">
    <section class="hero-section" id="top">
      <div class="hero-grid">
        <div class="hero-copy">
          <p class="eyebrow">SocioNeed Community OS</p>
          <h1>Stronger Community, Better Living</h1>
          <p class="hero-lead">
            Manage residents, services, notices, security, and support operations in one elegant platform.
            SocioNeed keeps every part of community life connected without adding complexity.
          </p>

          <div class="hero-actions">
            <router-link to="/register" class="btn btn-primary btn-lg">Get Started</router-link>
            <router-link to="/login" class="btn btn-outline btn-lg">Login</router-link>
            <a href="#features" class="btn btn-ghost btn-lg hero-link">Explore Features</a>
          </div>

          <div class="hero-metrics">
            <article class="metric-card card card-hover">
              <strong>250+</strong>
              <span>Residents connected</span>
            </article>
            <article class="metric-card card card-hover">
              <strong>50+</strong>
              <span>Services managed</span>
            </article>
            <article class="metric-card card card-hover">
              <strong>99.9%</strong>
              <span>Workflow coverage</span>
            </article>
          </div>
        </div>

        <div class="hero-visual card card-hover" aria-hidden="true">
          <div class="visual-backdrop"></div>
          <div class="skyline skyline-back">
            <span class="tower tower-sm"></span>
            <span class="tower tower-md"></span>
            <span class="tower tower-lg"></span>
            <span class="tower tower-xl"></span>
          </div>
          <div class="community-band">
            <span class="tree"></span>
            <span class="path"></span>
            <span class="person person-left"></span>
            <span class="person person-center"></span>
            <span class="person person-right"></span>
            <span class="tree tree-right"></span>
          </div>
          <div class="floating-bubble bubble-one">
            <strong>24/7</strong>
            <span>Support</span>
          </div>
          <div class="floating-bubble bubble-two">
            <strong>Fast</strong>
            <span>Resolution</span>
          </div>
          <div class="floating-bubble bubble-three">
            <strong>Live</strong>
            <span>Updates</span>
          </div>
        </div>
      </div>
    </section>

    <section class="trust-strip">
      <div class="section-container trust-grid">
        <div>
          <span class="trust-label">Built for</span>
          <strong>Residents, admins, providers, and security teams</strong>
        </div>
        <div>
          <span class="trust-label">Designed like</span>
          <strong>Linear, Stripe, Notion, and Vercel</strong>
        </div>
        <div>
          <span class="trust-label">Focused on</span>
          <strong>Clarity, speed, and operational confidence</strong>
        </div>
      </div>
    </section>

    <section class="services-section section-container" id="services">
      <div class="section-header">
        <p class="eyebrow">Core Platform</p>
        <h2>Everything your society needs, in one place</h2>
        <p>These are the same services your project already exposes, now presented like a polished product suite.</p>
      </div>

      <div class="services-grid">
        <button
          v-for="service in featureCards"
          :key="service.title"
          type="button"
          class="service-card card card-hover"
        >
          <div class="service-icon" v-html="service.icon"></div>
          <h3>{{ service.title }}</h3>
          <p>{{ service.desc }}</p>
        </button>
      </div>
    </section>

    <section class="features-section section-container" id="features">
      <div class="section-header">
        <p class="eyebrow">Why SocioNeed</p>
        <h2>Premium workflows with clear information hierarchy</h2>
        <p>Thoughtful spacing, strong contrast, and calm motion help every user understand what matters at a glance.</p>
      </div>

      <div class="feature-grid">
        <article v-for="feature in featurePillars" :key="feature.title" class="feature-card card card-hover">
          <div class="feature-icon" v-html="feature.icon"></div>
          <h3>{{ feature.title }}</h3>
          <p>{{ feature.description }}</p>
        </article>
      </div>
    </section>

    <section class="timeline-section section-container" id="how-it-works">
      <div class="section-header">
        <p class="eyebrow">How It Works</p>
        <h2>Simple flow, polished execution</h2>
        <p>The project keeps the same structure users already know, but the visual presentation now feels structured and intentional.</p>
      </div>

      <div class="timeline card">
        <article v-for="(step, index) in workflowSteps" :key="step.title" class="timeline-step">
          <div class="timeline-number">0{{ index + 1 }}</div>
          <div class="timeline-content">
            <h3>{{ step.title }}</h3>
            <p>{{ step.description }}</p>
          </div>
        </article>
      </div>
    </section>

    <section class="facilities-section section-container">
      <div class="section-header">
        <p class="eyebrow">Facilities</p>
        <h2>Community amenities and shared spaces</h2>
        <p>Reused from your existing project data, but elevated with cleaner cards and stronger hierarchy.</p>
      </div>

      <div class="facilities-grid">
        <button v-for="f in facilities" :key="f.id" type="button" class="facility-item card card-hover">
          <span class="facility-icon">{{ f.icon }}</span>
          <span class="facility-name">{{ f.name }}</span>
        </button>
      </div>
    </section>

    <section class="committee-section section-container">
      <div class="section-header">
        <p class="eyebrow">Committee</p>
        <h2>Management committee at a glance</h2>
        <p>The same members and responsibilities, now displayed like a premium team directory.</p>
      </div>

      <div class="committee-grid">
        <article v-for="member in committeeMembers" :key="member.id" class="member-card card card-hover">
          <div class="avatar avatar-xl">{{ member.name.split(' ').map((part) => part[0]).join('') }}</div>
          <div>
            <h3>{{ member.name }}</h3>
            <p>{{ member.role }}</p>
          </div>
        </article>
      </div>
    </section>

    <section class="testimonials-section section-container">
      <div class="section-header">
        <p class="eyebrow">Testimonials</p>
        <h2>Built for trust and everyday clarity</h2>
        <p>Resident-facing tools feel calmer when the interface does the heavy lifting for them.</p>
      </div>

      <div class="testimonial-grid">
        <article v-for="testimonial in testimonials" :key="testimonial.name" class="testimonial-card card card-hover">
          <p class="quote">“{{ testimonial.quote }}”</p>
          <div class="testimonial-footer">
            <div>
              <strong>{{ testimonial.name }}</strong>
              <span>{{ testimonial.role }}</span>
            </div>
            <div class="rating">{{ testimonial.rating }}</div>
          </div>
        </article>
      </div>
    </section>

    <section class="cta-section section-container">
      <div class="cta-card card">
        <div>
          <p class="eyebrow">Ready to upgrade</p>
          <h2>Make SocioNeed feel like a product company built it</h2>
          <p>Keep the same functionality, routes, and workflows while delivering a polished modern SaaS experience.</p>
        </div>
        <div class="cta-actions">
          <router-link to="/register" class="btn btn-primary btn-lg">Get Started Free</router-link>
          <router-link to="/contact" class="btn btn-outline btn-lg">Contact Team</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { committeeMembers, facilities } from '@/data/mockData'

const featureCards = [
  {
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><path d="M9 22V12h6v10"></path></svg>',
    title: 'Notices & Events',
    desc: 'Stay updated with announcements, celebrations, and maintenance notices without bouncing across screens.',
  },
  {
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="16" rx="3"></rect><path d="M7 8h10M7 12h6M7 16h8"></path></svg>',
    title: 'Service Booking',
    desc: 'Book amenities and trusted providers through a clear, streamlined booking flow.',
  },
  {
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 7h16M4 12h10M4 17h13"></path><path d="M18 11l2 1-2 1"></path></svg>',
    title: 'Complaint Management',
    desc: 'Report issues, track progress, and see status updates in real time from one calm dashboard.',
  },
  {
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M7 20V10l5-6 5 6v10"></path><path d="M5 20h14"></path><path d="M12 14v6"></path></svg>',
    title: 'Visitor Security',
    desc: 'Monitor gate approvals, vehicle logs, and incidents with a security-first information layout.',
  },
]

const featurePillars = [
  {
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 19V5h16v14"></path><path d="M8 9h8M8 13h5"></path></svg>',
    title: 'Clear hierarchy',
    description: 'Important metrics, statuses, and actions stay visually separated so each screen reads instantly.',
  },
  {
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3v18"></path><path d="M5 7h14"></path><path d="M5 17h14"></path></svg>',
    title: 'Balanced whitespace',
    description: 'The interface breathes more, with better spacing between cards, forms, tables, and dashboards.',
  },
  {
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 12h16"></path><path d="M12 4v16"></path><circle cx="12" cy="12" r="3"></circle></svg>',
    title: 'Action clarity',
    description: 'Primary and secondary actions are styled consistently so users always know what to do next.',
  },
  {
    icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 19h16"></path><path d="M7 16V8"></path><path d="M12 16V5"></path><path d="M17 16v-6"></path></svg>',
    title: 'Dashboard-first design',
    description: 'Charts, tables, cards, and sidebars now feel like a coherent SaaS product instead of a classroom project.',
  },
]

const workflowSteps = [
  {
    title: 'Sign in to the right role',
    description: 'Residents, admins, providers, and security staff land in the correct portal with the same route structure.',
  },
  {
    title: 'Navigate with confidence',
    description: 'A clearer sidebar, tighter top bar, and calmer spacing make it easy to move through the system.',
  },
  {
    title: 'Complete key tasks quickly',
    description: 'Forms, tables, and actions feel polished, helping users submit requests or approvals with less friction.',
  },
  {
    title: 'Track progress visually',
    description: 'Statuses, badges, metrics, and cards surface the important information without overwhelming the user.',
  },
]

const testimonials = [
  {
    name: 'Priya Sharma',
    role: 'Resident',
    rating: '★★★★★',
    quote: 'The new UI makes community updates and complaint tracking feel much easier to trust and use.',
  },
  {
    name: 'Rahul Verma',
    role: 'Service Provider',
    rating: '★★★★★',
    quote: 'The booking and earnings screens now look like a real product, not a student prototype.',
  },
  {
    name: 'Anita Kapoor',
    role: 'Admin Coordinator',
    rating: '★★★★★',
    quote: 'Everything feels calmer, more structured, and far more professional across all dashboards.',
  },
]
</script>

<style scoped>
.landing-page {
  overflow-x: hidden;
}

.section-container {
  max-width: var(--max-content-width);
  margin: 0 auto;
  padding: 0 var(--space-6);
}

.section-header {
  display: grid;
  gap: var(--space-3);
  max-width: 720px;
  margin-bottom: var(--space-8);
}

.section-header h2 {
  font-size: clamp(1.75rem, 2.8vw, 2.75rem);
  letter-spacing: -0.03em;
}

.hero-section {
  position: relative;
  padding: var(--space-16) 0 var(--space-12);
  overflow: hidden;
}

.hero-section::before,
.hero-section::after {
  content: '';
  position: absolute;
  border-radius: var(--radius-full);
  filter: blur(10px);
  pointer-events: none;
}

.hero-section::before {
  top: 10%;
  left: -4rem;
  width: 18rem;
  height: 18rem;
  background: rgba(37, 99, 235, 0.12);
}

.hero-section::after {
  right: 4%;
  bottom: 10%;
  width: 14rem;
  height: 14rem;
  background: rgba(59, 130, 246, 0.1);
}

.hero-grid {
  max-width: var(--max-content-width);
  margin: 0 auto;
  padding: 0 var(--space-6);
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(360px, 0.95fr);
  gap: var(--space-12);
  align-items: center;
}

.hero-copy h1 {
  font-size: clamp(3rem, 5vw, 5rem);
  line-height: 0.96;
  letter-spacing: -0.05em;
  margin-bottom: var(--space-5);
}

.hero-lead {
  max-width: 640px;
  margin-bottom: var(--space-8);
  font-size: var(--text-lg);
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-3);
  margin-bottom: var(--space-8);
}

.hero-link {
  padding-inline: var(--space-5);
}

.hero-metrics {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: var(--space-4);
}

.metric-card {
  padding: var(--space-5);
}

.metric-card strong {
  display: block;
  font-size: clamp(1.6rem, 2vw, 2.1rem);
  color: var(--color-text-primary);
  letter-spacing: -0.03em;
}

.metric-card span {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
}

.hero-visual {
  position: relative;
  min-height: 520px;
  padding: 0;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.95), rgba(241, 245, 249, 0.86)),
    radial-gradient(circle at top, rgba(37, 99, 235, 0.12), transparent 46%);
}

.visual-backdrop {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(37, 99, 235, 0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(37, 99, 235, 0.04) 1px, transparent 1px);
  background-size: 56px 56px;
  opacity: 0.5;
}

.skyline,
.community-band {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}

.skyline {
  bottom: 140px;
  display: flex;
  align-items: flex-end;
  gap: 16px;
}

.tower {
  position: relative;
  border-radius: 18px 18px 6px 6px;
  background: linear-gradient(180deg, #dbeafe, #93c5fd 54%, #2563eb 100%);
  box-shadow: 0 16px 36px rgba(37, 99, 235, 0.18);
}

.tower::before {
  content: '';
  position: absolute;
  inset: 10px;
  border-radius: 12px;
  background-image:
    radial-gradient(circle at center, rgba(255, 255, 255, 0.8) 0 3px, transparent 3px),
    linear-gradient(transparent 18%, rgba(255, 255, 255, 0.35) 18% 20%, transparent 20% 36%, rgba(255, 255, 255, 0.35) 36% 38%, transparent 38% 54%, rgba(255, 255, 255, 0.35) 54% 56%, transparent 56% 72%, rgba(255, 255, 255, 0.35) 72% 74%, transparent 74% 100%);
  background-size: 18px 18px, 100% 100%;
  opacity: 0.65;
}

.tower-sm {
  width: 66px;
  height: 170px;
  opacity: 0.72;
}

.tower-md {
  width: 78px;
  height: 240px;
}

.tower-lg {
  width: 96px;
  height: 300px;
}

.tower-xl {
  width: 74px;
  height: 210px;
  opacity: 0.86;
}

.community-band {
  bottom: 66px;
  width: calc(100% - 4rem);
  height: 120px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.95), rgba(239, 246, 255, 0.8));
  border: 1px solid rgba(37, 99, 235, 0.08);
  border-radius: 120px;
  box-shadow: 0 20px 40px rgba(15, 23, 42, 0.08);
}

.path {
  position: absolute;
  left: 50%;
  top: 55%;
  width: 72%;
  height: 14px;
  transform: translateX(-50%);
  border-radius: var(--radius-full);
  background: linear-gradient(90deg, rgba(37, 99, 235, 0.06), rgba(37, 99, 235, 0.14), rgba(37, 99, 235, 0.06));
}

.tree,
.person {
  position: absolute;
  bottom: 18px;
}

.tree {
  width: 28px;
  height: 52px;
  left: 18%;
  border-radius: 999px 999px 8px 8px;
  background: linear-gradient(180deg, #4ade80, #16a34a);
}

.tree::after,
.tree-right::after {
  content: '';
  position: absolute;
  left: 50%;
  bottom: -16px;
  width: 6px;
  height: 16px;
  transform: translateX(-50%);
  border-radius: 2px;
  background: #8b5a2b;
}

.tree-right {
  left: auto;
  right: 16%;
}

.person {
  width: 14px;
  height: 48px;
  border-radius: 999px;
  background: linear-gradient(180deg, #0f172a 0 16px, transparent 16px 22px, #2563eb 22px 34px, #0f172a 34px 100%);
}

.person::before,
.person::after {
  content: '';
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  border-radius: var(--radius-full);
}

.person::before {
  top: -12px;
  width: 12px;
  height: 12px;
  background: #0f172a;
}

.person::after {
  bottom: -12px;
  width: 4px;
  height: 14px;
  background: #0f172a;
}

.person-left { left: 30%; }
.person-center { left: 52%; background: linear-gradient(180deg, #0f172a 0 16px, transparent 16px 22px, #f97316 22px 34px, #0f172a 34px 100%); }
.person-right { right: 28%; background: linear-gradient(180deg, #0f172a 0 16px, transparent 16px 22px, #22c55e 22px 34px, #0f172a 34px 100%); }

.floating-bubble {
  position: absolute;
  min-width: 132px;
  padding: var(--space-4) var(--space-5);
  border: 1px solid rgba(37, 99, 235, 0.12);
  border-radius: var(--radius-xl);
  background: rgba(255, 255, 255, 0.92);
  box-shadow: 0 16px 36px rgba(37, 99, 235, 0.12);
  backdrop-filter: blur(14px);
  animation: float 7s ease-in-out infinite;
}

.floating-bubble strong {
  display: block;
  font-size: 1.2rem;
  color: var(--color-text-primary);
}

.floating-bubble span {
  font-size: var(--text-xs);
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.bubble-one { top: 16%; left: 10%; }
.bubble-two { top: 28%; right: 8%; animation-delay: 1.5s; }
.bubble-three { bottom: 24%; right: 18%; animation-delay: 3s; }

.trust-strip {
  padding: 0 0 var(--space-16);
}

.trust-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: var(--space-4);
}

.trust-grid > div {
  padding: var(--space-5);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  background: rgba(255, 255, 255, 0.8);
  box-shadow: var(--shadow-xs);
}

.trust-label {
  display: block;
  margin-bottom: var(--space-2);
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--color-primary);
}

.services-section,
.features-section,
.timeline-section,
.facilities-section,
.committee-section,
.testimonials-section {
  padding-bottom: var(--space-16);
}

.services-grid,
.feature-grid,
.testimonial-grid,
.facilities-grid,
.committee-grid {
  display: grid;
  gap: var(--space-4);
}

.services-grid,
.feature-grid,
.testimonial-grid,
.facilities-grid,
.committee-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.service-card,
.feature-card,
.testimonial-card,
.facility-item,
.member-card {
  display: grid;
  gap: var(--space-3);
  text-align: left;
}

.service-card {
  padding: var(--space-6);
  min-height: 210px;
  border: 1px solid var(--color-border);
  background: rgba(255, 255, 255, 0.9);
}

.service-icon,
.feature-icon {
  width: 52px;
  height: 52px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-lg);
  color: var(--color-primary);
  background: var(--color-primary-50);
}

.service-icon :deep(svg),
.feature-icon :deep(svg) {
  width: 24px;
  height: 24px;
}

.service-card h3,
.feature-card h3,
.testimonial-card strong,
.member-card h3 {
  font-size: var(--text-lg);
}

.service-card p,
.feature-card p,
.testimonial-card p,
.member-card p {
  color: var(--color-text-secondary);
}

.timeline {
  display: grid;
  gap: var(--space-4);
  padding: var(--space-6);
}

.timeline-step {
  display: grid;
  grid-template-columns: 72px minmax(0, 1fr);
  gap: var(--space-4);
  align-items: start;
  padding: var(--space-2) 0;
}

.timeline-step:not(:last-child) {
  padding-bottom: var(--space-4);
  border-bottom: 1px solid var(--color-border);
}

.timeline-number {
  width: 64px;
  height: 64px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-xl);
  background: var(--color-primary-50);
  color: var(--color-primary);
  font-family: var(--font-heading);
  font-size: var(--text-lg);
  font-weight: var(--font-bold);
}

.facility-item {
  justify-items: center;
  padding: var(--space-5);
  min-height: 120px;
}

.facility-icon {
  font-size: 2rem;
}

.facility-name {
  font-weight: var(--font-medium);
  color: var(--color-text-primary);
  text-align: center;
}

.member-card {
  justify-items: center;
  text-align: center;
  padding: var(--space-6);
}

.testimonial-card {
  padding: var(--space-6);
  min-height: 220px;
}

.quote {
  font-size: var(--text-lg);
  color: var(--color-text-primary);
}

.testimonial-footer {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: var(--space-4);
  margin-top: auto;
}

.testimonial-footer span {
  display: block;
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
}

.rating {
  color: var(--color-accent-dark);
  font-size: var(--text-sm);
  letter-spacing: 0.08em;
}

.cta-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-8);
  padding: var(--space-10);
  border: 1px solid rgba(37, 99, 235, 0.14);
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.04), rgba(59, 130, 246, 0.1));
}

.cta-card h2 {
  margin-bottom: var(--space-3);
  font-size: clamp(1.75rem, 3vw, 2.6rem);
}

.cta-actions {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-3);
}

@keyframes float {
  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-14px);
  }
}

@media (max-width: 1100px) {
  .hero-grid,
  .trust-grid,
  .services-grid,
  .feature-grid,
  .testimonial-grid,
  .facilities-grid,
  .committee-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .hero-visual {
    min-height: 460px;
  }
}

@media (max-width: 768px) {
  .hero-grid,
  .trust-grid,
  .services-grid,
  .feature-grid,
  .testimonial-grid,
  .facilities-grid,
  .committee-grid,
  .cta-card {
    grid-template-columns: 1fr;
  }

  .hero-grid {
    padding-inline: var(--space-4);
  }

  .hero-copy h1 {
    font-size: clamp(2.6rem, 10vw, 3.4rem);
  }

  .hero-metrics {
    grid-template-columns: 1fr;
  }

  .hero-visual {
    min-height: 380px;
  }

  .section-container {
    padding-inline: var(--space-4);
  }

  .cta-card {
    padding: var(--space-8);
  }

  .timeline-step {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .floating-bubble {
    animation: none;
  }
}
</style>
