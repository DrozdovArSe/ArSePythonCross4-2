#!/usr/bin/env python3
# coding=utf-8

import re
import sys
import random
import string

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/LOGO.jpeg'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_desolve.clicked.connect(self.desolve)

    def solve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText()
        tnew = ''
        k = 0
        for i in range(len(text)):
            if text[i] != ' ':
                k += 1
            if k % 2 == 1 or text[i] == ' ':
                tnew += text[i]
        self.textEdit_words.setText(tnew)

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()

    def desolve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText()
        tnew = ''
        for i in range(len(text)):
            tnew += text[i]
            if text[i] != ' ':
                tnew += random.choice(string.ascii_lowercase)
        self.textEdit_words.setText(tnew)

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
