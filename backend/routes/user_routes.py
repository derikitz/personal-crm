from fastapi import APIRouter, HTTPException
from services.user_service import UserService
from schemas.user_schema import UserCreate, UserUpdate, UserResponse
from typing import List

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
def get_users():
    users = UserService.get_all_users()
    return users

@router.get("/{user_id}", response_model=UserResponse)  
def get_user(user_id: int):
    user = UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    created_user = UserService.create_user(user)
    return created_user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    print("User Data:", user)
    updated_user = UserService.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail=updated_user)
    return updated_user

@router.delete("/{user_id}")
def delete_user(user_id: int):
    success = UserService.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}