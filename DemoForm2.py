# DemoForm2.py
# DemoForm2.ui(화면) + 2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#화면
form_class = uic.loadUiType("Demoform2.ui")[0]

#클래스 정의(부모 클래스 변경)
class DemoForm(QMainWindow , form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #시그널 처리하는 슬롯 메서드
    def firstClick(self):
        self.label.setText("첫번째 버튼을 클릭")
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
        self.label.setText("네이버 웹툰을 크롤링 ")



    def secondClick(self):
        self.label.setText("두번째 버튼 클릭~~")  
    def thirdClick(self):
        self.label.setText("이번에는 세번째 버튼~~")  

#직접 모듈을 실행한 경우
if __name__ =="__main__":
    app = QApplication(sys.argv)
    demoWindow =DemoForm()
    demoWindow.show()
    app.exec_()

