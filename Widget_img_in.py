from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap, QImage
import ShowImg

class Widget_img_in(QWidget):
    
    loaded = QtCore.pyqtSignal(str)

    def __init__(self, ShowImg, parent = None):
        super(Widget_img_in, self).__init__(parent)
        self.setObjectName('Widget_img_in')
        self.ShowImg = ShowImg
        self.canvas = QLabel(self)
        self.canvas.resize(350, 350)
              
    def upd(self, evt):
        self.loaded.emit(self.ShowImg.loadInput())
        self.canvas.setPixmap(self.ShowImg.ShowInput())











