import json
import csv
import pandas as pd



with open('D:\\PythonProject\\MyPython\\ch01basic\\정치_naver_news1.json', 'r', encoding='utf-8') as f1:
    json_politics_news = json.load(f1)

with open('D:\\PythonProject\\MyPython\\ch01basic\\경제_naver_news.json', 'r', encoding='utf-8') as f2:
    json_economys_news = json.load(f2)

with open('D:\\PythonProject\\MyPython\\ch01basic\\스포츠_naver_news.json', 'r', encoding='utf-8') as f3:
    json_sports_news = json.load(f3)

with open('D:\\PythonProject\\MyPython\\ch01basic\\it_naver_news.json', 'r', encoding='utf-8') as f4:
    json_its_news = json.load(f4)


# print(json.dumps(json_news, indent=4, sort_keys= True, ensure_ascii=False))

count = 0

naver_news = []
section_list = ['정치', '경제', 'IT', '스포츠']

for news in json_politics_news:
    count += 1
    title = news['title']
    section = '정치'
    link = news['link']
    pData = news['pDate']
    description = news['description']
    naver_news.append([count,title,section ,link, pData, description])
#end for

for news in json_economys_news:
    count += 1
    title = news['title']
    section = '경제'
    link = news['link']
    pData = news['pDate']
    description = news['description']
    naver_news.append([count,title,section ,link, pData, description])
#end for

for news in json_sports_news:
    count += 1
    title = news['title']
    section = '스포츠'
    link = news['link']
    pData = news['pDate']
    description = news['description']
    naver_news.append([count,title,section ,link, pData, description])
#end for

for news in json_its_news:
    count += 1
    title = news['title']
    section = 'IT'
    link = news['link']
    pData = news['pDate']
    description = news['description']
    naver_news.append([count,title,section ,link, pData, description])
#end for

print(json.dumps(naver_news, indent=4, ensure_ascii=False))

newsFrame = pd.DataFrame(naver_news)
newsFrame.columns = ['count', 'title', 'section', 'link', 'pDate', 'description']
newsFrame.head()
# headers = ['count','title','section' ,'link', 'pDate', 'description']
#
# newsFrame['count'] = '넘버'
# newsFrame['title'] = '제목'
# newsFrame['section'] = '섹션'
# newsFrame['link'] = '링크'
# newsFrame['pDate'] = '날짜'
# newsFrame['description'] = '설명'
#
# newsFrame= newsFrame[headers]

filename ='naver_news.csv'
newsFrame.to_csv(filename, encoding='utf-8-sig', index=False)
