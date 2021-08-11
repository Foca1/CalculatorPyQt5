from PyQt5 import QtWidgets
from calc_ui import Ui_MainWindow

class CWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.num0.clicked.connect(self.basic)
        self.num1.clicked.connect(self.basic)
        self.num2.clicked.connect(self.basic)
        self.num3.clicked.connect(self.basic)
        self.num4.clicked.connect(self.basic)
        self.num5.clicked.connect(self.basic)
        self.num6.clicked.connect(self.basic)
        self.num7.clicked.connect(self.basic)
        self.num8.clicked.connect(self.basic)
        self.num9.clicked.connect(self.basic)

        self.bttn_plus.clicked.connect(self.basic)
        self.bttn_sub.clicked.connect(self.basic)
        self.bttn_mult.clicked.connect(self.basic)
        self.bttn_div.clicked.connect(self.basic)

        self.bttn_comma.clicked.connect(self.basic)
        self.bttn_power.clicked.connect(self.click_power)
        self.bttn_sqrt.clicked.connect(self.click_sqrt)

        self.bttn_bracket_left.clicked.connect(self.basic)
        self.bttn_bracket_right.clicked.connect(self.basic) 

        self.bttn_clear.clicked.connect(self.click_clear)
        self.bttn_equal.clicked.connect(self.click_equal)
        self.bttn_erase.clicked.connect(self.click_erase)

        self.main_value = ""
        self.value_sec = ""
        self.result = ""

    def basic(self):
        button = self.sender()

        self.main_value += button.text()
        self.label_main.setText(self.main_value)
        
    def click_clear(self):
        self.main_value = ""
        self.label_sec.setText("")
        self.label_main.setText(self.main_value)
        return self.main_value

    def click_power(self):
        try:
            n = pow(int(self.main_value), 2)
            self.label_sec.setText(f"{self.main_value}² = ")
            self.label_main.setText(str(n))

            self.main_value = str(n)
            return self.main_value    
        except ValueError:
            self.label_main.setText(self.main_value)

    def click_sqrt(self):
        try:
            n = float(self.main_value) ** 0.5
            self.label_sec.setText(f"√{self.main_value} = ")
            self.label_main.setText(str(n))

            self.main_value = str(n)
            return self.main_value    
        except ValueError:
            self.label_main.setText(self.main_value)
            
    def click_equal(self):
        try:
            self.value_sec = self.main_value
            self.label_sec.setText(f"   {self.value_sec} = ")

            self.label_main.setText("")
            self.result = eval(self.main_value)
            self.label_main.setText(f"{self.result!s}")

            self.main_value = str(self.result)
            return self.main_value
        except ZeroDivisionError:
            self.label_main.setText("Não é possivel dividir por 0")
        except SyntaxError:
            self.label_main.setText("Conta invalida")
        
    def click_erase(self):
        self.main_value = self.main_value[:-1]
        self.label_main.setText(self.main_value)
        return self.main_value