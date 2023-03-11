import asyncio
from core.chatgpt import get_response


collection = input('Enter collection: ')
message = input('Enter message: ')

asyncio.run(get_response(collection=collection, message=message))
