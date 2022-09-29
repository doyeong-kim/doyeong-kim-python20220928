# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open("c:\\work\\humor.txt", "wt", encoding="utf-8")
   

for n in range(1,11):
        #오늘의 유머 베스트 게시판 
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 꺠지는 경우 디코딩
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        #속성들(attrs)
        list = soup.find_all('td', attrs={'class':'subject'})
        # <td class="subject">
        # <a href="/board/view.php?table=bestofbest&amp;no=460111&amp;s_no=460111&amp;page=2" target="_top">수능정도는 유전자를 논하지말라는 일타강사.</a>
        # </td>
        for item in list:
                try:
                        title = item.find("a").text #a태그 없애고, 문자열 받아
                        print(title.strip())
                        # title = item.text.strip()
                        # #print(title)
                        # if (re.search('아이폰', title)):
                        #          print(title.strip())
                        #          f.write(title.strip() + "\n")
                except:
                        pass
        
f.close()