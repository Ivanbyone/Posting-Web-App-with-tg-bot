from fastapi import APIRouter, Form
from fastapi.responses import FileResponse
from database.database import send_post_to_mongo, show_post_from_mongo

router = APIRouter()


@router.get("/", tags=["Main"])
async def main_page() -> FileResponse:
    return FileResponse("templates/index.html")


@router.get("/api/posting", tags=["Posting"])
async def posting() -> FileResponse:
    return FileResponse("templates/posts.html")


@router.post("/api/posts", tags=["Posts"])
async def send_posted(text: str = Form(min_length=10,
                                     max_length=250)) -> dict:
    try:
        return {"Status 200": f"Post was created with id {send_post_to_mongo(text)}!"}
    except Exception as e:
        return {"Error": f"Creating post was failed with {e}!"}


@router.get("/api/posted/{id}")
async def show_post(id: int):
    try:
        post = show_post_from_mongo(id)
        return {"your post": f"{post.get('post')}",
                "liked": f"{post.get('liked')}",
                "disliked": f"{post.get('disliked')}"}
    except Exception as e:
        return {"error": f"Post with id {id} is not created with {e}"}
    