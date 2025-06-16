from fastapi import FastAPI
from routes import users, events, registrations

app = FastAPI(title="Event Management API System")

# ✅ Welcome route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Event API 🎉"}

# Include routers from our routes folder
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(registrations.router, prefix="/registrations", tags=["Registrations"])
