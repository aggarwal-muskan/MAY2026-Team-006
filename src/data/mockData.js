// ============================================
// SocioNeed — Mock Data
// ============================================

// ── Residents ──
export const residents = [
  { id: 1, name: 'Priya Sharma', flat: 'A-101', phone: '9876543210', email: 'priya.sharma@email.com', role: 'Owner', status: 'Active', avatar: null, joinDate: '2022-03-15' },
  { id: 2, name: 'Rahul Verma', flat: 'A-102', phone: '9876543211', email: 'rahul.verma@email.com', role: 'Owner', status: 'Active', avatar: null, joinDate: '2022-05-20' },
  { id: 3, name: 'Anita Desai', flat: 'A-103', phone: '9876543212', email: 'anita.desai@email.com', role: 'Owner', status: 'Active', avatar: null, joinDate: '2021-11-10' },
  { id: 4, name: 'Suresh Kumar', flat: 'B-201', phone: '9876543213', email: 'suresh.kumar@email.com', role: 'Owner', status: 'Active', avatar: null, joinDate: '2023-01-05' },
  { id: 5, name: 'Meena Patel', flat: 'B-202', phone: '9876543214', email: 'meena.patel@email.com', role: 'Owner', status: 'Active', avatar: null, joinDate: '2022-08-12' },
  { id: 6, name: 'Vikram Singh', flat: 'B-203', phone: '9876543215', email: 'vikram.singh@email.com', role: 'Owner', status: 'Active', avatar: null, joinDate: '2021-06-30' },
  { id: 7, name: 'Deepa Nair', flat: 'C-301', phone: '9876543216', email: 'deepa.nair@email.com', role: 'Owner', status: 'Active', avatar: null, joinDate: '2023-04-18' },
  { id: 8, name: 'Amit Joshi', flat: 'C-302', phone: '9876543217', email: 'amit.joshi@email.com', role: 'Owner', status: 'Active', avatar: null, joinDate: '2022-12-01' },
  { id: 9, name: 'Kavita Reddy', flat: 'C-303', phone: '9876543218', email: 'kavita.reddy@email.com', role: 'Owner', status: 'Inactive', avatar: null, joinDate: '2021-09-25' },
  { id: 10, name: 'Rajesh Gupta', flat: 'D-401', phone: '9876543219', email: 'rajesh.gupta@email.com', role: 'Owner', status: 'Active', avatar: null, joinDate: '2023-07-08' },
]

// ── Tenants ──
export const tenants = [
  { id: 1, name: 'Arjun Mehta', flat: 'A-104', phone: '9123456780', email: 'arjun.mehta@email.com', owner: 'Priya Sharma', leaseStart: '2024-01-01', leaseEnd: '2025-01-01', status: 'Active' },
  { id: 2, name: 'Sneha Rao', flat: 'B-204', phone: '9123456781', email: 'sneha.rao@email.com', owner: 'Suresh Kumar', leaseStart: '2024-03-15', leaseEnd: '2025-03-15', status: 'Active' },
  { id: 3, name: 'Kiran Das', flat: 'C-304', phone: '9123456782', email: 'kiran.das@email.com', owner: 'Deepa Nair', leaseStart: '2023-06-01', leaseEnd: '2024-06-01', status: 'Expired' },
  { id: 4, name: 'Neha Kapoor', flat: 'D-402', phone: '9123456783', email: 'neha.kapoor@email.com', owner: 'Rajesh Gupta', leaseStart: '2024-05-01', leaseEnd: '2025-05-01', status: 'Active' },
  { id: 5, name: 'Sanjay Tiwari', flat: 'A-105', phone: '9123456784', email: 'sanjay.tiwari@email.com', owner: 'Rahul Verma', leaseStart: '2024-02-01', leaseEnd: '2025-02-01', status: 'Active' },
]

