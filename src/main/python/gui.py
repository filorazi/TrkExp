from PyQt5.QtWidgets import *

class  Gui(QDialog):
    def __init__(self):
        super(Gui, self).__init__()
        self.originalPalette = QApplication.palette()
        self.label = QLabel("Ciao")
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.label)
        self.setLayout(mainLayout)
        self.setWindowTitle("Styles")


    def exec(self):
        self.app.exec_()
