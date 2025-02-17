from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email_address: EmailStr


class UserUpdate(BaseModel):    
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email_address: Optional[EmailStr] = None

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email_address: EmailStr