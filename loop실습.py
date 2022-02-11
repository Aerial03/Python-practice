# while 구문을 이용한 10고개 숫자 퀴즈
from random import randint
answer = randint(1, 100)
tries = 1
while tries <= 10:
    guess = int(input('1~100 사이의 값을 입력하세요: '))
    if answer == guess:
        break
    elif guess > answer:
        print('down')
    elif tries > 10:
        break
    else:
        print('up')
    tries += 1
if tries <= 10:
    print('정답입니다. 정답 {}, 시도횟수: {}회'.format(answer, tries))
else:
    print('fail. 정답 {}, 시도횟수 {}회'.format(answer,tries))