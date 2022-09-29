# DemoForm2.py
# DemoForm2.ui(화면) + 2.py(로직단)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

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

