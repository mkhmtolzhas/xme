from src.offers.model import Offer
from database import offers_collection
from bson import ObjectId

class OfferService:
    async def create_offer(self, offer: Offer):
        result = await offers_collection.insert_one(offer.to_bson())
        return str(result.inserted_id)

    async def get_offers(self, page: int, limit: int):
        cursor = offers_collection.find().skip(page * limit).limit(limit)
        documents = await cursor.to_list(length=limit)
        for document in documents:
            document["id"] = str(document["_id"])
            del document["_id"]
        return documents

    async def get_all_offers(self):
        cursor = offers_collection.find()
        documents = await cursor.to_list()
        for document in documents:
            document["id"] = str(document["_id"])
            del document["_id"]
        return documents

    async def get_offer(self, id: str):
        document = await offers_collection.find_one({"_id": ObjectId(id)})
        document["id"] = str(document["_id"])
        del document["_id"]
        return document

    async def update_offer(self, id: str, offer: Offer):
        result = await offers_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": offer.to_bson()}, return_document=True)
        if result:
            result["id"] = str(result["_id"])
            del result["_id"]
        return result

    async def delete_offer(self, id: str):
        result = await offers_collection.find_one_and_delete({"_id": ObjectId(id)})
        if result:
            result["id"] = str(result["_id"])
            del result["_id"]
        return result
