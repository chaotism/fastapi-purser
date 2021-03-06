from motor import motor_asyncio
from config import mongodb_config

client = motor_asyncio.AsyncIOMotorClient(mongodb_config.uri)
database = client[mongodb_config.db]
