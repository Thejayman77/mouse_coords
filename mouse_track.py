import pyautogui
from PyQt5.QtWidgets import QApplication, QWidget
from coords_gui import Ui_Form
from PyQt5.Qt import QThread

class MousePos(QThread):
    def __init__(self, gui):
        super().__init__()

        self.gui = gui

    def run(self):
        while True:
            x, y = pyautogui.position()
            self.gui.ui.x_coord.setText(str(x))
            self.gui.ui.y_coord.setText(str(y))


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    gui = AppWindow()
    gui.show()
    thread = MousePos(gui)
    thread.start()
    app.exec_()