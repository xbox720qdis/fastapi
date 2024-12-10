from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)  # Correct UUID generation
    first_name: str
    last_name: str
    middle_name: Optional[str] = None  # Optional field with a default value
    gender: Gender
    roles: List[Role]


#we need to creqate a product

class Product(BaseModel):
    id: int 
    name: str
    price: float
    