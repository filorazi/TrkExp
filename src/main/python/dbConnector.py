import sqlite3
from expenseHandler import *
import datetime, time

class DBConnector():
    def __init__(self, dbname):
        self.dbname = dbname
        self.password = password
        self.connection = sqlite3.connect(self.dbname)
        self.dbhandler = connection.cursor()
        sqlite3.register_adapter(datetime.datetime, self.adapt_datetime)

    def adapt_datetime(ts):
        return time.mktime(ts.timetuple())

    def addExpences(self, id, note, exp, expid, ex_date, pay_meth=None):
        self.cursor.execute("INSERT INTO Expences VALUES (?,?,?,?,?,?)", (id,note,exp,exp_id,ex_date, pay_meth))
        return

    def deleteExpences(self, id):
        self.cursor.execute("DELETE FROM Expences WHERE id = ?", id)
        return

    def addCategoryExp(self, id, name):
        self.cursor.execute("INSERT INTO Expences VALUES (?,?)", (id,name))
        return

    def deleteCategoryExp(self, id):
        self.cursor.execute("DELETE FROM categoryEx WHERE id = ?", id)
        return

    def getCategoryExp(self):
        self.cursor.execute("SELECT FROM categoryEx *")
        return self.cursor.fetchall()

    def getExpences(self):
        self.cursor.execute("SELECT FROM Expences *")
        return self.cursor.fetchall()

    def closeConn():
        self.connection.close()