// ── Complaints ──
export const complaints = [
  { id: 'C-001', title: 'Water leakage in bathroom', category: 'Plumbing', description: 'There is a water leakage in the bathroom tap from last 2 days. Please fix it.', status: 'In Progress', date: '2024-05-20', resident: 'Priya Sharma', flat: 'A-101', assignedTo: 'Maintenance Team', priority: 'High' },
  { id: 'C-002', title: 'Street light not working', category: 'Electrical', description: 'The street light near Block B entrance is not working since last week.', status: 'Pending', date: '2024-05-18', resident: 'Rahul Verma', flat: 'A-102', assignedTo: null, priority: 'Medium' },
  { id: 'C-003', title: 'Garbage not collected', category: 'Housekeeping', description: 'Garbage has not been collected from our floor for the last 3 days.', status: 'Resolved', date: '2024-05-15', resident: 'Anita Desai', flat: 'A-103', assignedTo: 'Housekeeping Team', priority: 'High' },
  { id: 'C-004', title: 'Intercom not working', category: 'Other', description: 'The intercom system in our flat is completely non-functional.', status: 'Resolved', date: '2024-05-10', resident: 'Suresh Kumar', flat: 'B-201', assignedTo: 'IT Support', priority: 'Low' },
  { id: 'C-005', title: 'Lift maintenance required', category: 'Electrical', description: 'Lift in Block C is making unusual noises and sometimes gets stuck.', status: 'In Progress', date: '2024-05-22', resident: 'Deepa Nair', flat: 'C-301', assignedTo: 'Elevator Service', priority: 'Critical' },
  { id: 'C-006', title: 'Parking lot flooding', category: 'Plumbing', description: 'During rain, the basement parking gets flooded. Need drainage improvement.', status: 'Pending', date: '2024-05-19', resident: 'Vikram Singh', flat: 'B-203', assignedTo: null, priority: 'High' },
  { id: 'C-007', title: 'Broken playground swing', category: 'Maintenance', description: 'One of the swings in the children playground is broken and unsafe.', status: 'Resolved', date: '2024-05-12', resident: 'Meena Patel', flat: 'B-202', assignedTo: 'Maintenance Team', priority: 'Medium' },
  { id: 'C-008', title: 'CCTV camera malfunction', category: 'Security', description: 'CCTV camera at Block A entrance is not recording properly.', status: 'In Progress', date: '2024-05-21', resident: 'Amit Joshi', flat: 'C-302', assignedTo: 'Security Team', priority: 'High' },
]

// ── Events ──
export const events = [
  { id: 1, title: 'Yoga Session', date: '2024-05-21', time: '7:00 AM', venue: 'Club House', description: 'Morning yoga session for all residents. Bring your own yoga mat.', category: 'Wellness', capacity: 30, registered: 18, image: null },
  { id: 2, title: 'Blood Donation Camp', date: '2024-05-30', time: '10:00 AM', venue: 'Community Hall', description: 'Annual blood donation camp organized by the society welfare committee.', category: 'Health', capacity: 50, registered: 25, image: null },
  { id: 3, title: "Children's Day Celebration", date: '2024-06-02', time: '4:00 PM', venue: 'Club House', description: "Fun activities, games, and performances by children of the society.", category: 'Festival', capacity: 100, registered: 65, image: null },
  { id: 4, title: 'Cricket Tournament', date: '2024-06-10', time: '6:00 AM', venue: 'Sports Ground', description: 'Inter-block cricket tournament. Register your team of 11 players.', category: 'Sports', capacity: 88, registered: 44, image: null },
  { id: 5, title: 'Society Meeting', date: '2024-06-15', time: '5:00 PM', venue: 'Community Hall', description: 'Monthly society general body meeting. All residents are requested to attend.', category: 'Meeting', capacity: 200, registered: 0, image: null },
  { id: 6, title: 'Diwali Celebration', date: '2024-10-28', time: '6:00 PM', venue: 'Garden Area', description: 'Grand Diwali celebration with decorations, sweets, and fireworks display.', category: 'Festival', capacity: 300, registered: 120, image: null },
]

// ── Notices ──
export const notices = [
  { id: 1, title: 'Water Supply Maintenance', date: '2024-05-20', content: 'Water supply will be shut down on 21 May 2024 from 10:00 AM to 2:00 PM for maintenance work.', category: 'Maintenance', priority: 'High' },
  { id: 2, title: 'Lift Maintenance', date: '2024-05-18', content: 'Lift will be under maintenance on 22 May 2024. Please use the stairs. We apologize for the inconvenience.', category: 'Maintenance', priority: 'Medium' },
  { id: 3, title: 'Festival Celebration', date: '2024-05-16', content: 'Diwali celebration will be held on Oct 28. All residents are invited to participate in the cultural programs.', category: 'Event', priority: 'Low' },
  { id: 4, title: 'Parking Rules Update', date: '2024-05-15', content: 'All residents are requested to park only in the designated areas. Visitor parking is limited to 2 hours.', category: 'Rules', priority: 'Medium' },
  { id: 5, title: 'Visitor Entry Policy', date: '2024-05-10', content: 'New visitor entry policy effective from 1 June 2024. All visitors must register at the security gate.', category: 'Security', priority: 'High' },
  { id: 6, title: 'Monthly Maintenance Due', date: '2024-05-08', content: 'Monthly maintenance charges for May 2024 are due by 15th May. Late payment will attract a penalty of 2%.', category: 'Finance', priority: 'High' },
  { id: 7, title: 'Fire Drill', date: '2024-05-05', content: 'A fire safety drill will be conducted on 12th May at 10:00 AM. All residents must participate.', category: 'Safety', priority: 'High' },
]

