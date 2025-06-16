from fastapi import APIRouter
from schemas.models import CreateUser, User
from services.logics import create_user, get_all_users

router = APIRouter()

@router.post("/", response_model=User)
def add_user(user: CreateUser):
    return create_user(user)

@router.get("/", response_model=list[User])
def list_users():
    return get_all_users()
