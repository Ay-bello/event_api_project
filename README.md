# 🎉 Event Management API System

# Description
This system allows users to register for events, track attendance, and manage both event and speaker information. It supports CRUD operations and uses in-memory data storage for demonstration purposes.

---

# Entities

# User
- `id`: Unique identifier
- `name`: Full name
- `email`: Email address
- `is_active`: Boolean (default: True)

# Event
- `id`: Unique identifier
- `title`: Name of the event
- `location`: Location
- `date`: Date of the event
- `is_open`: Boolean (default: True)

# Speaker
- `id`: Unique identifier
- `name`: Name of the speaker
- `topic`: Topic presented

# Registration
- `id`: Unique identifier
- `user_id`: User's ID
- `event_id`: Event's ID
- `registration_date`: Date registered
- `attended`: Boolean (default: False)

---

# API Endpoints

# **User Endpoints**
- `GET /users/` – List all users
- `POST /users/` – Create a new user

# **Event Endpoints**
- `GET /events/` – List all events
- `POST /events/` – Create a new event

# **Speaker Endpoints**
- `GET /speakers/` – List all initialized speakers (3 speakers are added on app startup)

# **Registration Endpoints**
- `GET /registrations/` – List all registrations
- `POST /registrations/` – Register a user for an event
- `GET /registrations/user/{user_id}` – View a user's registrations
- `PATCH /registrations/attend/{registration_id}` – Mark attendance

---

# Technical Requirements

- Built with **FastAPI**
- Uses **Pydantic** for data validation
- Data is stored using **in-memory lists**
- Follows a modular folder structure:
  - `main.py`
  - `routes/`
  - `schemas/`
  - `services/`
- Proper HTTP status codes are returned

---

#  How to Run This Project

```bash
# 1️. Clone the repository
git clone https://github.com/Ay-bello/event-management-api.git
cd event-management-api

# 2️, (Optional) Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3️. Install dependencies
pip install fastapi uvicorn

# 4. Run the FastAPI app
uvicorn main:app --reload
