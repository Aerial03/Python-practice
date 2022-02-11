from bs4 import BeautifulSoup
from urllib import request

url = "https://news.daum.net/"
result = request.urlopen(url)
soup = BeautifulSoup(result, "html.parser")
news = soup.select("strong.tit_g")
file = open("C:/PycharmProjects/python_base/news.txt", "w")

for list in news:
    a = list.select_one("a")
    print("링크: ", a.attrs["href"])
    file.write("링크: "+ a.attrs["href"] + "\n") # 줄바꿈하려면 엔터 필수
    title = a.string
    print("제목: "+title)
    file.write("제목: "+ title + "\n")
file.close()

# 파일 입출력
# file = open("C:/Users/효준/Desktop/basic.txt", "w") 열기
# file.write(("Hello Python")) 쓰기
# file.close() 닫기