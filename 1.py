from os import system
import sys
system("cls")
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class Win(QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.setWindowTitle("Calculator")
        #adressni to'g'irlab olish kerak
        self.setWindowIcon(QIcon(QPixmap("calculator\\calc.png")))
        self.resize(600,600)
        self.move(400,200)
        self.setFont(QFont("Times New Roman", 24))
        self.isonoff=False
        self.sign=""
        self.op1=""
        self.checker=True

        self.edit=QLineEdit(self)
        self.edit.move(0,0)
        self.edit.resize(600, 100)
        self.edit.setAlignment(Qt.AlignRight)
        self.edit.setStyleSheet("background-color:lightgrey;")
        self.edit.setText("")
        
        #on
        self.on=QPushButton(self)
        self.on.setGeometry(0, 100, 225, 100)
        self.on.clicked.connect(self.on_off)
        
        self.on.setText("OFF")
        self.on.setStyleSheet("""
            background-color:red;
            border:1px solid black;
        """)
        #C
        self.toza=QPushButton(self)
        self.toza.setGeometry(225, 100, 225, 100)
        self.toza.setText("C")
        self.toza.setStyleSheet("""background-color:DeepSkyBlue; border:1px solid black""")
        self.toza.clicked.connect(self.clear)
        #7
        self.seven=QPushButton(self)
        self.seven.setGeometry(0, 200, 150, 100)
        self.seven.setText("7")
        self.numbers(self.seven)
        self.seven.clicked.connect(self.action7)

        #8
        self.eight=QPushButton(self)
        self.eight.setGeometry(150, 200, 150, 100)
        self.eight.setText("8")
        self.numbers(self.eight)
        self.eight.clicked.connect(self.action8)

        #9
        self.nine=QPushButton(self)
        self.nine.setGeometry(300, 200, 150, 100)
        self.nine.setText("9")
        self.numbers(self.nine)
        self.nine.clicked.connect(self.action9)

        #4
        self.four=QPushButton(self)
        self.four.setGeometry(0, 300, 150, 100)
        self.four.setText("4")
        self.numbers(self.four)
        self.four.clicked.connect(self.action4)

        #5
        self.five=QPushButton(self)
        self.five.setGeometry(150, 300, 150, 100)
        self.five.setText("5")
        self.numbers(self.five)
        self.five.clicked.connect(self.action5)


        #6
        self.six=QPushButton(self)
        self.six.setGeometry(300, 300, 150, 100)
        self.six.setText("6")
        self.numbers(self.six)
        self.six.clicked.connect(self.action6)


        #1
        self.one=QPushButton(self)
        self.one.setGeometry(0, 400, 150, 100)
        self.one.setText("1")
        self.numbers(self.one)
        self.one.clicked.connect(self.action1)

        #2
        self.two=QPushButton(self)
        self.two.setGeometry(150, 400, 150, 100)
        self.two.setText("2")
        self.numbers(self.two)
        self.two.clicked.connect(self.action2)


        #3
        self.three=QPushButton(self)
        self.three.setGeometry(300, 400, 150, 100)
        self.three.setText("3")
        self.numbers(self.three)
        self.three.clicked.connect(self.action3)


        #0
        self.zero=QPushButton(self)
        self.zero.setGeometry(0, 500, 225, 100)
        self.zero.setText("0")
        self.numbers(self.zero)
        self.zero.clicked.connect(self.action0)


        #=
        self.equal=QPushButton(self)
        self.equal.setGeometry(225, 500, 225, 100)
        self.equal.setText("=")
        self.equal.setStyleSheet("""
            background-color:Red;
        """)
        self.equal.clicked.connect(self.answer)
        #+
        self.plus=QPushButton(self)
        self.plus.setGeometry(450, 100, 150, 125)
        self.plus.setText("+")
        self.amal(self.plus)
        self.plus.clicked.connect(self.add)

        #-
        self.minus=QPushButton(self)
        self.minus.setGeometry(450, 225, 150, 125)
        self.minus.setText("-")
        self.amal(self.minus)
        self.minus.clicked.connect(self.subtract)

        #*
        self.kop=QPushButton(self)
        self.kop.setGeometry(450, 350, 150, 125)
        self.kop.setText("*")
        self.amal(self.kop)
        self.kop.clicked.connect(self.multiply)

        #/
        self.bol=QPushButton(self)
        self.bol.setGeometry(450, 475, 150, 125)
        self.bol.setText("/")
        self.amal(self.bol)
        self.bol.clicked.connect(self.divide)


    def numbers(self, number):
        number.setStyleSheet("""
            background-color:orange;
            border:1px solid black;
        """)   
    def amal(self, bajar):
        bajar.setStyleSheet("""
            background-color: BlueViolet;
            border:1px solid black;
        """)
    def on_off(self):
        self.on.setFont(QFont("Times New Roman", 24))
        if self.on.text()=="OFF":
            self.on.setText("ON")
            self.on.setStyleSheet("""
                background-color:lawngreen;
                border:1px solid black;
            """)
            self.isonoff=True
            self.checker=False
            self.edit.setText("0")
        else:
            self.on.setText("OFF")
            self.on.setStyleSheet("""
                background-color:red;
                border:1px solid black;
            """)
            self.isonoff=False
            self.checker=True
            self.edit.setText("")
    def clear(self):
        self.edit.setText("0")
    def add(self):
        self.sign="+"
        self.op1=self.edit.text()
        self.edit.setText("")
    def subtract(self):
        self.sign="-"
        self.op1=self.edit.text()
        self.edit.setText("")
    def multiply(self):
        self.sign="*"
        self.op1=self.edit.text()
        self.edit.setText("")
    def divide(self):
        self.sign=":"
        self.op1=self.edit.text()
        self.edit.setText("")


    def answer(self):
        self.checker=False
        match self.sign:
            case "+":
                op2=self.edit.text()
                self.edit.setText(f"{int(self.op1)+int(op2)}")
            case "-":
                op2=self.edit.text()
                self.edit.setText(f"{int(self.op1)-int(op2)}")
            case "*":
                op2=self.edit.text()
                self.edit.setText(f"{int(self.op1)*int(op2)}")
            case ":":
                op2=self.edit.text()
                self.edit.setText(f"{int(self.op1)/int(op2)}")
            
    def action1(self):
        if self.edit.text()=='0' or self.checker==False:
            self.checker=True
            self.edit.setText('1')
        elif self.isonoff:
            self.edit.setText(self.edit.text()+"1")

    def action2(self):
        if self.edit.text()=='0' or self.checker==False:
            self.edit.setText('2')
            self.checker=True
        elif self.isonoff:
            self.edit.setText(self.edit.text()+"2")

    def action3(self):
        if self.edit.text()=='0' or self.checker==False:
            self.checker=True
            self.edit.setText('3')
        elif self.isonoff:
            self.edit.setText(self.edit.text()+"3")

    def action4(self):
        if self.edit.text()=='0' or self.checker==False:
            self.checker=True
            self.edit.setText('4')
        elif self.isonoff:
            self.edit.setText(self.edit.text()+"4")

    def action5(self):
        if self.edit.text()=='0' or self.checker==False:
            self.checker=True
            self.edit.setText('5')
        elif self.isonoff:
            self.edit.setText(self.edit.text()+"5")

    def action6(self):
        if self.edit.text()=='0' or self.checker==False:
            self.checker=True
            self.edit.setText('6')
        elif self.isonoff:
            self.edit.setText(self.edit.text()+"6")

    def action7(self):
        if self.edit.text()=='0' or self.checker==False:
            self.checker=True
            self.edit.setText('7')
        elif self.isonoff:
            self.edit.setText(self.edit.text()+"7")

    def action8(self):
        if self.edit.text()=='0' or self.checker==False:
            self.edit.setText('8')
            self.checker=True
        elif self.isonoff:
            self.edit.setText(self.edit.text()+"8")

    def action9(self):
        if self.edit.text()=='0' or self.checker==False:
            self.checker=True
            self.edit.setText('9')
        elif self.isonoff:
            self.edit.setText(self.edit.text()+"9")

    def action0(self):
        if self.edit.text()=='0' or self.checker==False:
            self.checker=True
            self.edit.setText('0')
        elif self.isonoff:
            self.edit.setText(self.edit.text()+"0")


app=QApplication(sys.argv)
calc=Win()
calc.show()
sys.exit(app.exec_())
