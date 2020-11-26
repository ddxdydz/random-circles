import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

ACTIVE_AREA = [500, 500]


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.widgetName = 'Git и желтые окружности'
        self.setWindowTitle(self.widgetName)  # заголовок виджета

        self.do_paint = False
        self.pushButton.clicked.connect(self.press_button)

    def press_button(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor('yellow'))
        qp.setPen(QColor('orange'))

        x, y = randint(20, ACTIVE_AREA[0] - 20), randint(20, ACTIVE_AREA[1] - 20)
        max_size = min([x, y, ACTIVE_AREA[0] - x, ACTIVE_AREA[1] - y])
        radius = randint(20, max_size if max_size <= ACTIVE_AREA[0] // 8 else ACTIVE_AREA[1] // 8)

        qp.drawEllipse(x - radius, y - radius, radius * 2, radius * 2)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
