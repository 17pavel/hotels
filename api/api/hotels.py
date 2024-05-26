
from fastapi import APIRouter, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

router = APIRouter()

class SBooking(BaseModel):
    room_id: int
    date_from: date 
    date_to: date
    stars: Optional[int] = Query(None, ge=1, le=5)
    


class SHotel(BaseModel):
    address: str
    name: str
    stars: int   

class HotelsArgs:
    def __init__(
        self,
        location: str,
        date_from: date, 
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = None
        ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa
        

@router.get("/hotels")
def get_hotels(search_args: HotelsArgs=Depends())->list[SHotel]:
    hotels = [
        {
            "address": "kemer",
            "name": "kylykia",
            "stars": 5,
            
        },
        {
            "address": "kemer",
            "name": "meder",
            "stars": 4,
            
        }
    ]
    return hotels
    

@router.post("/bookings")
def add_bookings(booking: SBooking):
    pass