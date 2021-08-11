from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Calculadora")
        MainWindow.resize(421, 480)
        MainWindow.setStyleSheet("background-color: #000000")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton {color: #3e0078; \
                                          background-color: #141414; \
                                          font: 75 14pt \\\MS Shell Dlg 2\\\; \
                                          border-width: 1px;}")

        self.num7 = QtWidgets.QPushButton(self.centralwidget)
        self.num7.setGeometry(QtCore.QRect(10, 200, 71, 61))
        self.num7.setStyleSheet("QPushButton {background-color: #141414; \
                                              border-radius: 5px;}"
                                "QPushButton:pressed {background-color: #1c1c1c }")
        self.num7.setText("7")

        self.num8 = QtWidgets.QPushButton(self.centralwidget)
        self.num8.setGeometry(QtCore.QRect(83, 200, 71, 61))
        self.num8.setStyleSheet("QPushButton {background-color: #141414; \
                                              border-radius: 5px;}"
                                "QPushButton:pressed {background-color: #1c1c1c }")
        self.num8.setText("8")

        self.num9 = QtWidgets.QPushButton(self.centralwidget)
        self.num9.setGeometry(QtCore.QRect(156, 200, 71, 61))
        self.num9.setStyleSheet("QPushButton {background-color: #141414; \
                                              border-radius: 5px;}"
                                "QPushButton:pressed {background-color: #1c1c1c }")
        self.num9.setText("9")

        self.num4 = QtWidgets.QPushButton(self.centralwidget)
        self.num4.setGeometry(QtCore.QRect(10, 270, 71, 61))
        self.num4.setStyleSheet("QPushButton {background-color: #141414; \
                                              border-radius: 5px;}"
                                "QPushButton:pressed {background-color: #1c1c1c }")
        self.num4.setText("4")

        self.num5 = QtWidgets.QPushButton(self.centralwidget)
        self.num5.setGeometry(QtCore.QRect(83, 270, 71, 61))
        self.num5.setStyleSheet("QPushButton {background-color: #141414; \
                                              border-radius: 5px;}"
                                "QPushButton:pressed {background-color: #1c1c1c }")
        self.num5.setText("5")

        self.num6 = QtWidgets.QPushButton(self.centralwidget)
        self.num6.setGeometry(QtCore.QRect(156, 270, 71, 61))
        self.num6.setStyleSheet("QPushButton {background-color: #141414; \
                                              border-radius: 5px;}"
                                "QPushButton:pressed {background-color: #1c1c1c }")
        self.num6.setText("6")
    
        self.num3 = QtWidgets.QPushButton(self.centralwidget)
        self.num3.setGeometry(QtCore.QRect(156, 340, 71, 61))
        self.num3.setStyleSheet("QPushButton {background-color: #141414; \
                                              border-radius: 5px;}"
                                "QPushButton:pressed {background-color: #1c1c1c }")
        self.num3.setText("3")

        self.num2 = QtWidgets.QPushButton(self.centralwidget)
        self.num2.setGeometry(QtCore.QRect(83, 340, 71, 61))
        self.num2.setStyleSheet("QPushButton {background-color: #141414; \
                                              border-radius: 5px;}"
                                "QPushButton:pressed {background-color: #1c1c1c }")
        self.num2.setText("2")

        self.num1 = QtWidgets.QPushButton(self.centralwidget)
        self.num1.setGeometry(QtCore.QRect(10, 340, 71, 61))
        self.num1.setStyleSheet("QPushButton {background-color: #141414; \
                                              border-radius: 5px;}"
                                "QPushButton:pressed {background-color: #1c1c1c }")
        self.num1.setText("1")

        self.num0 = QtWidgets.QPushButton(self.centralwidget)
        self.num0.setGeometry(QtCore.QRect(83, 410, 71, 61))
        self.num0.setStyleSheet("QPushButton {background-color: #141414; \
                                              border-radius: 5px;}"
                                "QPushButton:pressed {background-color: #1c1c1c }")
        self.num0.setText("0")

        self.bttn_comma = QtWidgets.QPushButton(self.centralwidget)
        self.bttn_comma.setGeometry(QtCore.QRect(10, 130, 71, 61))
        self.bttn_comma.setStyleSheet("QPushButton {background-color: #141414; \
                                      color: #ff9e9e; \
                                      border-radius: 5px;}"
                                      "QPushButton:pressed {background-color: #1c1c1c }" )
        self.bttn_comma.setText(".")

        self.bttn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.bttn_equal.setGeometry(QtCore.QRect(302, 270, 111, 201))
        self.bttn_equal.setStyleSheet("QPushButton {background-color: #141414; \
                                      color: #ff9e9e; \
                                      border-radius: 5px;}"
                                      "QPushButton:pressed {background-color: #1c1c1c }" )
        self.bttn_equal.setText("=")

        self.bttn_sub = QtWidgets.QPushButton(self.centralwidget)
        self.bttn_sub.setGeometry(QtCore.QRect(229, 340, 71, 61))
        self.bttn_sub.setStyleSheet("QPushButton {background-color: #141414; \
                                     color: #730000; \
                                     border-radius: 5px;}"
                                     "QPushButton:pressed {background-color: #1c1c1c }")
        self.bttn_sub.setText(" - ")

        self.bttn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.bttn_plus.setGeometry(QtCore.QRect(229, 410, 71, 61))
        self.bttn_plus.setStyleSheet("QPushButton {background-color: #141414; \
                                     color: #730000; \
                                     border-radius: 5px;}"
                                     "QPushButton:pressed {background-color: #1c1c1c }")
        self.bttn_plus.setText(" + ")

        self.bttn_mult = QtWidgets.QPushButton(self.centralwidget)
        self.bttn_mult.setGeometry(QtCore.QRect(229, 270, 71, 61))
        self.bttn_mult.setBaseSize(QtCore.QSize(0, 0))
        self.bttn_mult.setStyleSheet("QPushButton {background-color: #141414; \
                                     color: #730000; \
                                     border-radius: 5px;}"
                                     "QPushButton:pressed {background-color: #1c1c1c }")
        self.bttn_mult.setText(" * ")

        self.bttn_div = QtWidgets.QPushButton(self.centralwidget)
        self.bttn_div.setGeometry(QtCore.QRect(229, 200, 71, 61))
        self.bttn_div.setStyleSheet("QPushButton {background-color: #141414; \
                                     color: #730000; \
                                     border-radius: 5px;}"
                                     "QPushButton:pressed {background-color: #1c1c1c }")
        self.bttn_div.setText(" / ")

        self.bttn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.bttn_clear.setGeometry(QtCore.QRect(302, 200, 111, 61))
        self.bttn_clear.setStyleSheet("QPushButton {background-color: #141414; \
                                      color: #ff9e9e; \
                                      border-radius: 5px;}"
                                      "QPushButton:pressed {background-color: #1c1c1c }" )
        self.bttn_clear.setText("C")

        self.bttn_erase = QtWidgets.QPushButton(self.centralwidget)
        self.bttn_erase.setGeometry(QtCore.QRect(229, 130, 184, 61))
        self.bttn_erase.setStyleSheet("QPushButton {background-color: #141414; \
                                      color: #ff9e9e; \
                                      border-radius: 5px;}"
                                      "QPushButton:pressed {background-color: #1c1c1c }" )
        self.bttn_erase.setText("<--")
        
        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(6, 40, 410, 71))
        self.label_main.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_main.setStyleSheet("background-color:#171717;\n"
                                      "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                      "color: #ffffff")

        self.label_sec = QtWidgets.QLabel(self.centralwidget)
        self.label_sec.setGeometry(QtCore.QRect(6, 10, 410, 31))
        self.label_sec.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_sec.setStyleSheet("background-color:#171717;\n"
                                     "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                     "color: #ffffff")
        
        self.bttn_power = QtWidgets.QPushButton(self.centralwidget)
        self.bttn_power.setGeometry(QtCore.QRect(83, 130, 71, 61))
        self.bttn_power.setStyleSheet("QPushButton {background-color: #141414; \
                                      color: #ff9e9e; \
                                      border-radius: 5px;}"
                                      "QPushButton:pressed {background-color: #1c1c1c }" )
        self.bttn_power.setText("x²")

        self.bttn_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.bttn_sqrt.setGeometry(QtCore.QRect(156, 130, 71, 61))
        self.bttn_sqrt.setStyleSheet("QPushButton {background-color: #141414; \
                                      color: #ff9e9e; \
                                      border-radius: 5px;}"
                                      "QPushButton:pressed {background-color: #1c1c1c }")
        self.bttn_sqrt.setText("√")

        self.bttn_bracket_right = QtWidgets.QPushButton(self.centralwidget)
        self.bttn_bracket_right.setGeometry(QtCore.QRect(156, 410, 71, 61))
        self.bttn_bracket_right.setStyleSheet("QPushButton {background-color: #141414; \
                                               color: #730000; \
                                               border-radius: 5px;}"
                                              "QPushButton:pressed {background-color: #1c1c1c }")
        self.bttn_bracket_right.setText(")")

        self.bttn_bracket_left = QtWidgets.QPushButton(self.centralwidget)
        self.bttn_bracket_left.setGeometry(QtCore.QRect(10, 410, 71, 61))
        self.bttn_bracket_left.setStyleSheet("QPushButton {background-color: #141414; \
                                              color: #730000; \
                                              border-radius: 5px;}"
                                             "QPushButton:pressed {background-color: #1c1c1c }")
        self.bttn_bracket_left.setText("(")
        MainWindow.setCentralWidget(self.centralwidget)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())