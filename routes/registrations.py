from fastapi import APIRouter, HTTPException
from schemas.models import CreateRegistration
from services.logics import (
    register_user_to_event,
    get_all_registrations,
    get_user_registrations,
    mark_attendance
)

router = APIRouter()

@router.post("/", status_code=201)
def register(registration: CreateRegistration):
    return register_user_to_event(registration)

@router.get("/", status_code=200)
def list_registrations():
    return get_all_registrations()

@router.get("/user/{user_id}")
def list_user_registrations(user_id: int):
    return get_user_registrations(user_id)

@router.patch("/attend/{registration_id}")
def attend_event(registration_id: int):
    return mark_attendance(registration_id)
