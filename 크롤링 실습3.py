from bs4 import BeautifulSoup
from urllib import request

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("도시: ", location.select_one("city").string)
    print("날씨: ", location.select_one("wf").string)
    print("현재 시간: ", location.select_one("tmEF").string)
    print("최저기온: {}도".format(location.select_one("tmn").string))
    print("최고기온: {}도".format(location.select_one("tmx").string))
    print()