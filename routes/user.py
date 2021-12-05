from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post("/users")
def create_user(user: User):
    return "User.py"


@user.get("/users")
def home():
    return "User.py"


@user.get("/users")
def home():
    return "User.py"

@user.get("/users")
def home():
    return "User.py"