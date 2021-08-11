import sys
from PyQt5.QtWidgets import QApplication
from calc_func import CWindow

app = QApplication(sys.argv)
calculator = CWindow()
sys.exit(app.exec_())