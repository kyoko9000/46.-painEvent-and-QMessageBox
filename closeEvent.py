import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from gui import Ui_MainWindow
from gui1 import Ui_Form


class sub_screen(QWidget, Ui_Form):
    def __init__(self):
        super(sub_screen, self).__init__()
        self.go = None
        self.setupUi(self)

    def closeEvent(self, event):
        print("sub close")
        self.go = MainWindow()
        self.go.show_Messages()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.Button_m_start.clicked.connect(self.open_screen)

        self.uic1 = None

    def closeEvent(self, event):
        print("main close")
        if self.uic1:
            self.uic1.close()

    def open_screen(self):
        self.uic1 = sub_screen()
        self.uic1.show()

    def show_Messages(self):
        print("do something here")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
