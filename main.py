import sys
# pip install pyqt5
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QFileDialog
from gui import Ui_MainWindow
from gui1 import Ui_Form


class MyLabel(QLabel):
    begin = QPoint()
    end = QPoint()
    flag = False

    # Mouse click event
    def mousePressEvent(self, event):
        print(" 1")
        self.flag = True
        self.begin = event.pos()

    # Mouse movement events
    def mouseMoveEvent(self, event):
        print(" 2")
        if self.flag:
            self.end = event.pos()
            self.update()

    # Draw events
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        rect = QRect(self.begin, self.end)
        painter.drawRect(rect)


class sub_screen1(QMessageBox, Ui_Form):
    def __init__(self):
        super(sub_screen1, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        print("sub_screen is close")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.Button_m_start.clicked.connect(self.show_sub_screen)

        self.link_file = None
        self.pixmap = None
        self.lb = None

        # register sub screen
        self.uic1 = sub_screen1()
        # size of QMessageBox
        self.uic1.setStyleSheet("QLabel{min-width: 600px; min-height: 400px}")

        # add button Close to MessageBox
        self.uic1.addButton(QMessageBox.Close)

        # add button Draw to QMessageBox
        self.Draw_button = self.uic1.addButton('Draw', QMessageBox.YesRole)
        self.Draw_button.clicked.disconnect()
        self.Draw_button.clicked.connect(self.draw_rect)

        # add button open to QMessageBox
        self.open_button = self.uic1.addButton('open', QMessageBox.YesRole)
        self.open_button.clicked.disconnect()
        self.open_button.clicked.connect(self.open_image)

    def closeEvent(self, event):
        self.uic1.close()
        print("main close")

    def show_sub_screen(self):
        self.uic1.show()

    def open_image(self):
        self.link_file = QFileDialog.getOpenFileName()
        self.pixmap = QPixmap(self.link_file[0]).scaled(600, 400, Qt.KeepAspectRatio)
        self.uic1.label.setPixmap(self.pixmap)

    def draw_rect(self):
        print("draw")
        # show rectangle
        self.lb = MyLabel(self.uic1)  # call function of paintEvent
        # self.lb.setGeometry(QRect(0, 0, 200, 200))  # limit of rectangle and set up geometry
        self.lb.setCursor(Qt.CrossCursor)  # change type of mouse cursor
        self.lb.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
