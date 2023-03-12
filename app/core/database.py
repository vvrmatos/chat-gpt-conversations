import motor.motor_asyncio
from bson.objectid import ObjectId
from .config import db_settings

client = motor.motor_asyncio.AsyncIOMotorClient(db_settings.DATABASE_URL)

database = client[db_settings.DATABASE_NAME]


def serialize_id(document):
    document["id"] = str(document.pop("_id"))
    return document


async def get_collection(collection_name):
    return database[collection_name]


async def get_document_by_id(collection_name, document_id):
    collection = await get_collection(collection_name)
    document = await collection.find_one({"_id": ObjectId(document_id)})
    if document:
        return serialize_id(document)
    return None


async def create_document(collection_name, document_data):
    collection = await get_collection(collection_name)
    result = await collection.insert_one({'msg': document_data})
    return serialize_id({"_id": result.inserted_id, 'msg': document_data})


async def update_document(collection_name, document_id, document_data):
    collection = await get_collection(collection_name)
    await collection.update_one({"_id": ObjectId(document_id)}, {"$set": document_data})
    return await get_document_by_id(collection_name, document_id)


async def delete_document(collection_name, document_id):
    collection = await get_collection(collection_name)
    await collection.delete_one({"_id": ObjectId(document_id)})
