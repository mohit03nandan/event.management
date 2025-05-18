from pydantic import BaseModel

class UserSignupSchema(BaseModel):
    username: str
    password: str