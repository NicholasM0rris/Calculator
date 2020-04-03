import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np

calculator_labels = [
    'abs(',
    'x^3',
    '<>',
    'x^-1',
    'OFF',
    'sqrt(',
    'x^2',
    'NONE',
    'log',
    'ln',
    'sin(',
    'cos(',
    'tan(',
    '(',
    ')',
    '7',
    '8',
    '9',
    'del',
    'CLR',
    '4',
    '5',
    '6',
    'x',
    '/',
    '1',
    '2',
    '3',
    '+',
    '-',
    '0',
    '.',
    'x10',
    'ANS',
    '=',
]

numerals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for integer in numerals:
    integer = str(integer)

operations = ['+', '-', '/', '*', '(', ')']


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        #self.setStyleSheet('color: red')
        self.previous_answer = '0'
        self.buttons = []
        self.display_text = ""
        self.math_text = ''
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        #self.palette = QPalette()
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)
        #self.palette.setColor(QPalette.Button, Qt.blue)
        #self.palette.setColor(QPalette.ButtonText, Qt.white)
        self.grid = QGridLayout()
        # self.setPalette(self.palette)
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Nick's calculator")
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)

        # Creation functions
        self.create_buttons(calculator_labels)
        self.add_buttons()
        self.create_display()

        self.wid.setLayout(self.grid)
        self.show()

    def create_display(self):
        self.label = QLabel("Nick's calculator")
        f = self.label.font()
        f.setPointSize(16)
        self.label.setFont(f)
        self.label.setAlignment(Qt.AlignRight)
        self.label.setStyleSheet('color: red')
        newfont = QFont("Helvetica [Cronyx]", 16, QFont.Bold)
        self.label.setFont(newfont)

        self.display = QLineEdit()
        f = self.display.font()
        f.setPointSize(27)
        self.display.setFont(f)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding,
        )
        self.display.setMinimumHeight(100)

        self.grid.addWidget(self.display, 1, 0, 3, 0)
        self.grid.addWidget(self.label, 0, 0, 1, 0)

    def create_buttons(self, labels):
        for label in labels:
            if label not in ("NONE", '<>'):
                abutton = QPushButton(label, self)
                abutton.setSizePolicy(
                    QSizePolicy.Preferred,
                    QSizePolicy.Expanding,
                )
                newfont = QFont("SansSerif", 16, QFont.Bold)
                abutton.setFont(newfont)
                abutton.clicked.connect(self.onclick)
                if label == "CLR" or label == 'OFF':
                    abutton.setStyleSheet("background-color:#FF0000;\
        border: 2px solid #555555")
                elif label == 'del':
                    abutton.setStyleSheet("background-color:#FF6347;\
                    border: 2px solid #555555")


                self.buttons.append(abutton)
            else:
                self.buttons.append(label)


    def add_buttons(self):
        row, column = (4, 0)
        for button in self.buttons:
            if button not in ("NONE", "<>"):
                self.grid.addWidget(button, row, column)
            column += 1
            if column > 4:
                column = 0
                row += 1

    def onclick(self):
        print(self.sender().text())
        text = self.sender().text()
        if text == '=':
            try:
                print(self.math_text)
                answer = str(eval(self.math_text))
                self.previous_answer = answer
                print("ANSWER: ", answer)
                self.display_text = answer
                self.math_text = answer
                self.display.setText(self.display_text)
            except (SyntaxError, NameError):
                msg = QMessageBox()
                msg.setWindowTitle("Whoops ! ")
                msg.setText("That expression didn't make sense. \n PS: Don't forget to close off those brackets ! ")
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()
        elif text == 'del':
            self.display_text = self.display_text[:-1]
            self.math_text = self.math_text[:-1]
            self.display.setText(self.display_text)
        elif text == 'ANS':
            self.math_text = self.previous_answer
            self.display_text = self.previous_answer
            self.display.setText(self.display_text)
        elif text == 'cos(':
            self.math_text += 'np.cos('
            self.display_text += 'c/o/s/('
            self.display.setText(self.display_text)
        elif text == 'sin(':
            self.math_text += 'np.sin('
            self.display_text += 's/i/n/('
            self.display.setText(self.display_text)
        elif text == 'tan(':
            self.math_text += 'np.tan('
            self.display_text += 't/a/n/('
            self.display.setText(self.display_text)
        elif text == 'CLR':
            self.math_text = ''
            self.display_text = ''
            self.display.setText(self.display_text)
        elif text == 'sqrt(':
            self.math_text += '**(1/2)'
            self.display_text += '^^(1/2)'
            self.display.setText(self.display_text)
        elif text == 'ln':
            self.math_text += 'np.log('
            self.display_text += 'l/o/g/('
            self.display.setText(self.display_text)
        elif text == 'log':
            self.math_text += 'np.log10('
            self.display_text += 'l/o/g/10('
            self.display.setText(self.display_text)
        elif text == 'OFF':
            self.display_text = "OFF"
            self.display.setText(self.display_text)
            sys.exit(0)
        elif text == 'x':
            self.math_text += '*'
            self.display_text += text
            self.display.setText(self.display_text)
        elif text == 'x^3':
            self.math_text += '**3'
            self.display_text += '^^3'
            self.display.setText(self.display_text)
        elif text == 'x^2':
            self.math_text += '**2'
            self.display_text += '^^2'
            self.display.setText(self.display_text)
        elif text == 'x^-1':
            self.math_text += '**(-1)'
            self.display_text += '^^(-1)'
            self.display.setText(self.display_text)
        elif text == 'x10':
            self.math_text += '*10'
            self.display_text += 'x10'
            self.display.setText(self.display_text)

        else:
            self.math_text += text
            self.display_text += text
            self.display.setText(self.display_text)




def main(arglist):
    app = QApplication([])
    calculator = Calculator()
    app.exec_()


if __name__ == '__main__':
    main(sys.argv[1:])
