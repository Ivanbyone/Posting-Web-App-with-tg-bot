from fastapi import APIRouter
from . import controllers

main_router = APIRouter()
main_router.include_router(controllers.router)