// ── Bookings ──
export const bookings = [
  { id: 1, facility: 'Club House', date: '2024-05-25', time: '5:00 PM - 9:00 PM', purpose: 'Birthday Celebration', status: 'Confirmed', resident: 'Priya Sharma', flat: 'A-101' },
  { id: 2, facility: 'Gym', date: '2024-05-22', time: '6:00 AM - 7:00 AM', purpose: 'Morning Workout', status: 'Completed', resident: 'Rahul Verma', flat: 'A-102' },
  { id: 3, facility: 'Swimming Pool', date: '2024-05-28', time: '4:00 PM - 6:00 PM', purpose: 'Swimming Practice', status: 'Confirmed', resident: 'Anita Desai', flat: 'A-103' },
  { id: 4, facility: 'Community Hall', date: '2024-05-30', time: '10:00 AM - 1:00 PM', purpose: 'Society Meeting', status: 'Confirmed', resident: 'Suresh Kumar', flat: 'B-201' },
  { id: 5, facility: 'Guest Room', date: '2024-05-21', time: 'Full Day', purpose: 'Guest Accommodation', status: 'Completed', resident: 'Deepa Nair', flat: 'C-301' },
  { id: 6, facility: 'Tennis Court', date: '2024-06-01', time: '6:00 AM - 8:00 AM', purpose: 'Tennis Match', status: 'Upcoming', resident: 'Vikram Singh', flat: 'B-203' },
]

