from PySide.QtCore import *
from PySide.QtGui import *
from widget import simpleSceneScene
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Simple Scene')


class simpleViewClass(QGraphicsView):
    def __init__(self):
        super(simpleViewClass, self).__init__()
        self.setWindowIcon(QIcon(r"widget\sun.png"))
        self.setWindowTitle("Simple Sunny Scene")
        self.scene = simpleSceneScene.simpleSceneClass()
        self.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication([])
    window = simpleViewClass()
    window.show()
    app.exec_()