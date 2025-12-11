from fastapi import APIRouter,HTTPException,status,Depends
from auth.securty import get_api_key

router = APIRouter()

@router.get("/")
def validate_key(api_key: str = Depends(get_api_key)):
    return{"message": "API Key is valid"}