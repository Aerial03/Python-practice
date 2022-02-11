# que 1
# special_words.txt 파일로부터 문자 'c'가 포함된 단어를 출력
# 단) 단어를 출력할 때 등장한 순서대로 출력
def que01():
    with open('./data/special_words.txt', 'r', encoding='utf-8') as file:
        lines = file.readline().split()
        lines = [i.strip(',.') for i in lines]
        for word in lines:
            if 'c' in word:
                print(word)
que01()

def que02():
    with open('./data/special_words.txt', 'r', encoding='utf-8') as file:
        cnt=0
        lines = file.readline().split()
        lines = [i.strip(',.') for i in lines]
        for word in lines:
            if len(word) <= 10:
                cnt += 1
        print('10이하인 단어의 개수: {}'.format(int(cnt)))
que02()

def que03():
    try:
        with open('./data/zipcode.txt', 'r', encoding='utf-8') as file:
            dong = input('동이름을 입력하시오: ')
            line = file.readline()
            while line:
                addr_lst = line.split('\t')
                if addr_lst[3].startswith(dong):
                    print(addr_lst)
                line = file.readline()
    except Exception as e:
        print(str(e))
que03()