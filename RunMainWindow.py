import sys
import MainWindowHorizontalLayout

form PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__'
    app = QApplication(sys.argr)
    mainWindow = QMainWindow()
    ui = MainWindowHorizontalLayout.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())