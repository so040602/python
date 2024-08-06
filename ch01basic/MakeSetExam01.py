coffess = set() # empty set(집합)

coffess.add('아메리카노')
coffess.add('100')
coffess.add('True')
coffess.add('아메리카노')

print(len(coffess))

coffess.clear()

coffess.add('아메리카노')
coffess.add('에스프레소')
coffess.add('믹스커피')
coffess.add('카페라떼')

newItem = ['콜드브루','고구마라떼','디카페인커피']
coffess.update(newItem)

# 집합은 순서가 없으므로, 인덱싱/슬라이싱이 불가능 합니다.
# print(coffees[3])

targetItem = '카푸치노'
bool = targetItem in coffess
print('%s 존재 여부 : %s' % (targetItem, bool))

targetItem = '마키야또'
if not targetItem in coffess:
    coffess.add(targetItem)

targetItem = '믹스커피'
coffess.remove(targetItem)

try:
    targetItem = '바닐라라떼'
    coffess.remove(targetItem)
except KeyError:
    print('%s는 목록에 존재하지 않습니다.' % targetItem)

print('반복문을 사용한 출력')
for element in coffess:
    print(element)
#end for

coffee01 = set(['고구마라떼','에스프레소','아메리카노','마키야또'])
coffee02 = set(['아메리카노','마키야또','카페라떼','디카페인커피'])

union_set = coffee01.union(coffee02)
print('합집합01 : %s' % union_set)

union_set = coffee01 | coffee02
print('합집합01 : %s' % union_set)

intersection_set = coffee01.intersection(coffee02)
print('교집합01 : %s' % intersection_set)

intersection_set = coffee01 & coffee02
print('교집합02 : %s' % intersection_set)

defference_set_01 = coffee01.difference(coffee02)
print('차집합 A-B : %s' % defference_set_01)

defference_set_02 = coffee02.difference(coffee01)
print('차집합 B-A : %s' % defference_set_02)

defference_set_01 = coffee01 - coffee02
print('차집합 A-B : %s' % defference_set_01)

defference_set_02 = coffee02 - coffee01
print('차집합 B-A : %s' % defference_set_02)

symmetric_defference_set = coffee01.symmetric_difference(coffee02)
print('차집합들의 합집합 : %s' % symmetric_defference_set)

super_set = set(['고구마라떼','에스프레소','아메리카노','마키야또'])
sub_set_01 = set(['고구마라떼','에스프레소'])
sub_set_02 = set(['바닐라라떼', '마키야또'])

boolTest = sub_set_01.issubset(super_set)
if boolTest :
    print('집합01은 슈퍼 집합의 부분 집합입니다.')
else:
    print('집합01은 슈퍼 집합의 부분 집합이 아닙니다.')
#end for

boolTest = sub_set_02.issubset(super_set)
if boolTest :
    print('집합02은 슈퍼 집합의 부분 집합입니다.')
else:
    print('집합02은 슈퍼 집합의 부분 집합이 아닙니다.')
#end for

boolTest = super_set.issuperset(sub_set_01)
if boolTest :
    print('super_set은 sub_set_01의 상위 집합입니다.')
else:
    print('super_set은 sub_set_01의 상위 집합이 아닙니다.')
#end for

boolTest = super_set.issuperset(sub_set_02)
if boolTest :
    print('super_set은 sub_set_02의 상위 집합입니다.')
else:
    print('super_set은 sub_set_02의 상위 집합이 아닙니다.')
#end for

print(coffess)