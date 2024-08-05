import random

answer = random.randint(1, 100)
print('정답 : %d' % answer)


count = 0

while True:
    num = int(input('1부터 100 사이의 정수 입력 : '))
    count += 1
    if answer > num:
        print('%d 보다 큰 수를 입력해 주세요.' %num)

    elif answer < num:
        print('%d보다 작은 수를 입력해 주세요. ' %num)
    else:
        print('정답을 맞추셨군요.')
        break;
    #end if
#end while

print('%d번만에 맞추었습니다.' % count)


