# -*- coding: cp1251 -*-
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from command.command import command_router

app = FastAPI()
app.include_router(command_router)

@app.get('/', response_class= HTMLResponse)
async def f_index():
    return "FIO:Shulga Olga Vladimirovna"

