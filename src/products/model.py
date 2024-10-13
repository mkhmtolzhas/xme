from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    price: float
    rating: float
    image: str

    def to_bson(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'rating': self.rating,
            'image': self.image
        }