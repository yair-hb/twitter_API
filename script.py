from enum import Flag
from fileinput import filename
from random import random
from tabnanny import filename_only
from textwrap import indent
from urllib import request
from cv2 import sort
import tweepy
import json
import os

with open('dataset.json') as f:
    data = json.load(f)

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('','')

api = tweepy.API(auth)

char = 0
while data[char]['appear'] == 'True':
    char = int(random.uniform(0, len(data)))
    if data [char]['appear'] == 'False':
        data[char]['appear'] == 'True'
        break

with open ('dataset.json','w') as f:
    f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',',': ')))

height_in_foot = round(float(data[char]['height'][0:4])*3.281,3)

msg = f"RT si mides más que {data[char]['name']} --> {data[char]['height']}\n\nRT if you're taller than {data[char]['name']} --> {height_in_foot} ft"

filename="temp.jpg"
request = request.get(data[char]['img'], stream=True)
if request.status_code == 200:
    with open(filename, 'wb') as image:
        for chunk in request:
            image.write(chunk)

api.update_with_media(filename, msg)

os.remove('temp.jpg')