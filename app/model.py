from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    fullname: str = Field(...)
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Muhammad Ciko Wibowo",
                "username": "ciko",
                "password": "cikopass"
            }
        }

class UserLoginSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "ciko",
                "password": "cikopass"
            }
        }