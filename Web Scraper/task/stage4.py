import requests
import string
from bs4 import BeautifulSoup

url = 'https://www.nature.com/nature/articles'
r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
# print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')

# get area where all items will come from
area = soup.find_all('article')
print(len(area))
print(area[0])

news = []
# first get article type
for i in area:
    article_type = i.find('span', {'class': 'c-meta__type'}).get_text()
    if article_type == "News":
        # then get follow link
        href = i.find('a').get('href')
        news.append(f"https://www.nature.com{href}")

for art in news:
    req_art = requests.get(art)
    soup2 = BeautifulSoup(req_art.content, 'html.parser')
    if req_art.status_code == 200:
        # get title
        title = soup2.find('h1', {'class':'c-article-magazine-title'}).get_text()
        # print(title)
        # format title
        final_title = title.strip().translate(title.maketrans('','',string.punctuation)).replace('‘','').replace("’",
                                                                                                     "").replace(' '
                                                                                                                   '','_')
        # print(f'{final_title}.txt')


        # get body
        body = soup2.find('div', {'class':'c-article-body'}).text
        # print(body)

        # save to file
        file = open(f'{final_title}.txt', 'w')
        file.write(body)
        file.close()