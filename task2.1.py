class TestString:
    def __init__(self):
        self.inputStr = ""

    def getString(self):
        self.inputStr = input("Enter the string")

    def printString(self):
        print("String is: ", self.inputStr.upper())


test = TestString()
test.getString()
test.printString()

