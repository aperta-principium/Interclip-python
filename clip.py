import requests
import urllib
import re
urlInput = input("What is your URL? ")
def Clip(inputUrl):

    url = 'http://unidev.hys.cz/includes/api'
    data = dict(url=inputUrl)

    r = requests.post(url, data=data, allow_redirects=True)
    responce = str(r.content)
    responce = responce.replace("'",'')
    return responce[1:]

print("Your code:",Clip(urlInput))