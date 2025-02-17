from db import supabase
from models.user import User
from typing import List, Optional

class UserService:
    @staticmethod
    def get_all_users() -> List[dict]:
        response = supabase.table(User.TABLE_NAME).select("*").execute()
        if not response.data:
            return Exception(response.error.message)
        return response.data
    
    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[dict]:
        response = supabase.table(User.TABLE_NAME).select("*").eq("id", user_id).execute()
        data = response.data
        return data[0] if data else None
    
    @staticmethod
    def create_user(user: dict) -> dict:
        response = supabase.table(User.TABLE_NAME).insert(user.dict()).execute()
        if not response.data:
            raise Exception(response.error.message)
        return response.data[0]
    
    @staticmethod
    def update_user(user_id: int, user: dict) -> Optional[dict]:
        print(f"Supabase Data: {user.dict()}")
        print(f"User ID: {type(user_id) is int}")
        response = supabase.table(User.TABLE_NAME).update(user.dict()).eq("id", user_id).execute()
        data = response.data
        return data[0] if data else None
    
    @staticmethod
    def delete_user(user_id: int) -> bool:
        response = supabase.table(User.TABLE_NAME).delete().eq("id", user_id).execute()
        return True