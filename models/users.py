from pydantic import BaseModel, Field
from typing import Union, Annotated

class User_Public(BaseModel):
    name: Union[str, None] = None
    id: Annotated[Union[int, None],Field(default=100, ge=1, lt=400)]
    
class User_BD(User_Public):
    password: Annotated[Union[str, None], Field(max_length=50, min_length=8)]
    
class New_Respons(BaseModel):
    message: str
    