"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com
"""

import core
from ui_gui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow


class Zhihu(QMainWindow):
    '''
    爬虫
    '''
    def __init__(self, parent=None) -> None:
        '''
        the widget
        '''
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.pushButton.clicked.connect(self.getzhihu)
        self.ui.textEdit.setReadOnly(True)

    def getzhihu(self):
        '''
        get zhihu message
        '''
        self.ui.textEdit.clear()
        try:
            zhihu_question = self.ui.lineEdit.text()
            if zhihu_question == "":
                return
            answer = core.get_message(zhihu_question, self.ui.spinBox.value())
            self.ui.textEdit_2.setText(answer[1])
            for message in answer[0]:
                self.ui.textEdit.append(message)
        except:
            self.ui.textEdit.setText("Something happend")
        else:
            print("what else")

    def selfcancle(self):
        '''
        solve the warning
        '''
        self.close()
