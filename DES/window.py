import sys
import untitled
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = untitled.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.key_lineEdit_2.setText('Hello World')

    MainWindow.show()
    sys.exit(app.exec_())