import requests

from bs4 import BeautifulSoup

actno = int(input())
index = actno - 1
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

links = soup.find_all("a")
# print(len(links))
# for l in links:
#    print(l.get("href"))

print(links[index].get("href"))
