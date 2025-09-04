from fastapi import APIRouter, HTTPException
from models import UserCreate, User

router = APIRouter()

# In-memory user store for demo purposes
users_db = {}
user_id_counter = 1

@router.post("/register", response_model=User)
def register_user(user: UserCreate):
    global user_id_counter
    for u in users_db.values():
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(id=user_id_counter, username=user.username, email=user.email)
    users_db[user_id_counter] = new_user
    user_id_counter += 1
    return new_user

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[User])
def list_users():
    return list(users_db.values())

@router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_id in users_db:
        del users_db[user_id]
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
