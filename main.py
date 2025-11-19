from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

# import from .env file
MONGO_URI = os.getenv("MONGO_URI")
# create client
client = AsyncIOMotorClient(MONGO_URI)
# from cliet go to db
db = client["euron_db"]
# from db go to collection
euron_data = db["euron_coll"]

app = FastAPI()

class eurondata(BaseModel):
    name : str
    phone: int | None = None
    city : str | None = None
    course : str | None = None

class eurondelete(BaseModel):
    name : str

class euronupdate(BaseModel):
    findvalue : str
    setvalue : str

@app.post("/euron/insert")
async def euron_data_insert_helper(data:eurondata):
    result = await euron_data.insert_one(data.dict())
    return {"message": f"data inserted for {result.inserted_id}"}

# to resolve ValueError: [TypeError("'ObjectId' object is not iterable"),

#  when mongo db is returning the document it is also returning _id (default key field) which has ObjectId() which is non-iterable hence the helper function is used to remove _id from the document and replace with id
def euron_helper(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

@app.get("/euron/getdata")
async def get_euron_data():
    items = []
    cursor = euron_data.find({})
    async for document in cursor:
        items.append(euron_helper(document))
    return items

@app.get("/euron/showdata")
async def show_euron_data():
    items = []
    cursor = euron_data.find({})
    async for document in cursor:
        items.append(euron_helper(document))
    return items

@app.post("/euron/deletedata")
async def delete_euron_data(to_delete:eurondelete):
    """You need to provide only name in order to delete"""
    query_filter = { "name": to_delete.name }
    # delete the document as selected via query_filter
    result = await euron_data.delete_one(query_filter)
    return {"message": f"No of documents deleted: {result.deleted_count}"}

@app.post("/euron/updatename")
async def update_euron_name(to_update:euronupdate):
    query_filter = {'name' : to_update.findvalue}
    update_operation = { '$set' : { 'name' : to_update.setvalue }}
    result = await euron_data.update_one(query_filter, update_operation)
    return {"message": f"No of documents found: {result.matched_count}\nNo of documents updated: {result.modified_count}"}