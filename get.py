import requests
import urllib
import re

codeInput = input("What is your code? ")

def GetClip(code):
    url = 'http://unidev.hys.cz/includes/get-api'
    data = dict(code=code)

    r = requests.post(url, data=data, allow_redirects=True)
    responce = str(r.content)
    responce = responce.replace("'",'')
    return responce[1:]

print("Your URL:",GetClip(codeInput))