# schemas/models.py

from pydantic import BaseModel
from datetime import datetime

class CreateUser(BaseModel):
    name: str
    email: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True  # Add this if you want to track active status

class CreateEvent(BaseModel):
    title: str
    location: str
    date: datetime

class Event(BaseModel):
    id: int
    title: str
    location: str
    date: datetime
    is_open: bool = True

class CreateRegistration(BaseModel):
    user_id: int
    event_id: int

class Registration(BaseModel):
    id: int
    user_id: int
    event_id: int
    registration_date: datetime
    attended: bool = False
