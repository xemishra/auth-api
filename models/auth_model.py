from pydantic import BaseModel, Field, EmailStr, ValidationInfo, field_validator

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=2)
    name: str = Field(..., min_length=2)
    confirm_password: str = Field(..., min_length=2)

    @field_validator("confirm_password")
    @classmethod
    def validate_confirm_password(cls, value: str, info: ValidationInfo):
        if "password" in info.data and value != info.data["password"]:
            raise ValueError("Passwords do not match")
        return value
    
class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=2)