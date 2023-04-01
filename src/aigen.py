#!/usr/bin/env python3

import sys
import os
import openai

# Load your API key from an environment variable or ask to user
openai.api_key = os.getenv("openaisk")
if (openai.api_key == None):
    print('Couldn\'t get the OpenAI API key. Please enter...')
    openai.api_key = input('API key=')
    print('To prevent this export your api key as environment variable named as openaisk.')

# Read argumants
'''
-c <filename> -> if you are coding, you should pass the whole file to get better results
'''
coding = False
if ('-c' in sys.argv):
    file_name = sys.argv[sys.argv.index('-c')+1]
    sys.argv.pop(sys.argv.index('-c'))
    sys.argv.pop(sys.argv.index(file_name))
    coding = True

quest = ' '.join(sys.argv[1:])

if (coding):
    pre_caption='this is the whole code I have:\n'
    file_content = open(file_name).read()+'\n'
    post_caption='\nimplement without comments.'

    def genCode():
        response = openai.Completion.create(
                model="text-davinci-003",
                prompt=pre_caption + file_content + quest + post_caption,
                temperature=0.7,
                max_tokens=256)

        return response['choices'][0]['text']

    print(genCode())

else:
    pass
