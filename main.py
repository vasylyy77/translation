import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from translator import Ui_MainWindow
from PySide6.QtTextToSpeech import QTextToSpeech
class NewWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewWindow()
    window.show()
    app.exec()
    #sys.exit(app.exec())



# pip install pyinstaller
# pyinstaller   --onefile --noconsole --icon=logo.ico -n translation main.py
# pyinstaller --hidden-import enchant.backends --hidden-import enchant.tokenize main.py