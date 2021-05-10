"""
mainwindow
"""
import sys
from PyQt5.QtWidgets import QApplication
import gui


app = QApplication(sys.argv)
zhihu = gui.Zhihu()
zhihu.show()
sys.exit(app.exec())
