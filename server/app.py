import logging
import uvicorn

from fastapi import FastAPI
from config.config import *
import controllers


def create_app() -> FastAPI:
    posts_app = FastAPI(
        title=PROJECT_NAME,
        description="Operations with users posts",
        version="0.0.1",
        contact={
            "name": "Ivanbyone",
            "email": "ivanbyone@gmail.com"
        }
    )

    return posts_app


app = create_app()

app.include_router(controllers.main_router)


if __name__ == "__main__":
    try:
        uvicorn.run("app:app", 
                    host=HOST, 
                    port=PORT, 
                    reload=False)
    except Exception as e:
        logging.info(f"App stoped with {e}")
