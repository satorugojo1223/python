class myclass:
    __privar = 89:

    def __privmeth(self):
        print("Hello from private method")

    def publicmeth(self):
        print("the value of the private variable is ", myclass.__privar)

obj1 = myclass()
obj1.publicmeth()
obj1.__privmeth()