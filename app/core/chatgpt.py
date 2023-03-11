#!/usr/bin/env python3

import os
import openai
from dotenv import dotenv_values
from app.core.config import gtp_settings
from app.core.database import create_document


def __set_gpt():
    if os.getenv('OPENAI_KEY'):
        openai.api_key = os.getenv('OPENAI_KEY')
    elif dotenv_values().get('OPENAI_KEY'):
        openai.api_key = dotenv_values().get('OPENAI_KEY')
    else:
        raise ValueError('No API Key found')


async def get_response(collection, message: str = ''):
    __set_gpt()

    response = openai.ChatCompletion.create(
        model=gtp_settings.MODEL,
        messages=[
                {'role': 'user', 'content': f'{message}'}
            ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    await create_document(collection_name=collection, document_data=response.choices[0].get('message').get('content'))

    print(result)
