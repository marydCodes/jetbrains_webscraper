import requests
import json
from bs4 import BeautifulSoup

url = input("Input the URL: ")
# url = 'https://www.imdb.com/title/tt0080684/' #video.movie
# url = 'https://www.imdb.com/title/tt10048342/' #video.tv_show
# url = 'https://www.imdb.com/name/nm0001191/' #actor
# url = "https://www.google.com/"


r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
page_content = requests.get(url).content
print(r.status_code)

if r.status_code == 200:
    file = open('source.html', 'wb')
    file.write(page_content)
    file.close()
    print("Content saved.")
else:
    print(f"The URL returned {r.status_code}")