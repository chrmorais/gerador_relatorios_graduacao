from PyQt4 import QtGui
import sys
from views import base

class RelataLabApp(QtGui.QMainWindow, base.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RelataLabApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    form = RelataLabApp()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
