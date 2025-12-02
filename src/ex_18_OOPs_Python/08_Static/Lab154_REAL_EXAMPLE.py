class ExcelReader:
    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class MySQLDBConnection:
    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")

class TC1:
    def runTC(self):
        ExcelReader().readExcelFile()
        MySQLDBConnection().readMySQLFile()
        print("Hi")

class TC2:
    def runTC(self):
        ExcelReader().readExcelFile()
        MySQLDBConnection().readMySQLFile()
        print("Hi")

tc1 = TC1()
tc1.runTC()
# Reading from Excel
# Reading from MySQL
# Hi
tc2 = TC2()
tc2.runTC()
# Reading from Excel
# Reading from MySQL
# Hi