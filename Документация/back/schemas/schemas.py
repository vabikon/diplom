# Pydantic schemas
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# MenuItem Schemas
class MenuItemBase(BaseModel):
    name: str
    category: str
    price: int
    weight: int
    composition: str
    description: str
    image: str
    featured: bool = False


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(MenuItemBase):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[int] = None
    weight: Optional[int] = None
    composition: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    featured: Optional[bool] = None


class MenuItem(MenuItemBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Review Schemas
class ReviewBase(BaseModel):
    name: str
    email: Optional[str] = None
    rating: int = 5
    text: str
    answer: Optional[str] = None


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(ReviewBase):
    name: Optional[str] = None
    email: Optional[str] = None
    rating: Optional[int] = None
    text: Optional[str] = None
    answer: Optional[str] = None


class Review(ReviewBase):
    id: int
    date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# GalleryImage Schemas
class GalleryImageBase(BaseModel):
    src: str
    alt: str
    description: str
    category: str


class GalleryImageCreate(GalleryImageBase):
    pass


class GalleryImageUpdate(GalleryImageBase):
    src: Optional[str] = None
    alt: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None


class GalleryImage(GalleryImageBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Order Schemas
from typing import Union
import json

class OrderBase(BaseModel):
    items: Union[List[dict], str]  # Может быть списком или JSON-строкой
    total: float
    customer_name: Optional[str] = "Гость"
    customer_phone: str
    customer_email: Optional[str] = None
    address: Optional[str] = None
    status: str = "pending"


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    items: Optional[List[dict]] = None
    total: Optional[float] = None
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None
    customer_email: Optional[str] = None
    address: Optional[str] = None
    status: Optional[str] = None


class Order(OrderBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

    @classmethod
    def validate_items(cls, v):
        if isinstance(v, str):
            try:
                import json
                return json.loads(v)
            except json.JSONDecodeError:
                return []
        return v


# User and Auth Schemas
class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    username: Optional[str] = None


class OrderStatusUpdate(BaseModel):
    status: str


class TableReservationBase(BaseModel):
    customer_phone: str
    reservation_type: str = "table_reservation"
    source: Optional[str] = None
    status: str = "pending"


class TableReservationCreate(BaseModel):
    customer_phone: str
    reservation_type: str = "table_reservation"
    source: Optional[str] = None


class TableReservation(TableReservationBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class TableReservationStatusUpdate(BaseModel):
    status: str
