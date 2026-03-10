class iostring:
    def __init__(self):
        self.str1 = "Book"

    def getsrting(self):
        self.str1 = input("enter a phase")

    def printstring(self):
        print("the given string in uppercase is :",self.str1.upper())

obj1 = iostring()
obj1.getsrting()
obj1.printstring()