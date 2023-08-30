from instr import *
from second_win import *
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import(Qapplication, Qwidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)
class MainWin(Qwidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.btn_next = QpushButton(txt_next)
        self.hello_text = Qlabel(txt_hello)
        self.instruction = Qlabel(txt_instruction)
        
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment =Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment =Qt.AlignLeft)
        self.layout_line.addWidget(self.btn, alignment = Qt.AlignCenter)

    def next_click(self):
        self.tw = TestWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        pass
def main():
    app = QApplication([])
    mw = MainWin()
    app.exec_()

main()

