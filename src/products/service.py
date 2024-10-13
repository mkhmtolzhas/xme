from src.products.model import Product
from database import products_collection
from bson import ObjectId

class ProductService:
    async def create_product(self, product: Product):
        result = await products_collection.insert_one(product.to_bson())
        return str(result.inserted_id)

    async def get_products(self, page: int, limit: int):
        cursor = products_collection.find().skip(page * limit).limit(limit)
        documents = await cursor.to_list(length=limit)
        for document in documents:
            document["id"] = str(document["_id"])
        return documents

    async def get_all_products(self):
        cursor = products_collection.find()
        documents = await cursor.to_list()
        for document in documents:
            document["id"] = str(document["_id"])
        return documents

    async def get_product(self, id: str):
        document = await products_collection.find_one({"_id": ObjectId(id)})
        document["id"] = str(document["_id"])
        return document

    async def update_product(self, id: str, product: Product):
        result = await products_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": product.to_bson()}, return_document=True)
        if result:
            result["id"] = str(result["_id"])
        return result

    async def delete_product(self, id: str):
        result = await products_collection.find_one_and_delete({"_id": ObjectId(id)})
        if result:
            result["id"] = str(result["_id"])
        return result