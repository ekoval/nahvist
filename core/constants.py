TRIP_STATE_PLANNED = 'planned'
TRIP_STATE_CANCELLED = 'cancelled'
TRIP_STATE_FINISHED = 'finished'
TRIP_STATES = zip((EVENT_STATE_OPENED, EVENT_STATE_CANCELLED, EVENT_STATE_CLOSED),
                  ('Open', 'Cancelled', 'Closed'))



REQUEST_STATE_PENDING = 'pending'
REQUEST_STATE_APPROVED = 'approved'
REQUEST_STATE_REJECTED = 'rejected'
REQUEST_STATE_CANCELLED = 'cancelled'
REQUEST_STATES = zip((REQUEST_STATE_PENDING, REQUEST_STATE_APPROVED, REQUEST_STATE_REJECTED, REQUEST_STATE_CANCELLED),
                  ('Pending', 'Approved', 'Rejected', 'Cancelled'))



ROLE_DRIVER = 'driver'
ROLE_PASSENGER = 'passenger'
ROLES = zip((ROLE_DRIVER, ROLE_PASSENGER), ('Driver', 'Passenger'))
