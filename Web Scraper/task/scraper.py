#stage 5 out of 5

if __name__ == '__main__':
    import string
    import requests
    import os
    from bs4 import BeautifulSoup

    numpgs = int(input())
    article_type = input()

    # start_url = 'https://www.nature.com/nature/articles'
    for i in range(1, numpgs + 1):
        newdir = f'Page_{i}'
        os.mkdir(newdir)
        os.chdir(newdir)

        url = f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={i}"
        r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        # print(r.status_code)

        soup = BeautifulSoup(r.content, 'html.parser')

        # get area where all items will come from
        area = soup.find_all('article')

        news = []
        # first get article type
        for i in area:
            if i.find('span', {'class': 'c-meta__type'}).get_text() == article_type:
                #then get follow link
                href = i.find('a').get('href')
                news.append(f"https://www.nature.com{href}")

        for art in news:
            req_art = requests.get(art)
            if req_art.status_code == 200:
                soup2 = BeautifulSoup(req_art.content, 'html.parser')

                # get title
                title = soup2.find('h1', {'itemprop': 'headline'}).get_text()
                # print(title)
                # format title
                final_title = title.strip().translate(title.maketrans('', '', string.punctuation)).replace('‘', '').replace("’","").replace(' ', '_')
                # print(f'{final_title}.txt')

                # get body
                try:
                    body = soup2.find('div', {'class': 'c-article-body'}).text.strip()
                except:
                    body = soup2.find('div', {'class': 'article-item__body'}).text.strip()
                # print(body)

                # save to file
                file = open(f'{final_title}.txt', 'wb')
                try:
                    file.write(body.encode('utf-8'))
                except:
                    pass
                file.close()
        os.chdir(r"C:\Users\emade\PycharmProjects\Web Scraper\Web Scraper\task")