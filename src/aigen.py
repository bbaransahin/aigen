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
new_convo = False
if ('-c' in sys.argv):
    file_name = sys.argv[sys.argv.index('-c')+1]
    sys.argv.pop(sys.argv.index('-c'))
    sys.argv.pop(sys.argv.index(file_name))
    coding = True

elif ('-n' in sys.argv):
    sys.argv.pop(sys.argv.index('-n'))
    new_convo = True

quest = ' '.join(sys.argv[1:])

def save_convo(convo):
    convo_file = open(os.path.expanduser('~/.aigen/convos/convo.txt'), "w+")
    convo_file.write("SPLITTOKEN".join(convo))
    convo_file.close()

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

elif (new_convo):
    convo = []
    convo.append(quest)
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt="\n".join(convo),
            temperature=0.7,
            max_tokens=256)

    convo.append(response['choices'][0]['text'])
    print(response['choices'][0]['text'])
    save_convo(convo)

else:
    try:
        convo_file = open(os.path.expanduser('~/.aigen/convos/convo.txt'), "r")
        convo = convo_file.read().split('SPLITTOKEN')
        convo_file.close()
    except:
        print("couldn't read convo file so creating new one")
        convo = []
    convo.append(quest)
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt="\n".join(convo),
            temperature=0.7,
            max_tokens=256)

    convo.append(response['choices'][0]['text'])
    print(response['choices'][0]['text'])
    save_convo(convo)
