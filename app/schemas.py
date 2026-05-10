from pydantic import BaseModel
from fastapi_users import schemas
import uuid

class PostResponse(BaseModel):
    id: str
    caption: str
    url: str
    file_type: str
    file_name: str
    email: str
    is_owner: bool
    created_at: str
    
class UserRead(schemas.BaseUser[uuid.UUID]):
    pass
    
class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass
