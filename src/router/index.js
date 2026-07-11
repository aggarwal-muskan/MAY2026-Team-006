// ============================================
// SocioNeed — Vue Router Configuration
// ============================================
import { createRouter, createWebHistory } from 'vue-router'

// ── Public Pages ──
const LandingPage = () => import('@/views/public/LandingPage.vue')
const AboutUs = () => import('@/views/public/AboutUs.vue')
const Services = () => import('@/views/public/Services.vue')
const ContactUs = () => import('@/views/public/ContactUs.vue')
const HowItWorks = () => import('@/views/public/HowItWorks.vue')

// ── Auth Pages ──
const LoginPage = () => import('@/views/auth/LoginPage.vue')
const RegisterPage = () => import('@/views/auth/RegisterPage.vue')

// ── Portal Screen Renderers ──
const ResidentScreen = () => import('@/components/screens/ResidentPortalView.vue')
const AdminScreen = () => import('@/components/screens/AdminPortalView.vue')
const ProviderScreen = () => import('@/components/screens/ProviderPortalView.vue')
const SecurityScreen = () => import('@/components/screens/SecurityPortalView.vue')

const routes = [
  // ── Public Routes ──
  { path: '/', name: 'Landing', component: LandingPage, meta: { layout: 'public' } },
  { path: '/about', name: 'About', component: AboutUs, meta: { layout: 'public' } },
  { path: '/services', name: 'Services', component: Services, meta: { layout: 'public' } },
  { path: '/contact', name: 'Contact', component: ContactUs, meta: { layout: 'public' } },
  { path: '/how-it-works', name: 'HowItWorks', component: HowItWorks, meta: { layout: 'public' } },
  { path: '/login', name: 'Login', component: LoginPage, meta: { layout: 'auth' } },
  { path: '/register', name: 'Register', component: RegisterPage, meta: { layout: 'auth' } },

  // ── Resident Routes ──
  { path: '/resident/dashboard', name: 'ResidentDashboard', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'dashboard' } },
  { path: '/resident/notices', name: 'ResidentNotices', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'notices' } },
  { path: '/resident/events', name: 'ResidentEvents', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'events' } },
  { path: '/resident/complaints', name: 'ResidentComplaints', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'complaints' } },
  { path: '/resident/complaints/new', name: 'RaiseComplaint', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'raise-complaint' } },
  { path: '/resident/complaints/:id', name: 'ComplaintDetails', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'complaint-details' } },
  { path: '/resident/services', name: 'BrowseServices', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'browse-services' } },
  { path: '/resident/services/provider/:id', name: 'ProviderDetails', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'provider-details' } },
  { path: '/resident/booking-calendar', name: 'BookingCalendar', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'booking-calendar' } },
  { path: '/resident/my-bookings', name: 'MyBookings', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'my-bookings' } },
  { path: '/resident/amenities', name: 'BookAmenities', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'book-amenities' } },
  { path: '/resident/parking', name: 'Parking', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'parking' } },
  { path: '/resident/visitor-parking', name: 'VisitorParking', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'visitor-parking' } },
  { path: '/resident/family', name: 'MyFamily', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'family' } },
  { path: '/resident/notifications', name: 'ResidentNotifications', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'notifications' } },
  { path: '/resident/profile', name: 'ResidentProfile', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'profile' } },
  { path: '/resident/help', name: 'ResidentHelp', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'help-support' } },
  { path: '/resident/maintenance-bills', name: 'MaintenanceBills', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'maintenance-bills' } },
  { path: '/resident/service-history', name: 'ServiceHistory', component: ResidentScreen, meta: { layout: 'portal', role: 'resident', sidebar: 'resident', page: 'service-history' } },

  // ── Admin Routes ──
  { path: '/admin/dashboard', name: 'AdminDashboard', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'dashboard' } },
  { path: '/admin/residents', name: 'AdminResidents', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'residents' } },
  { path: '/admin/tenants', name: 'AdminTenants', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'tenants' } },
  { path: '/admin/providers', name: 'AdminProviders', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'providers' } },
  { path: '/admin/complaints', name: 'AdminComplaints', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'complaints' } },
  { path: '/admin/notices', name: 'AdminNotices', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'notices' } },
  { path: '/admin/notices/create', name: 'CreateNotice', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'create-notice' } },
  { path: '/admin/events', name: 'AdminEvents', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'events' } },
  { path: '/admin/events/create', name: 'CreateEvent', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'create-event' } },
  { path: '/admin/parking', name: 'ParkingManagement', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'parking' } },
  { path: '/admin/parking/assign', name: 'AssignParking', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'assign-parking' } },
  { path: '/admin/analytics', name: 'Analytics', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'analytics' } },
  { path: '/admin/settings', name: 'AdminSettings', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'settings' } },
  { path: '/admin/roles', name: 'RolesPermissions', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'roles' } },
  { path: '/admin/maintenance-fees', name: 'MaintenanceFees', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'maintenance-fees' } },
  { path: '/admin/reports', name: 'ReportsExport', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'reports' } },
  { path: '/admin/logs', name: 'SystemLogs', component: AdminScreen, meta: { layout: 'admin', role: 'admin', sidebar: 'admin', page: 'logs' } },

  // ── Service Provider Routes ──
  { path: '/provider/dashboard', name: 'ProviderDashboard', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'dashboard' } },
  { path: '/provider/bookings', name: 'ProviderBookings', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'bookings' } },
  { path: '/provider/availability', name: 'ProviderAvailability', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'availability' } },
  { path: '/provider/services', name: 'ProviderServices', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'services' } },
  { path: '/provider/reviews', name: 'ProviderReviews', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'reviews' } },
  { path: '/provider/earnings', name: 'ProviderEarnings', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'earnings' } },
  { path: '/provider/profile', name: 'ProviderProfile', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'profile' } },
  { path: '/provider/notifications', name: 'ProviderNotifications', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'notifications' } },
  { path: '/provider/settings', name: 'ProviderSettings', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'settings' } },
  { path: '/provider/help', name: 'ProviderHelp', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'help' } },
  { path: '/provider/customer-history', name: 'CustomerHistory', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'customer-history' } },
  { path: '/provider/completed-jobs', name: 'CompletedJobs', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'completed-jobs' } },
  { path: '/provider/payouts', name: 'Payouts', component: ProviderScreen, meta: { layout: 'portal', role: 'provider', sidebar: 'provider', page: 'payouts' } },

  // ── Security Routes ──
  { path: '/security/dashboard', name: 'SecurityDashboard', component: SecurityScreen, meta: { layout: 'portal', role: 'security', sidebar: 'security', page: 'dashboard' } },
  { path: '/security/visitor-entry', name: 'VisitorEntry', component: SecurityScreen, meta: { layout: 'portal', role: 'security', sidebar: 'security', page: 'visitor-entry' } },
  { path: '/security/parking', name: 'ParkingMonitor', component: SecurityScreen, meta: { layout: 'portal', role: 'security', sidebar: 'security', page: 'parking-monitor' } },
  { path: '/security/vehicles', name: 'VehicleLogs', component: SecurityScreen, meta: { layout: 'portal', role: 'security', sidebar: 'security', page: 'vehicle-logs' } },
  { path: '/security/patrol', name: 'PatrolLog', component: SecurityScreen, meta: { layout: 'portal', role: 'security', sidebar: 'security', page: 'patrol-log' } },
  { path: '/security/visitor-approval', name: 'VisitorApproval', component: SecurityScreen, meta: { layout: 'portal', role: 'security', sidebar: 'security', page: 'visitor-approval' } },
  { path: '/security/emergency', name: 'EmergencyAlerts', component: SecurityScreen, meta: { layout: 'portal', role: 'security', sidebar: 'security', page: 'emergency-alerts' } },
  { path: '/security/incidents', name: 'IncidentReports', component: SecurityScreen, meta: { layout: 'portal', role: 'security', sidebar: 'security', page: 'incident-reports' } },

  // ── Catch-all ──
  { path: '/:pathMatch(.*)*', redirect: '/' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    return { top: 0 }
  },
})

// ── Navigation Guard ──
router.beforeEach((to, from, next) => {
  // For this frontend-only version, we allow all navigation
  // In production, this would check auth state
  next()
})

export default router
