from fastapi import APIRouter
from schemas.models import CreateEvent, Event
from services.logics import create_event, get_all_events

router = APIRouter()

@router.post("/", response_model=Event)
def add_event(event: CreateEvent):
    return create_event(event)

@router.get("/", response_model=list[Event])
def list_events():
    return get_all_events()
