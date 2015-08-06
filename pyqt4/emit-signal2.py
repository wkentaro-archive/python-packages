#-*- coding: utf-8 -*-
# emit-signal2.py
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def mousePressEvent(self, QMouseEvent):
        print QMouseEvent.pos()

    def mouseReleaseEvent(self, QMouseEvent):
        cursor =QtGui.QCursor()
        print cursor.pos()

    def initUI(self):
        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.clicked.connect(self.test)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(0, 0, 800, 540)
        self.setWindowTitle('Quit button')
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        # self.connect("clicked", self.test)
        self.show()

    def test(self):
        print "test"

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
