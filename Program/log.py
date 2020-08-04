import sqlite3


class lgn:
    def __init__(self):
        with sqlite3.connect('accounts.db') as self.conn:
            self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS User(username text, password text, FN text, LN text, email text)")

        self.cursor.execute(
            'SELECT * FROM User WHERE (username=:user)', {'user': "admin"})
        entry = self.cursor.fetchone()
        if entry is None:
            self.cursor.execute("INSERT INTO User VALUES(:user, :pass, :first, :last, :email)",
                                {'user': "admin123", 'pass': "123456", 'first': "Test", 'last': "Acc", 'email': "testacc@something.com"})
            self.conn.commit()

        self.FirstName = ""
        self.LastName = ""

    def checkAccount(self, a, b):
        self.cursor.execute(
            "SELECT * FROM User WHERE (username=:user)", {'user': a})
        info = self.cursor.fetchone()
        if info != None:
            if b == info[1]:
                self.FirstName = info[2]
                self.LastName = info[3]
                return("correct")
            else:
                self.FirstName = ""
                self.LastName = ""
                return("incorrect")
        else:
            return "DoesNotExist"

    def getFirstName(self):
        return self.FirstName

    def getLastName(self):
        return self.LastName

    def closeDataBase(self):
        self.conn.close()
