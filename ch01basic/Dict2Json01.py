
humanDict = {
    'age':20, 'name':'유현식', 'hobby':'독서',
    'address':{'city':'seoul', 'gu':'마포구', 'ziocode':'12345'}
}

print(type(humanDict))
print(humanDict)

import json
humanString = json.dumps(humanDict, ensure_ascii=False, indent=4, sort_keys=True) #사전을 문자열로 변환, indent 들여쓰기, sort_keys 정렬
print(type(humanString))
print(humanString)

humanJson = json.loads(humanString)

print('출력 결과')
print('이름 : %s' % humanJson['name'])
print('취미 : %s' % humanJson['hobby'])
print('나이 : %d' % humanJson['age'])
print('시도 : %s' % humanJson['address']['city'])
print('군구 : %s' % humanJson['address']['gu'])
print('우편 번호 : %s' % humanJson['address']['ziocode'])