// ── Service Providers ──
export const serviceProviders = [
  { id: 1, name: 'Ravi Plumber', category: 'Plumber', phone: '9111222333', email: 'ravi.plumber@email.com', rating: 4.5, reviews: 120, experience: '5 years', description: 'Experienced plumber specializing in bathroom repairs, pipe fitting, and drainage solutions.', availability: { mon: true, tue: true, wed: true, thu: true, fri: true, sat: true, sun: false }, services: [{ name: 'Plumbing Work', price: '₹500 - ₹2000' }, { name: 'Pipe Fitting', price: '₹300 - ₹1500' }, { name: 'Bathroom Repair', price: '₹800 - ₹3000' }], earnings: 12450 },
  { id: 2, name: 'Sita Electrician', category: 'Electrician', phone: '9111222334', email: 'sita.elec@email.com', rating: 4.7, reviews: 95, experience: '8 years', description: 'Expert electrician for wiring, switchboard repairs, and appliance installations.', availability: { mon: true, tue: true, wed: false, thu: true, fri: true, sat: true, sun: false }, services: [{ name: 'Wiring', price: '₹400 - ₹2500' }, { name: 'Switchboard Repair', price: '₹200 - ₹800' }, { name: 'Appliance Installation', price: '₹500 - ₹1500' }], earnings: 18300 },
  { id: 3, name: 'Geeta House Maid', category: 'House Maid', phone: '9111222335', email: 'geeta.maid@email.com', rating: 4.3, reviews: 200, experience: '10 years', description: 'Professional house cleaning, utensil washing, and laundry services.', availability: { mon: true, tue: true, wed: true, thu: true, fri: true, sat: false, sun: false }, services: [{ name: 'House Cleaning', price: '₹300/day' }, { name: 'Utensil Washing', price: '₹150/day' }, { name: 'Laundry', price: '₹200/day' }], earnings: 9800 },
  { id: 4, name: 'Ramesh Gardener', category: 'Gardener', phone: '9111222336', email: 'ramesh.garden@email.com', rating: 4.6, reviews: 78, experience: '7 years', description: 'Garden maintenance, lawn mowing, plant care, and landscaping services.', availability: { mon: true, tue: false, wed: true, thu: false, fri: true, sat: true, sun: false }, services: [{ name: 'Garden Maintenance', price: '₹500/visit' }, { name: 'Lawn Mowing', price: '₹300/visit' }, { name: 'Plant Care', price: '₹200/visit' }], earnings: 7600 },
  { id: 5, name: 'Sunita Laundry', category: 'Laundry', phone: '9111222337', email: 'sunita.laundry@email.com', rating: 4.4, reviews: 150, experience: '6 years', description: 'Professional laundry and dry-cleaning services with pickup and delivery.', availability: { mon: true, tue: true, wed: true, thu: true, fri: true, sat: true, sun: false }, services: [{ name: 'Wash & Iron', price: '₹50/piece' }, { name: 'Dry Cleaning', price: '₹150/piece' }, { name: 'Bulk Laundry', price: '₹500/10kg' }], earnings: 15200 },
  { id: 6, name: 'Ajay Tailor', category: 'Tailor', phone: '9111222338', email: 'ajay.tailor@email.com', rating: 4.8, reviews: 60, experience: '12 years', description: 'Expert tailoring, alterations, and custom stitching for all garments.', availability: { mon: true, tue: true, wed: true, thu: true, fri: true, sat: false, sun: false }, services: [{ name: 'Alterations', price: '₹100 - ₹500' }, { name: 'Custom Stitching', price: '₹500 - ₹3000' }, { name: 'Blouse Stitching', price: '₹300 - ₹800' }], earnings: 11000 },
  { id: 7, name: 'Kumar Car Wash', category: 'Car Wash', phone: '9111222339', email: 'kumar.carwash@email.com', rating: 4.2, reviews: 85, experience: '4 years', description: 'Exterior and interior car cleaning, polishing, and detailing services.', availability: { mon: true, tue: true, wed: true, thu: true, fri: true, sat: true, sun: true }, services: [{ name: 'Basic Wash', price: '₹200' }, { name: 'Full Detailing', price: '₹1500' }, { name: 'Interior Cleaning', price: '₹800' }], earnings: 13500 },
  { id: 8, name: 'Lakshmi Cook', category: 'Cook', phone: '9111222340', email: 'lakshmi.cook@email.com', rating: 4.9, reviews: 180, experience: '15 years', description: 'Home-cooked meals, party catering, and special diet menu preparation.', availability: { mon: true, tue: true, wed: true, thu: true, fri: true, sat: true, sun: false }, services: [{ name: 'Daily Cooking', price: '₹5000/month' }, { name: 'Party Catering', price: '₹200/plate' }, { name: 'Tiffin Service', price: '₹3000/month' }], earnings: 22000 },
]

// ── Service Categories ──
export const serviceCategories = [
  { id: 'house-maid', name: 'House Maid', icon: '🏠', description: 'Professional cleaning services' },
  { id: 'plumber', name: 'Plumber', icon: '🔧', description: 'Plumbing and pipe repairs' },
  { id: 'electrician', name: 'Electrician', icon: '⚡', description: 'Electrical work and wiring' },
  { id: 'laundry', name: 'Laundry', icon: '👔', description: 'Wash, iron and dry cleaning' },
  { id: 'car-wash', name: 'Car Wash', icon: '🚗', description: 'Vehicle cleaning services' },
  { id: 'gardener', name: 'Gardener', icon: '🌿', description: 'Garden and lawn care' },
  { id: 'tailor', name: 'Tailor', icon: '✂️', description: 'Stitching and alterations' },
  { id: 'cook', name: 'Cook', icon: '👨‍🍳', description: 'Home cooking and catering' },
]

