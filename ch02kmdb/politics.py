
import json
import urllib.request
import urllib.parse
import datetime
import time


def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id','vJwkgT18tOP_0fDvs3I5')
    req.add_header("X-Naver-Client-Secret",'byeK_KpM5i')
    # req.add_header("Content-Type", "application/json")

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s]Url Request Success' % datetime.datetime.now())
            return response.read().decode('utf-8')

    except Exception as e :
        print(e)
        print('[%s] Error for URL : %s' % (datetime.datetime.now(), url))
        return None

def getNaverSearch(node, srcText, display, start):
    base = 'https://openapi.naver.com/v1/search'
    node1 = '/%s.json' % node
    parameters = '?query=%s&display=%s&start=%s' % (urllib.parse.quote(srcText), display, start)
    print(urllib.parse.quote(srcText))
    url = base + node1 + parameters
    responseDecode = getRequestUrl(url)
    print(url)
    if responseDecode is None:
        print("Failed to decode the response.")
        return None
    else:
        return json.loads(responseDecode)

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({
        'cnt':cnt,
        'title':title,
        'description':description,
        'org_link':org_link,
        'link':link,
        'pDate':pDate
    })
    return

def main():
    node = 'news'
    srcText = '정치'
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 100, 1)
    total = jsonResponse.get('total', 0)

    while((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt +=1
            getPostData(post, jsonResult, cnt)

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, 100, start)

    print('전체 검색 : %d 건' %total)

    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf-8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys= True, ensure_ascii=False)

        outfile.write(jsonFile)

    print("가져온 데이터 : %d 건" % (cnt))
    print('%s_naver_%s.json SAVED' % (srcText, node))

    # start = 1
    # display = 100
    # while True:
    #     jsonResponse = getNaverSearch(node, srcText, start, display)
    #     if not jsonResponse:
    #         print("No data retrieved or error occurred.")
    #         break
    #
    #     total = jsonResponse.get('total', 0)
    #     if jsonResponse.get('display', 0) == 0:
    #         break
    #
    #     for post in jsonResponse.get('items', []):
    #         cnt += 1
    #         getPostData(post, jsonResult, cnt)
    #
    #     # Move to the next page
    #     start += display
    #
    # print('전체 검색 : %d 건' % total)
    #
    # file_name = '%s_naver_%s.json' % (srcText, node)
    # try:
    #     with open(file_name, 'w', encoding='utf-8') as outfile:
    #         jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    #         outfile.write(jsonFile)
    #     print(f"{file_name} SAVED")
    # except IOError as e:
    #     print(f"File save error: {e}")
    #
    # print("가져온 데이터 : %d 건" % cnt)

if __name__ == '__main__':
    main()
