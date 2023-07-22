# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'un.ui'
##
# Created by: Qt User Interface Compiler version 6.5.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from enchant.checker import SpellChecker
import enchant
from googletrans import Translator
from PySide6.QtTextToSpeech import QTextToSpeech
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QTextCharFormat, QTextCursor, QImage, QKeySequence, QLinearGradient, QPainter,
     QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
     QMainWindow, QMenuBar, QPushButton, QRadioButton,QMessageBox,
     QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
     QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 625)
        self.setWindowIcon(QIcon("logo.png"))
        self.is_speaking = False
        self.is_speaking_2 = False

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.maimFrame = QFrame(self.centralwidget)
        self.maimFrame.setObjectName(u"maimFrame")
        self.maimFrame.setGeometry(QRect(20, 30, 771, 501))
        self.verticalLayout = QVBoxLayout(self.maimFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.maimFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton = QRadioButton(self.maimFrame)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.maimFrame)
        self.radioButton_2.setObjectName(u"radioButton_2")



        self.horizontalLayout.addWidget(self.radioButton_2)



        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(self.maimFrame)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.pushButton.clicked.connect(self.click_tr)
# btn 4
        self.pushButton_4 = QPushButton(self.maimFrame)
        self.pushButton_4.setObjectName("Check")
        self.pushButton_4.clicked.connect(self.check_text)

        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.pushButton.clicked.connect(self.click_tr)

        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.pushButton_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit = QTextEdit(self.maimFrame)
        self.textEdit.setObjectName(u"textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.textEdit_2 = QTextEdit(self.maimFrame)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.maimFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)

        # Set the initial icon for the QPushButton
        self.update_button_icon()

        # Connect the button to the speak_text function
        self.pushButton_2.clicked.connect(self.speak_text)
        # Set the size of the icon
        icon_size = QSize(32, 32)  # Adjust the size as needed
        self.pushButton_2.setIconSize(icon_size)
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QPushButton(self.maimFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        self.update_button_icon_2()
        icon_size = QSize(32, 32)  # Adjust the size as needed
        self.pushButton_3.setIconSize(icon_size)
        self.pushButton_3.clicked.connect(self.speak_text_2)
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 807, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.text_to_speech = QTextToSpeech()
        locale = QLocale("en_US")
        self.text_to_speech.setLocale(locale)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Translator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0437\u0432\u0443\u0447\u0438\u0442\u044c \u0442\u0435\u043a\u0441\u0442", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0437\u0432\u0443\u0447\u0438\u0442\u044c \u043f\u0435\u0440\u0435\u0432\u043e\u0434", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", 'Check text',None))

    def check_text(self):
        d = enchant.Dict("en_US")
        text = self.textEdit.toPlainText()
        chkr = SpellChecker("en")
        chkr.set_text(text)
        for err in chkr:
            print(err.word)
            mess = QMessageBox()
            mess.information(self.maimFrame, "Spell Check", f"""{err.word} : 
              {d.suggest(err.word)}""")
            mess.setFixedWidth(400)
            mess.setStyleSheet("background-color: rgb(0, 0, 0);")


    def click_tr(self):
        if(self.radioButton.isChecked()):
            input_text = self.textEdit.toPlainText()
            translator = Translator()
            translated_text = translator.translate(input_text, dest='en').text
            self.textEdit_2.setText(translated_text)
        if(self.radioButton_2.isChecked()):
            input_text = self.textEdit.toPlainText()
            translator = Translator()
            translated_text = translator.translate(input_text, dest='ru').text
            self.textEdit_2.setText(translated_text)



    def speak_text(self):

        if self.is_speaking:
            # Stop the text-to-speech and reset the icon
            self.text_to_speech.stop()
            self.is_speaking = False
            self.update_button_icon()
        else:
            # Start speaking the text and set the icon accordingly
            text = self.textEdit.toPlainText()
            self.text_to_speech.say(text)
            self.is_speaking = True
            self.update_button_icon()

    def update_button_icon(self):
        # Toggle the button's icon based on the current state
        if self.is_speaking:
            self.pushButton_2.setIcon(QIcon('stop-sound.svg'))
        else:
            self.pushButton_2.setIcon(QIcon('volume.svg'))

    def speak_text_2(self):
        if self.is_speaking_2:
            # Stop the text-to-speech and reset the icon
            self.text_to_speech.stop()
            self.is_speaking_2 = False
            self.update_button_icon_2()
        else:
            # Start speaking the text and set the icon accordingly
            text = self.textEdit_2.toPlainText()
            self.text_to_speech.say(text)
            self.is_speaking_2 = True
            self.update_button_icon_2()

    def update_button_icon_2(self):
        # Toggle the button's icon based on the current state
        if self.is_speaking_2:
            self.pushButton_3.setIcon(QIcon('stop-sound.svg'))
        else:
            self.pushButton_3.setIcon(QIcon('volume.svg'))