// ── Parking ──
export const parkingSlots = [
  { id: 'A-101', block: 'A', status: 'Occupied', resident: 'Priya Sharma', flat: 'A-101', vehicle: 'MH 01 AB 1234', type: 'Car' },
  { id: 'A-102', block: 'A', status: 'Occupied', resident: 'Rahul Verma', flat: 'A-102', vehicle: 'MH 02 CD 5678', type: 'Car' },
  { id: 'A-103', block: 'A', status: 'Available', resident: null, flat: null, vehicle: null, type: null },
  { id: 'A-104', block: 'A', status: 'Occupied', resident: 'Arjun Mehta', flat: 'A-104', vehicle: 'DL 03 EF 9012', type: 'Car' },
  { id: 'A-105', block: 'A', status: 'Available', resident: null, flat: null, vehicle: null, type: null },
  { id: 'B-101', block: 'B', status: 'Occupied', resident: 'Suresh Kumar', flat: 'B-201', vehicle: 'KA 04 GH 3456', type: 'Car' },
  { id: 'B-102', block: 'B', status: 'Occupied', resident: 'Meena Patel', flat: 'B-202', vehicle: 'MH 05 IJ 7890', type: 'Bike' },
  { id: 'B-103', block: 'B', status: 'Reserved', resident: null, flat: null, vehicle: null, type: null },
  { id: 'B-104', block: 'B', status: 'Occupied', resident: 'Sneha Rao', flat: 'B-204', vehicle: 'TN 06 KL 1234', type: 'Car' },
  { id: 'B-105', block: 'B', status: 'Available', resident: null, flat: null, vehicle: null, type: null },
  { id: 'C-101', block: 'C', status: 'Occupied', resident: 'Deepa Nair', flat: 'C-301', vehicle: 'KL 07 MN 5678', type: 'Car' },
  { id: 'C-102', block: 'C', status: 'Available', resident: null, flat: null, vehicle: null, type: null },
  { id: 'C-103', block: 'C', status: 'Occupied', resident: 'Amit Joshi', flat: 'C-302', vehicle: 'GJ 08 OP 9012', type: 'Car' },
  { id: 'C-104', block: 'C', status: 'Reserved', resident: null, flat: null, vehicle: null, type: null },
  { id: 'C-105', block: 'C', status: 'Available', resident: null, flat: null, vehicle: null, type: null },
]

// ── Family Members ──
export const familyMembers = [
  { id: 1, name: 'Priya Sharma', relation: 'Self', phone: '9876543210', age: 35 },
  { id: 2, name: 'Rohan Sharma', relation: 'Husband', phone: '9876543220', age: 38 },
  { id: 3, name: 'Aarav Sharma', relation: 'Son', phone: null, age: 10 },
  { id: 4, name: 'Kavya Sharma', relation: 'Daughter', phone: null, age: 7 },
]

// ── Notifications ──
export const notifications = [
  { id: 1, title: 'Complaint C-034 is in progress', description: 'Your complaint about water leakage has been assigned to the maintenance team.', time: '2 hours ago', type: 'complaint', read: false, date: 'Today' },
  { id: 2, title: 'Water supply maintenance on 21 May', description: 'Water supply will be shut down from 10:00 AM to 2:00 PM.', time: '4 hours ago', type: 'notice', read: false, date: 'Today' },
  { id: 3, title: 'New notice: Parking Rules Update', description: 'New parking rules have been posted. Please review the updated guidelines.', time: '6 hours ago', type: 'notice', read: true, date: 'Today' },
  { id: 4, title: 'Your booking with Ravi Plumber is confirmed', description: 'Service booking for 25 May, 10:00 AM has been confirmed.', time: '1 day ago', type: 'booking', read: true, date: 'Yesterday' },
  { id: 5, title: 'Event: Yoga Session tomorrow', description: 'Reminder: Yoga session is scheduled for tomorrow at 7:00 AM.', time: '1 day ago', type: 'event', read: true, date: 'Yesterday' },
  { id: 6, title: 'Maintenance bill generated', description: 'Your maintenance bill for May 2024 has been generated. Amount: ₹5,500.', time: '2 days ago', type: 'billing', read: true, date: 'Earlier' },
]

// ── Visitor Logs ──
export const visitorLogs = [
  { id: 1, name: 'Rakesh Sharma', purpose: 'Guest Visit', flat: 'A-101', entryTime: '2024-05-20 09:30 AM', exitTime: '2024-05-20 12:30 PM', vehicle: 'MH 01 XY 4567', status: 'Exited', approvedBy: 'Security Guard 1' },
  { id: 2, name: 'Delivery Boy (Swiggy)', purpose: 'Food Delivery', flat: 'B-202', entryTime: '2024-05-20 12:45 PM', exitTime: '2024-05-20 01:00 PM', vehicle: 'Bike', status: 'Exited', approvedBy: 'Security Guard 2' },
  { id: 3, name: 'Plumber - Ravi Kumar', purpose: 'Service', flat: 'C-301', entryTime: '2024-05-20 02:00 PM', exitTime: null, vehicle: null, status: 'Inside', approvedBy: 'Security Guard 1' },
  { id: 4, name: 'Seema Agarwal', purpose: 'Family Visit', flat: 'A-103', entryTime: '2024-05-20 03:15 PM', exitTime: null, vehicle: 'DL 02 AB 8901', status: 'Inside', approvedBy: 'Security Guard 2' },
  { id: 5, name: 'Courier (Amazon)', purpose: 'Package Delivery', flat: 'B-201', entryTime: '2024-05-20 10:00 AM', exitTime: '2024-05-20 10:15 AM', vehicle: 'Van', status: 'Exited', approvedBy: 'Security Guard 1' },
  { id: 6, name: 'Cable TV Technician', purpose: 'Service', flat: 'D-401', entryTime: '2024-05-20 11:30 AM', exitTime: '2024-05-20 01:00 PM', vehicle: null, status: 'Exited', approvedBy: 'Security Guard 2' },
  { id: 7, name: 'Mohan Singh', purpose: 'Guest Visit', flat: 'C-302', entryTime: '2024-05-19 04:00 PM', exitTime: '2024-05-19 08:00 PM', vehicle: 'UP 16 CD 2345', status: 'Exited', approvedBy: 'Security Guard 1' },
]

