import asyncio
from core.chatgpt import get_response


asyncio.run(get_response('python', 'Write some Python code that prints Hello, World! Not using print'))
