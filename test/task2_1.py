
class GiveString:
    def __init__(self):
        self.inputStr = ""
        self.finalString = ""

    def get_string(self):
        self.inputStr = input("Enter the string")
        return self.inputStr

    def print_string(self):
        self.finalString = self.inputStr.upper()
        print("String is: ", self.finalString)
        return self.finalString


if __name__ == '__main__':
    test = GiveString()
    test.get_string()
    test.print_string()
