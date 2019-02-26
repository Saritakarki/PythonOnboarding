
class GiveString:
    def __init__(self):
        self.inputStr = ""
        self.finalString = ""

    def get_string(self):
        self.inputStr = input("Enter the string")

    def print_string(self):
        self.finalString = self.inputStr.upper()
        print("String is: ", self.finalString)


if __name__ == '__main__':
    test = GiveString()
    test.get_string()
    test.print_string()
    