import sqlite3

class rgr:
    def __init__(self):
        with sqlite3.connect('accounts.db') as self.conn:
            self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS User(username text, password text, FN text, LN text, email text)")

        self.cursor.execute('SELECT * FROM User WHERE (username=:user)', {'user':"admin"})
        entry = self.cursor.fetchone()
        if entry is None:
            self.cursor.execute("INSERT INTO User VALUES(:user, :pass, :first, :last, :email)",
                               {'user':"admin",'pass':"123456",'first':"Test",'last':"Scenario",'email':"ajsdn@something.com"})
            self.conn.commit()
        
        self.Username = ""
        self.Password = ""
        self.FirstName = ""
        self.LastName = ""
        self.email = ""
    
    def checkUser(self,a):
        self.cursor.execute("SELECT * FROM User WHERE (username=:user)",{'user': a})
        info = self.cursor.fetchone()
        if info == None:
            self.Username = a
            return "DoesNotExist"
        else:
            return "Exist"
    
    def setPassword(self,a):
        self.Password = a
        
    def setFirstName(self,a):
        self.FirstName = a
        
    def setLastName(self,a):
        self.LastName = a
        
    def setEmail(self,a):
        self.email = a
    
    def sendToFile(self):
        if self.Username != "":
            self.cursor.execute("INSERT INTO User VALUES(:user, :pass, :first, :last, :email)",
                                {'user':self.Username,'pass':self.Password,'first':self.FirstName,'last':self.LastName,'email':self.email})
            self.conn.commit()
    
    def closeDataBase(self):
        self.conn.close()