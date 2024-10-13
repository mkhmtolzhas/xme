from src.offers.service import OfferService
from src.offers.model import Offer
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["offers"])
service = OfferService()

@router.post("")
async def create_offer(offer: Offer):
    return await service.create_offer(offer)

@router.get("")
async def get_offers(page: int = 0, limit: int = 10):
    return await service.get_offers(page, limit)

@router.get("/all")
async def get_all_offers():
    return await service.get_all_offers()

@router.get("/{id}")
async def get_offer(id: str):
    offer = await service.get_offer(id)
    if offer:
        return offer
    raise HTTPException(status_code=404, detail="Offer not found")

@router.put("/{id}")
async def update_offer(id: str, offer: Offer):
    updated_offer = await service.update_offer(id, offer)
    if updated_offer:
        return updated_offer
    raise HTTPException(status_code=404, detail="Offer not found")

@router.delete("/{id}")
async def delete_offer(id: str):
    deleted_offer = await service.delete_offer(id)
    if deleted_offer:
        return deleted_offer
    raise HTTPException(status_code=404, detail="Offer not found")


