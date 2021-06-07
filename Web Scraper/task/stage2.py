import requests
import json
from bs4 import BeautifulSoup


url = input()
#url = 'https://www.imdb.com/title/tt0080684/' #video.movie
#url = 'https://www.imdb.com/title/tt10048342/' #video.tv_show
#url = 'https://www.imdb.com/name/nm0001191/' #actor
#url = "https://www.google.com/"


r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
soup = BeautifulSoup(r.content, 'html.parser')

title = soup.title.text
metatags = soup.find("meta", property = "og:type")
metacontent = metatags["content"]
a = soup.find("meta", property="og:description")
description = a['content']
a_dict = {}

if ".movie" in metacontent or ".tv_show" in metacontent:
    print(metacontent)
    a_dict["title"] = title
    a_dict["description"] = description

    print(a_dict)
else:
    print("Invalid movie page!")