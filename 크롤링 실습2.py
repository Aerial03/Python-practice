from bs4 import BeautifulSoup
import urllib.request as req  #request 모듈을 req로 줄여쓰겠다.

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

result = req.urlopen(url) #url열기
soup = BeautifulSoup(result, "html.parser") #데이터 분석하기
title = soup.find("title").string #title 추출하기
print(title)