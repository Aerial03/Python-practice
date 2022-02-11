# 영화목록 만들기 실습
movieLst = ['이터널스', '스파이더맨', '매트릭스', '경관의 피', '샹치', '스타워즈', '아이언맨']
print('type - ', type(movieLst))
print('data - ', movieLst)

'''
요구사항
1. 모가디슈를 추가
2. 스파이더맨과  매트릭스 사이에 임섭순을 추가
3. 경관의 피를 삭제
4. 매트릭스와 샹치를 삭제
5. 이터널스의 인덱스를 구해서 pop()함수를 이용한 삭제
6. 최종 리스트 출력
'''

movieLst.append('모가디슈') #1
print(movieLst)
movieLst.insert(2, '임섭순') #2
print(movieLst)
movieLst.remove('경관의 피') #3
print(movieLst)
del movieLst[3] #4
del movieLst[3] #동시에 삭제하려면 반복문 필요
print(movieLst)
idx = movieLst.index('이터널스') #5
movieLst.pop(idx)
print(movieLst) #6