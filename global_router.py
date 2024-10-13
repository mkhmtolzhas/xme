from fastapi import APIRouter
from src.products.router import router as products_router
from src.offers.router import router as offers_router

router = APIRouter()

router.include_router(products_router, prefix="/products")
router.include_router(offers_router, prefix="/offers")

