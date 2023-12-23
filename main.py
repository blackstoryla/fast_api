# -*- coding: cp1251 -*-
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"FIO":"Shulga Olga Vladimirovna"}

@app.get('/users')
async def f_index():
    return {"Phone":"+7 123 456 78 90"}

@app.get('/tools')
async def f_index():
    return{"Skills":"Different"}