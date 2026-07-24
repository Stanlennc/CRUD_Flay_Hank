from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_message():
    return {"message": "Hello World!"}