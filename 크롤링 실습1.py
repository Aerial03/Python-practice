from bs4 import BeautifulSoup

html = """
<html>
<head>
    <title>파이썬 웹 크롤링</title>
</head>
<body>
    <h1 id="title">안녕하세요</h1>
    <p id="name">루나입니다.</p>
    <ul>
        <li>
            <a href="http://www.naver.com">네이버</a>
        </li>
        <li>
            <a href="http://www.google.com">구글</a>
        </li>
    </ul>
</body>
</html>
"""

# html 태그 분석
soup = BeautifulSoup(html, 'html.parser')
h1 = soup.html.body.h1 #데이터 위치 찾는 방법
p = soup.html.body.p #데이터 위치 찾는 방법

print("h1: ", h1.string) #.string: 양 옆의 <> 제거
print("p: " , p.string)

# find 함수
title = soup.find("h1")
name = soup.find("p")

print("title: ", title.string)
print("name: ", name.string)

# find_all 함수, 데이터를 찾아서 리스트에 저장
list = soup.find_all("a")
for a in list: # 데이터 추출
    text = a.string # 글자만 추출
    href = a.attrs["href"] # 링크만 추출
    print(text)
    print(href)

# print(list[0]) 단순히 리스트로 출력
# print(list[1])