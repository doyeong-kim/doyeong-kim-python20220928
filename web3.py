#web2.py

#웹서버서 요청
from os import link
import urllib.request
#크롤링
from bs4 import BeautifulSoup
#파일에 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
#페이징처리(한페이지에 10개)
for i in range(1,6):
    url = \
    "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page=" + str(i)
    print(url)
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")
    for item in cartoons:
        title = item.find("a").text.strip()
        print(title)
        f.write(title + "\n")
    # title = cartoons[0].find("a").text
    # link = cartoons[0].find("a")["href"]
    # print(title)
    # print(link)
    # print("개수 :{0}".format(len(cartoons)))

#http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri

# <td class="title">
#      <a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" onclick="nclk_v2(event,'lst.title','20853','50')">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
f.close()
    