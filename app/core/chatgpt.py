#!/usr/bin/env python3

import os
import sys
import asyncio
import openai
from dotenv import dotenv_values
from .config import gtp_settings
from .database import create_document


success_message = 'Saved successfully'
bye_message = 'Bye!'

def __set_gpt():
    if os.getenv('OPENAI_KEY'):
        openai.api_key = os.getenv('OPENAI_KEY')
    elif dotenv_values().get('OPENAI_KEY'):
        openai.api_key = dotenv_values().get('OPENAI_KEY')
    else:
        raise ValueError('No API Key found')


async def get_response(choice, collection, user_prompt: str = ''):
    __set_gpt()

    match choice:
        case 'image generator':
            response = openai.Image.create(
                prompt=user_prompt,
                n=1,
                size='1024x1024'
            )
            image_url = response['data'][0]['url']
            print(image_url)

            user_input = input('Save Chat Response (Y/n)? ').lower()

            if user_input or user_input[0] == 'y':
                await create_document(collection_name=collection, document_data=image_url)
                print(success_message)

            print(bye_message)

        case 'chat completion':
            response = openai.ChatCompletion.create(
                model=gtp_settings.MODEL,
                messages=[
                        {'role': 'user', 'content': f'{user_prompt}'}
                    ]
            )

            result = ''
            for choice in response.choices:
                result += choice.message.content

            print(result)

            user_input = input('Save Chat Response (y/n)? ').lower()
            if user_input and user_input[0] == 'y':
                await create_document(collection_name=collection,
                                  document_data=response.choices[0].get('message').get('content'))
                print(success_message)

            print(bye_message)


def start():
    print('** Welcome **')
    print('** Choose One Of The Options **')

    services = {
        '1': 'image generator',
        '2': 'chat completion'
    }

    for option in services:
        print(option, services.get(option).title(), sep=' - ')

    choice = services.get(input('> '))
    if not services:
        sys.exit()

    collection = input('Enter collection: ').lower()
    prompt = input('Enter prompt: ')

    asyncio.run(get_response(choice=choice, collection=collection, user_prompt=prompt))
