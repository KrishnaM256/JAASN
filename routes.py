from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate, UserLogin, UserResponse
from auth import hash_password, verify_password, create_access_token
from datetime import timedelta

router = APIRouter()

# User Registration
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password),
        is_admin=False  # Default to user
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Admin Registration (Manually set admin)
@router.post("/register-admin", response_model=UserResponse)
def register_admin(user: UserCreate, db: Session = Depends(get_db)):
    new_admin = User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password),
        is_admin=True  # Set admin flag
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

# User Login
@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Generate JWT Token
    access_token = create_access_token(
        data={"sub": db_user.email, "is_admin": db_user.is_admin},
        expires_delta=timedelta(minutes=30)
    )

    # Debugging: Log successful login
    print(f"Login successful for {db_user.name}")  # This will show in FastAPI logs

    # Return name along with other details
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "is_admin": db_user.is_admin,
        "name": db_user.name  # Ensure 'name' is included here
    }
