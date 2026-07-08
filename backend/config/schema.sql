PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS societies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    pincode TEXT NOT NULL,
    contact_email TEXT,
    contact_phone TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    society_id INTEGER NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('admin', 'owner', 'tenant', 'service_provider', 'security')),
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT UNIQUE,
    password_hash TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'blocked')),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (society_id) REFERENCES societies(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS units (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    society_id INTEGER NOT NULL,
    block_name TEXT,
    unit_number TEXT NOT NULL,
    floor TEXT,
    unit_type TEXT,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'inactive')),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (society_id) REFERENCES societies(id) ON DELETE CASCADE,
    UNIQUE (society_id, block_name, unit_number)
);

CREATE TABLE IF NOT EXISTS resident_occupancies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    occupancy_type TEXT NOT NULL CHECK (occupancy_type IN ('owner', 'tenant')),
    start_date TEXT NOT NULL,
    end_date TEXT,
    is_primary INTEGER NOT NULL DEFAULT 1 CHECK (is_primary IN (0, 1)),
    FOREIGN KEY (unit_id) REFERENCES units(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS service_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS service_providers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL UNIQUE,
    category_id INTEGER NOT NULL,
    business_name TEXT NOT NULL,
    service_description TEXT,
    verification_status TEXT NOT NULL DEFAULT 'pending' CHECK (verification_status IN ('pending', 'approved', 'rejected')),
    rating_avg REAL NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES service_categories(id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS provider_slots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider_id INTEGER NOT NULL,
    slot_start TEXT NOT NULL,
    slot_end TEXT NOT NULL,
    is_available INTEGER NOT NULL DEFAULT 1 CHECK (is_available IN (0, 1)),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (provider_id) REFERENCES service_providers(id) ON DELETE CASCADE,
    UNIQUE (provider_id, slot_start, slot_end)
);

CREATE TABLE IF NOT EXISTS service_bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resident_user_id INTEGER NOT NULL,
    provider_id INTEGER NOT NULL,
    slot_id INTEGER,
    booking_status TEXT NOT NULL DEFAULT 'requested' CHECK (booking_status IN ('requested', 'accepted', 'declined', 'cancelled', 'completed')),
    request_notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (resident_user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES service_providers(id) ON DELETE CASCADE,
    FOREIGN KEY (slot_id) REFERENCES provider_slots(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS notices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    society_id INTEGER NOT NULL,
    created_by_user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    notice_type TEXT NOT NULL CHECK (notice_type IN ('general', 'maintenance', 'emergency', 'event')),
    priority TEXT NOT NULL DEFAULT 'normal' CHECK (priority IN ('low', 'normal', 'high', 'urgent')),
    publish_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expires_at TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (society_id) REFERENCES societies(id) ON DELETE CASCADE,
    FOREIGN KEY (created_by_user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    society_id INTEGER NOT NULL,
    created_by_user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    event_date TEXT NOT NULL,
    start_time TEXT,
    end_time TEXT,
    venue TEXT,
    status TEXT NOT NULL DEFAULT 'scheduled' CHECK (status IN ('scheduled', 'cancelled', 'completed')),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (society_id) REFERENCES societies(id) ON DELETE CASCADE,
    FOREIGN KEY (created_by_user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    society_id INTEGER NOT NULL,
    raised_by_user_id INTEGER NOT NULL,
    assigned_to_user_id INTEGER,
    subject TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    priority TEXT NOT NULL DEFAULT 'medium' CHECK (priority IN ('low', 'medium', 'high', 'urgent')),
    status TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'in_progress', 'resolved', 'closed')),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (society_id) REFERENCES societies(id) ON DELETE CASCADE,
    FOREIGN KEY (raised_by_user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (assigned_to_user_id) REFERENCES users(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS complaint_updates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    complaint_id INTEGER NOT NULL,
    updated_by_user_id INTEGER NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('open', 'in_progress', 'resolved', 'closed')),
    comment TEXT NOT NULL,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (complaint_id) REFERENCES complaints(id) ON DELETE CASCADE,
    FOREIGN KEY (updated_by_user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS parking_spaces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    society_id INTEGER NOT NULL,
    space_number TEXT NOT NULL,
    space_type TEXT NOT NULL CHECK (space_type IN ('resident', 'visitor', 'reserved')),
    current_status TEXT NOT NULL DEFAULT 'available' CHECK (current_status IN ('available', 'occupied', 'reserved', 'blocked')),
    assigned_unit_id INTEGER,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (society_id) REFERENCES societies(id) ON DELETE CASCADE,
    FOREIGN KEY (assigned_unit_id) REFERENCES units(id) ON DELETE SET NULL,
    UNIQUE (society_id, space_number)
);

CREATE TABLE IF NOT EXISTS parking_allocations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parking_space_id INTEGER NOT NULL,
    unit_id INTEGER NOT NULL,
    vehicle_number TEXT NOT NULL,
    allocated_by_user_id INTEGER NOT NULL,
    allocation_status TEXT NOT NULL DEFAULT 'active' CHECK (allocation_status IN ('active', 'released')),
    allocated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    released_at TEXT,
    FOREIGN KEY (parking_space_id) REFERENCES parking_spaces(id) ON DELETE CASCADE,
    FOREIGN KEY (unit_id) REFERENCES units(id) ON DELETE CASCADE,
    FOREIGN KEY (allocated_by_user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS visitor_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    society_id INTEGER NOT NULL,
    recorded_by_user_id INTEGER NOT NULL,
    resident_user_id INTEGER,
    visitor_name TEXT NOT NULL,
    vehicle_number TEXT,
    contact_number TEXT,
    entry_time TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    exit_time TEXT,
    parking_space_id INTEGER,
    remarks TEXT,
    FOREIGN KEY (society_id) REFERENCES societies(id) ON DELETE CASCADE,
    FOREIGN KEY (recorded_by_user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (resident_user_id) REFERENCES users(id) ON DELETE SET NULL,
    FOREIGN KEY (parking_space_id) REFERENCES parking_spaces(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS provider_reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider_id INTEGER NOT NULL,
    resident_user_id INTEGER NOT NULL,
    booking_id INTEGER,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    feedback TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (provider_id) REFERENCES service_providers(id) ON DELETE CASCADE,
    FOREIGN KEY (resident_user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (booking_id) REFERENCES service_bookings(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_users_society_role ON users(society_id, role);
CREATE INDEX IF NOT EXISTS idx_units_society ON units(society_id);
CREATE INDEX IF NOT EXISTS idx_bookings_provider_status ON service_bookings(provider_id, booking_status);
CREATE INDEX IF NOT EXISTS idx_complaints_status ON complaints(status);
CREATE INDEX IF NOT EXISTS idx_visitor_entries_time ON visitor_entries(society_id, entry_time);
