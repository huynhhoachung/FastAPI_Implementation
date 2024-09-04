from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = True
    is_admin: Optional[bool] = False

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class CompanyBase(BaseModel):
    name: str
    description: Optional[str] = None
    mode: Optional[str] = None
    rating: Optional[int] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    mode: Optional[str] = None
    rating: Optional[int] = None

class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    summarize: str
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    summarize: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[int] = None

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True