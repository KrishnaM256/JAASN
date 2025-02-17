from fastapi import FastAPI
from database import engine, Base
import routes

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI App
app = FastAPI()

# Include Routes
app.include_router(routes.router)
