from PySide.QtCore import *
from PySide.QtGui import *
from widget import colorPickerUI2_ps as ui
from widget import gradientWidget, cubesWidget
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Color Picker')


class colorPickerClass(QMainWindow, ui.Ui_ColorPicker):
    def __init__(self):
        super(colorPickerClass, self).__init__()
        self.setupUi(self)
        self.setFixedSize(QSize(550, 505))
        self.setWindowIcon(QIcon(r"widget\app.png"))

        self.gradient_widget = gradientWidget.gradientWidget()
        self.gridLayout.addWidget(self.gradient_widget, 1, 1, 2, 2)
        self.cubesWidget = cubesWidget.cubesWidget()
        self.gridLayout.addWidget(self.cubesWidget, 1, 3, 2, 1)

        self.prev_color = None
        self.curr_color = None

        self.prev_lbl.setMinimumHeight(40)
        self.prev_lbl.setMaximumWidth(195)
        self.curr_lbl.setMinimumHeight(40)
        self.curr_lbl.setMaximumWidth(195)
        self.curr_lbl.setAutoFillBackground(True)
        self.prev_lbl.setAutoFillBackground(True)

        palette1 = self.curr_lbl.palette()
        palette1.setColor(self.curr_lbl.backgroundRole(), Qt.white)
        self.curr_lbl.setPalette(palette1)
        palette2 = self.prev_lbl.palette()
        palette2.setColor(self.prev_lbl.backgroundRole(), Qt.white)
        self.prev_lbl.setPalette(palette2)

        self.rgb_lbl.setText("R:        G:         B:        ")
        self.hex_lbl.setText("#")
        self.value_sld.setValue(255)
        self.value_sld_value_lbl.setText("Value: 255")

        self.value_sld.valueChanged.connect(self.showValue)
        self.value_sld.valueChanged.connect(self.gradient_widget.updateHSVValue)
        self.gradient_widget.colorChangedSignal.connect(self.updateColor)
        self.cubesWidget.colorCubeSignal.connect(self.gradient_widget.setMarker)
        self.cubesWidget.colorCubeSignal.connect(self.defineValue)
        self.cubesWidget.colorCubeSignal.connect(self.setRGB)

    def showValue(self, value):
        text = "Value: {0}".format(str(value))
        self.value_sld_value_lbl.setText(text)

    def defineValue(self):
        value = self.cubesWidget.setValue
        if value is not None:
            self.value_sld.setValue(value)

    def updateColor(self, color):
        if self.prev_color:
            palettePrev = self.prev_lbl.palette()
            palettePrev.setColor(self.prev_lbl.backgroundRole(), self.prev_color)
            self.prev_lbl.setPalette(palettePrev)
        paletteCurr = self.curr_lbl.palette()
        paletteCurr.setColor(self.curr_lbl.backgroundRole(), color)
        self.curr_lbl.setPalette(paletteCurr)
        self.prev_color = color
        self.calcRGB(color)
        self.cubesWidget.colorsUpdate(color)

    def setRGB(self, event, color):
        self.calcRGB(color)

    def calcRGB(self, color):
        rgb_red = color.red()
        rgb_green = color.green()
        rgb_blue = color.blue()
        rgb_text = "R: {0}   G: {1}   B: {2}".format(rgb_red, rgb_green, rgb_blue)
        self.rgb_lbl.setText(rgb_text)
        hex_text = "#{0:X}{1:X}{2:X}".format(rgb_red, rgb_green, rgb_blue)
        self.hex_lbl.setText(hex_text)


if __name__ == '__main__':
    app = QApplication([])
    window = colorPickerClass()
    window.show()
    app.exec_()
