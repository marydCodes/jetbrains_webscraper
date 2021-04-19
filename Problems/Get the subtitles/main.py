import requests
from bs4 import BeautifulSoup

index = int(input())
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

sections = soup.find_all("h2")
#print(len(sections))
#for s in sections:
#    print(s.text, "\n")
print(sections[index].text)
