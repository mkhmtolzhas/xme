from motor.motor_asyncio import AsyncIOMotorClient
from config import DATABASE_URL

client = AsyncIOMotorClient(DATABASE_URL)

db = client.xme

products_collection = db.get_collection("products")
offers_collection = db.get_collection("offers")