// ── Vehicle Logs ──
export const vehicleLogs = [
  { id: 1, vehicleNo: 'MH 01 AB 1234', type: 'Car', resident: 'Priya Sharma', flat: 'A-101', entry: '2024-05-20 08:00 AM', exit: null, status: 'Inside' },
  { id: 2, vehicleNo: 'MH 02 CD 5678', type: 'Car', resident: 'Rahul Verma', flat: 'A-102', entry: '2024-05-20 07:30 AM', exit: '2024-05-20 09:00 AM', status: 'Exited' },
  { id: 3, vehicleNo: 'DL 03 EF 9012', type: 'Car', resident: 'Arjun Mehta', flat: 'A-104', entry: '2024-05-20 06:45 AM', exit: null, status: 'Inside' },
  { id: 4, vehicleNo: 'KA 04 GH 3456', type: 'Car', resident: 'Suresh Kumar', flat: 'B-201', entry: '2024-05-20 09:15 AM', exit: '2024-05-20 06:00 PM', status: 'Exited' },
  { id: 5, vehicleNo: 'MH 05 IJ 7890', type: 'Bike', resident: 'Meena Patel', flat: 'B-202', entry: '2024-05-20 10:00 AM', exit: null, status: 'Inside' },
  { id: 6, vehicleNo: 'UP 16 AB 4521', type: 'Car', resident: 'Visitor', flat: 'C-302', entry: '2024-05-20 11:30 AM', exit: '2024-05-20 03:00 PM', status: 'Exited' },
]

// ── Management Committee ──
export const committeeMembers = [
  { id: 1, name: 'Ravi Sharma', role: 'President', phone: '9800000001' },
  { id: 2, name: 'Pooja Mehta', role: 'Vice President', phone: '9800000002' },
  { id: 3, name: 'Arpit Verma', role: 'Secretary', phone: '9800000003' },
  { id: 4, name: 'Neha Singh', role: 'Treasurer', phone: '9800000004' },
  { id: 5, name: 'Rohit Gupta', role: 'Joint Secretary', phone: '9800000005' },
]

// ── Facilities ──
export const facilities = [
  { id: 1, name: 'Club House', icon: '🏛️', description: 'Community gathering space with indoor games' },
  { id: 2, name: 'Swimming Pool', icon: '🏊', description: 'Olympic-size swimming pool with trained lifeguard' },
  { id: 3, name: 'Gym', icon: '💪', description: 'Fully equipped modern gymnasium' },
  { id: 4, name: 'Community Hall', icon: '🏢', description: 'Multi-purpose hall for events and meetings' },
  { id: 5, name: 'Guest Room', icon: '🛏️', description: 'Guest accommodation for visitors' },
  { id: 6, name: 'Tennis Court', icon: '🎾', description: 'Professional tennis court with floodlights' },
  { id: 7, name: 'Garden', icon: '🌿', description: 'Beautiful landscaped gardens and walking paths' },
  { id: 8, name: 'Parking', icon: '🅿️', description: 'Covered parking for cars and two-wheelers' },
]

