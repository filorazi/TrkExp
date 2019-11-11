from PyQt5.QtWidgets import *
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class Canvas(FigureCanvas):

    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plot()

    def plot(self):
        x = np.array([50, 30,40])
        labels = ["Apples", "Bananas", "Melons"]
        ax = self.figure.add_subplot(111)
        ax.pie(x, labels=labels)


class  Gui(QDialog):
    def __init__(self):
        super(Gui, self).__init__()
        self.originalPalette = QApplication.palette()
        self.label = QLabel("Ciao")
        mainLayout = QGridLayout()
        tab = QTabWidget()
        # TODO:
        dbcon = dbConnector("database.db")
        self.data = dbcon.getCatData()

        tab.addTab(self.frontPage(),"1")
        tab.addTab(self.secondPage(),"2")
        tab.addTab(self.lastPage(),"3")
        mainLayout.addWidget(tab)
        self.setLayout(mainLayout)
        self.setWindowTitle("Styles")

    def frontPage(self):
        page = QWidget()

        #cate = QLabel("Categories")
        #expe = QLabel("Expences")
        #a = QLabel("Categories")
        #b = QLabel("Expences")
        #c = QLabel("Categories")
        #d = QLabel("Expences")

        #canvas = FigureCanvas(Figure(figsize=(4,2)))

        outernHBox = QVBoxLayout()
        outernHBox.addWidget(dataTable())
        outernHBox.addWidget(graphPlot())

        page.setLayout(outernHBox)
        return page

    def dataTable(self):
        table = QTableWidget()
        # TODO:
        rows = len(self.data)
        cols = 2
        table.setColumnCount(cols)
        table.setRowCount(cols)

        i=0
        for cat, nb in self.data:
            table.setItem(i,0, QTableWidgetItem(cat))
            table.setItem(i,1, QTableWidgetItem(nb))
            i -= -1

        return table

    def graphPlot():
        frame = QWidget()
        flayout = QVBoxLayout()
        canvas = FigureCanvas(Figure(figsize=(4,2)))
        flayout.addWidget(canvas)
        
        return


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
