#!/usr/bin/env python3

import sys
import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("openaisk")
if (openai.api_key == None):
    print('Couldn\'t get the OpenAI API key. Please enter...')
    openai.api_key = input('API key=')

pre_caption='this is the whole code I have:\n'

file_content = open(sys.argv[1]).read()

post_caption='\nimplement without comments.'

def genCode():
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=pre_caption + file_content +'\n'.join(sys.argv[2:]) + post_caption,
            temperature=0.7,
            max_tokens=256)

    return response['choices'][0]['text']

print(genCode())
