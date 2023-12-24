from typing import Annotated, Union
from fastapi import Body
from fastapi.routing import APIRouter
from models.users import New_Respons, User_BD, User_Public


command_router = APIRouter()

users_list = [User_BD(name = 'Ivanov', id = 115, password = '345345345'), User_BD(name = 'Petrov', id= 204, password = '612612612')]

def coder_psw(n : int):
    return str(n * 3) * 3

def find_user(id: int) -> Union[User_BD, None]:
    for user in users_list:
        if user.id == id:
            return user
    return None
    
@command_router.get("/users", response_model=Union[list[User_Public], None])
def get_users():
    '''
    Return all users
    '''
    return users_list

@command_router.get("/users/{id}", response_model=Union[User_Public, New_Respons])
def get_user(id: int):
    user = find_user(id)
    if user == None:
        return New_Respons(message = "Not find")
    return user

@command_router.post("/users", response_model=User_Public)
def create_user(item: Annotated[User_Public, Body(embed=True, description="new user")]):
    user = User_BD(name = item.name, id = item.id, password = coder_psw(item.id))
    users_list.append(user)
    return user

@command_router.put("/users", response_model= Union[User_Public, New_Respons])
def edit_person(item: Annotated[User_Public, Body(embed=True, description="edit user")]):
    user = find_user(item.id)
    if user == None:
        return New_Respons(message = "Not find")
    user.name = item.name
    return user

@command_router.delete("/users/{id}", response_model=Union[list[User_Public], None])
def delete_user(id : int):
    user = find_user(id)
    if user == None:
        return New_Respons(message = "Not find")
    users_list.remove(user)
    return users_list