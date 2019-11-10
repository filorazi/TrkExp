from PyQt5.QtWidgets import *

class  Gui(QDialog):
    def __init__(self):
        super(Gui, self).__init__()
        self.originalPalette = QApplication.palette()
        self.label = QLabel("Ciao")
        mainLayout = QGridLayout()
        tab = QTabWidget()
        tab.addTab(self.frontPage(),"1")
        tab.addTab(self.secondPage(),"2")
        tab.addTab(self.lastPage(),"3")
        mainLayout.addWidget(tab)
        self.setLayout(mainLayout)
        self.setWindowTitle("Styles")

    def frontPage(self):
        page = QWidget()
        label = QLabel("aaaaa")
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        page.setLayout(vbox)
        return page

    def secondPage(self):
        page = QWidget()
        label = QLabel("ccccc")
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        page.setLayout(vbox)
        return page

    def lastPage(self):
        page = QWidget()
        label = QLabel("bbbbb")
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        page.setLayout(vbox)
        return page

    def exec(self):
        self.app.exec_()
