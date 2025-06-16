from schemas.models import CreateUser, User, CreateEvent, Event, CreateRegistration

# USER LOGIC
users = []
user_id_counter = 1

def create_user(user_data: CreateUser) -> User:
    global user_id_counter
    user = User(id=user_id_counter, name=user_data.name, email=user_data.email)
    users.append(user)
    user_id_counter += 1
    return user

def get_all_users() -> list[User]:
    return users

# EVENT LOGIC
events = []
event_id_counter = 1

def create_event(event_data: CreateEvent) -> Event:
    global event_id_counter
    event = Event(
        id=event_id_counter,
        title=event_data.title,
        date=event_data.date,
        location=event_data.location
    )
    events.append(event)
    event_id_counter += 1
    return event

def get_all_events() -> list[Event]:
    return events

# REGISTRATION LOGIC
registrations = []
registration_id_counter = 1  # Add an ID counter if needed

def register_user_to_event(reg_data: CreateRegistration):
    global registration_id_counter
    user_exists = any(user.id == reg_data.user_id for user in users)
    event_exists = any(event.id == reg_data.event_id for event in events)

    if not user_exists:
        raise ValueError("User not found.")
    if not event_exists:
        raise ValueError("Event not found.")

    registration = {
        "id": registration_id_counter,
        "user_id": reg_data.user_id,
        "event_id": reg_data.event_id,
        "attended": False
    }
    registrations.append(registration)
    registration_id_counter += 1
    return {"message": "Registration successful", "registration": registration}

def get_all_registrations():
    return registrations

def get_user_registrations(user_id: int):
    return [r for r in registrations if r["user_id"] == user_id]

def mark_attendance(registration_id: int):
    for reg in registrations:
        if reg["id"] == registration_id:
            reg["attended"] = True
            return {"message": "Attendance marked"}
    raise ValueError("Registration not found")
