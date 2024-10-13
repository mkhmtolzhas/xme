from src.products.service import ProductService
from src.products.model import Product
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["products"])
service = ProductService()

@router.post("")
async def create_product(product: Product):
    return await service.create_product(product)

@router.get("")
async def get_products(page: int = 0, limit: int = 10):
    return await service.get_products(page, limit)


@router.get("/{id}")
async def get_product(id: str):
    product = await service.get_product(id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.put("/{id}")
async def update_product(id: str, product: Product):
    updated_product = await service.update_product(id, product)
    if updated_product:
        return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/{id}")
async def delete_product(id: str):
    deleted_product = await service.delete_product(id)
    if deleted_product:
        return deleted_product
    raise HTTPException(status_code=404, detail="Product not found")