// ── Maintenance Bills ──
export const maintenanceBills = [
  { id: 1, month: 'May 2024', amount: 5500, dueDate: '2024-05-15', status: 'Paid', paidDate: '2024-05-12' },
  { id: 2, month: 'April 2024', amount: 5500, dueDate: '2024-04-15', status: 'Paid', paidDate: '2024-04-10' },
  { id: 3, month: 'March 2024', amount: 5500, dueDate: '2024-03-15', status: 'Paid', paidDate: '2024-03-14' },
  { id: 4, month: 'June 2024', amount: 5500, dueDate: '2024-06-15', status: 'Unpaid', paidDate: null },
  { id: 5, month: 'February 2024', amount: 5000, dueDate: '2024-02-15', status: 'Paid', paidDate: '2024-02-13' },
  { id: 6, month: 'January 2024', amount: 5000, dueDate: '2024-01-15', status: 'Paid', paidDate: '2024-01-11' },
]

// ── Service Provider Bookings ──
export const providerBookings = [
  { id: 1, customer: 'Priya Sharma', flat: 'A-101', service: 'Pipe Fitting', date: '2024-05-25', time: '10:00 AM', status: 'Pending', amount: '₹800' },
  { id: 2, customer: 'Rahul Verma', flat: 'A-102', service: 'Plumbing Work', date: '2024-05-23', time: '2:00 PM', status: 'Accepted', amount: '₹1200' },
  { id: 3, customer: 'Anita Desai', flat: 'A-103', service: 'Bathroom Repair', date: '2024-05-22', time: '11:00 AM', status: 'Completed', amount: '₹2500' },
  { id: 4, customer: 'Suresh Kumar', flat: 'B-201', service: 'Pipe Fitting', date: '2024-05-20', time: '9:00 AM', status: 'Completed', amount: '₹600' },
  { id: 5, customer: 'Deepa Nair', flat: 'C-301', service: 'Plumbing Work', date: '2024-05-28', time: '3:00 PM', status: 'Pending', amount: '₹1500' },
]

// ── Reviews ──
export const reviews = [
  { id: 1, customer: 'Priya Sharma', rating: 5, comment: 'Excellent work! Fixed the leak quickly and professionally.', date: '2024-05-15' },
  { id: 2, customer: 'Rahul Verma', rating: 4, comment: 'Good service, arrived on time. Could improve cleanup after work.', date: '2024-05-10' },
  { id: 3, customer: 'Anita Desai', rating: 5, comment: 'Very skilled and polite. Highly recommended!', date: '2024-05-05' },
  { id: 4, customer: 'Meena Patel', rating: 4, comment: 'Did a good job. Slightly overpriced but quality work.', date: '2024-04-28' },
  { id: 5, customer: 'Vikram Singh', rating: 3, comment: 'Work was okay. Took longer than expected.', date: '2024-04-20' },
]

// ── FAQs ──
export const faqs = [
  { id: 1, question: 'How do I raise a complaint?', answer: 'Go to My Complaints section in the sidebar and click on "Raise New Complaint". Fill in the category, title, description, and optionally upload an image. Click "Submit Complaint" to register your complaint.' },
  { id: 2, question: 'How can I book an amenity?', answer: 'Navigate to Book Amenities from the sidebar. Select the facility, date, time slot, and purpose. Click "Book Now" to confirm your booking. You will receive a confirmation notification.' },
  { id: 3, question: 'How do I know my complaint status?', answer: 'Go to My Complaints page to see all your complaints with their current status. Click on any complaint to view detailed information and timeline updates.' },
  { id: 4, question: 'How do I update my profile?', answer: 'Click on "My Profile" in the sidebar. You can view your current information and click "Edit Profile" to update your details like phone number, email, and profile picture.' },
  { id: 5, question: 'How do I pay maintenance fees?', answer: 'Go to Maintenance Bills section. You can view all pending and past bills. Click "Pay Now" on any unpaid bill to make the payment through the integrated payment gateway.' },
]

// ── Incident Reports ──
export const incidentReports = [
  { id: 1, type: 'Theft', location: 'Parking Area B', description: 'Bicycle stolen from parking area.', severity: 'High', date: '2024-05-18', status: 'Under Investigation', reportedBy: 'Security Guard 1' },
  { id: 2, type: 'Vandalism', location: 'Garden Area', description: 'Garden bench damaged by unknown persons.', severity: 'Medium', date: '2024-05-15', status: 'Resolved', reportedBy: 'Security Guard 2' },
  { id: 3, type: 'Trespassing', location: 'Back Gate', description: 'Unauthorized person attempted entry through back gate.', severity: 'High', date: '2024-05-20', status: 'Under Investigation', reportedBy: 'Security Guard 1' },
]

