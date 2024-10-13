from pydantic import BaseModel
from typing import Optional

class Offer(BaseModel):
    id: Optional[int] = None
    text: str

    def to_bson(self):
        return {
            'text': self.text
        }