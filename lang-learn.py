# -*- coding: utf-8 -*-
#!./venv/bin/python

from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os
import sys


def temp_dir(path):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(".")
    
    return os.path.join(base, path)


def check_main_data_file():
    base = os.path.abspath(".")
    if not os.path.isfile(os.path.join(base, "maindata.json")):
        with open(os.path.join(base, "maindata.json"), "w", encoding="utf-8") as file:
            json.dump({}, file, ensure_ascii=False)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_add_word = QtWidgets.QWidget()
        self.tab_add_word.setObjectName("tab_add_word")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_add_word)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_tab_add_word = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_tab_add_word.setContentsMargins(0, 0, 0, 0)
        self.grid_tab_add_word.setObjectName("grid_tab_add_word")
        self.labe_translate_of_word = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labe_translate_of_word.setObjectName("labe_translate_of_word")
        self.grid_tab_add_word.addWidget(self.labe_translate_of_word, 1, 0, 1, 1)
        self.label_delete_word = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_delete_word.setObjectName("label_delete_word")
        self.grid_tab_add_word.addWidget(self.label_delete_word, 5, 0, 1, 1)
        self.word_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.word_input.setObjectName("word_input")
        self.grid_tab_add_word.addWidget(self.word_input, 0, 2, 1, 1)
        self.label_word = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_word.setObjectName("label_word")
        self.grid_tab_add_word.addWidget(self.label_word, 0, 0, 1, 1)
        self.delete_word_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.delete_word_input.setObjectName("delete_word_input")
        self.grid_tab_add_word.addWidget(self.delete_word_input, 5, 1, 1, 1)
        self.translate_of_word_input = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.translate_of_word_input.setObjectName("translate_of_word_input")
        self.grid_tab_add_word.addWidget(self.translate_of_word_input, 1, 2, 1, 1)
        self.add_word_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_word_button.setObjectName("add_word_button")
        self.grid_tab_add_word.addWidget(self.add_word_button, 2, 0, 1, 3)
        self.delete_word_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.delete_word_button.setObjectName("delete_word_button")
        self.save_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.grid_tab_add_word.addWidget(self.save_button, 3, 0, 1, 3)
        self.grid_tab_add_word.addWidget(self.delete_word_button, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_tab_add_word.addItem(spacerItem, 3, 0, 1, 3)
        self.tabWidget.addTab(self.tab_add_word, "")
        self.tab_learn = QtWidgets.QWidget()
        self.tab_learn.setObjectName("tab_learn")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_learn)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 791, 431))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 789, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.show_button = QtWidgets.QPushButton(self.tab_learn)
        self.show_button.setGeometry(QtCore.QRect(0, 430, 89, 31))
        self.show_button.setObjectName("show_button")
        self.tabWidget.addTab(self.tab_learn, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.add_word_button.clicked.connect(self.add_word)
        self.delete_word_button.clicked.connect(self.delete_word)
        self.save_button.clicked.connect(self.updatemaindatafile)
        self.show_button.clicked.connect(self.show_learn)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.updatemaindata()
        self.show_learn()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Turkish Learn"))
        self.labe_translate_of_word.setText(_translate("MainWindow", "Translate of word:"))
        self.label_delete_word.setText(_translate("MainWindow", "Delete Word"))
        self.word_input.setPlaceholderText(_translate("MainWindow", "Enter a word"))
        self.label_word.setText(_translate("MainWindow", "Word:"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.delete_word_input.setPlaceholderText(_translate("MainWindow", "Enter a Word"))
        self.translate_of_word_input.setPlaceholderText(_translate("MainWindow", "Enter translate if word (You can add multi translate; split by \"-\")"))
        self.add_word_button.setText(_translate("MainWindow", "Add"))
        self.delete_word_button.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_add_word), _translate("MainWindow", "Add Word"))
        self.show_button.setText(_translate("MainWindow", "Show"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_learn), _translate("MainWindow", "Learn"))

    def clear_how_learn(self):
        for i in reversed(range(self.gridLayout.count())):
            try:
                self.gridLayout.itemAt(i).widget().deleteLater()
            except Exception:
                pass


    def show_learn(self):
        self.clear_how_learn()
        counter = 1
        for i in self.maindata:
            w = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            t = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            w.setText(i)
            t.setText(" , ".join(self.maindata[i]))
            self.gridLayout.addWidget(w, counter, 3, 1, 1)
            self.gridLayout.addWidget(t, counter, 4, 1, 1)
            counter += 1
    
    def updatemaindata(self):
        with open("maindata.json", "r", encoding="utf-8") as file:
            self.maindata = json.load(file)
    
    def updatemaindatafile(self):
        with open("maindata.json", "w", encoding="utf-8") as file:
            json.dump(self.maindata, file, ensure_ascii=False)
    
    def add_word(self):
        word = self.word_input.text().title()
        translate = self.translate_of_word_input.toPlainText().split("-")
        translate = [i.title() for i in translate]
        try:
            self.maindata[word].append(translate)
        except KeyError:
            self.maindata[word] = translate
    
    def delete_word(self):
        word = self.delete_word_input.text().title()
        self.maindata.pop(word)


if __name__ == "__main__":
    check_main_data_file()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