// ── Emergency Alerts ──
export const emergencyAlerts = [
  { id: 1, title: 'Fire alarm test', priority: 'Low', date: '2024-05-12', time: '10:00 AM', description: 'Routine fire alarm testing. No action required.', status: 'Completed' },
  { id: 2, title: 'Water pipe burst - Block A', priority: 'Critical', date: '2024-05-18', time: '3:30 PM', description: 'Major water pipe burst in Block A basement. Maintenance team dispatched.', status: 'Resolved' },
  { id: 3, title: 'Power outage', priority: 'High', date: '2024-05-20', time: '7:00 PM', description: 'Scheduled power outage due to electrical maintenance. Generator backup active.', status: 'Active' },
]

// ── System Logs ──
export const systemLogs = [
  { id: 1, action: 'User Login', user: 'Admin', timestamp: '2024-05-20 09:00:00', details: 'Admin logged in from IP 192.168.1.100' },
  { id: 2, action: 'Complaint Created', user: 'Priya Sharma', timestamp: '2024-05-20 09:30:00', details: 'New complaint C-001 created' },
  { id: 3, action: 'Notice Published', user: 'Admin', timestamp: '2024-05-20 10:00:00', details: 'Notice: Water Supply Maintenance published' },
  { id: 4, action: 'Booking Created', user: 'Rahul Verma', timestamp: '2024-05-20 11:00:00', details: 'Gym booking for 22 May' },
  { id: 5, action: 'Complaint Updated', user: 'Admin', timestamp: '2024-05-20 14:00:00', details: 'Complaint C-001 assigned to Maintenance Team' },
  { id: 6, action: 'Visitor Entry', user: 'Security', timestamp: '2024-05-20 15:00:00', details: 'Visitor Rakesh Sharma entered for A-101' },
  { id: 7, action: 'Event Created', user: 'Admin', timestamp: '2024-05-19 16:00:00', details: 'Event: Yoga Session created' },
  { id: 8, action: 'User Registration', user: 'System', timestamp: '2024-05-19 10:00:00', details: 'New resident Rajesh Gupta registered' },
]

// ── Analytics Data ──
export const analyticsData = {
  complaintsOverTime: [
    { month: 'Jan', count: 12 },
    { month: 'Feb', count: 19 },
    { month: 'Mar', count: 15 },
    { month: 'Apr', count: 22 },
    { month: 'May', count: 18 },
    { month: 'Jun', count: 14 },
  ],
  complaintsByStatus: {
    'Open': 5,
    'In Progress': 8,
    'Resolved': 42,
    'Closed': 35,
    'Rejected': 3,
  },
  bookingsByService: {
    'Club House': 15,
    'Gym': 28,
    'Swimming Pool': 12,
    'Community Hall': 8,
    'Guest Room': 5,
    'Tennis Court': 10,
  },
  parkingUtilization: {
    'Occupied': 9,
    'Available': 4,
    'Reserved': 2,
  },
  monthlyRevenue: [
    { month: 'Jan', amount: 125000 },
    { month: 'Feb', amount: 130000 },
    { month: 'Mar', amount: 128000 },
    { month: 'Apr', amount: 135000 },
    { month: 'May', amount: 132000 },
    { month: 'Jun', amount: 140000 },
  ],
}

// ── Current User (simulated) ──
export const currentUser = {
  id: 1,
  name: 'Priya Sharma',
  email: 'resident@socioneed.com',
  password: '123456',
  phone: '9876543210',
  flat: 'A-101',
  role: 'resident',
  avatar: null,
  society: 'Green Valley Society',
  address: 'Green Avenue Society, Sector 45, Noida, UP 201301',
}

// ── Admin User ──
export const adminUser = {
  id: 100,
  name: 'Admin User',
  email: 'admin@socioneed.com',
  password: '123456',
  role: 'admin',
  avatar: null,
}

// ── Provider User ──
export const providerUser = {
  id: 1,
  name: 'Ravi Plumber',
  email: 'provider@socioneed.com',
  password: '123456',
  phone: '9111222333',
  role: 'provider',
  category: 'Plumber',
  avatar: null,
}

// ── Security User ──
export const securityUser = {
  id: 200,
  name: 'Ramesh Guard',
  email: 'security@socioneed.com',
  password: '123456',
  role: 'security',
  shift: 'Day (6 AM - 6 PM)',
  avatar: null,
}
