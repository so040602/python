import requests
from bs4 import BeautifulSoup

def is_article_link(link):
    # 링크가 기사 페이지인지 확인하는 간단한 방법
    return link and 'article.naver.com' in link

def crawl_news():
    url = 'https://news.naver.com/section/100'
    try:
        resp = requests.get(url)
        resp.raise_for_status()  # 요청이 성공했는지 확인
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return

resp = requests.get('https://news.naver.com/section/100')
html = resp.text

soup = BeautifulSoup(html, 'html.parser')

news_containers = soup.select('.section_article')

seen_titles = set()

for container in news_containers:
    articles = container.select('a')

    for article in articles:
        title = article.get_text(strip=True)
        link = article.get('href')

        if title in seen_titles:
            continue

        if is_article_link(link):
            if not link.startswith('http'):
                link = 'https://news.naver.com' + link

        print(f'Title : {title}')
        print(f'Link: {link}')

        seen_titles.add(title)

crawl_news()