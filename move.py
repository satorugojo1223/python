from abc import ABC,abstractmethod

class animal(ABC):

    @abstractmethod
    def move(self):
        pass

class human(animal):
    def move(self):
        print("i can move by walking")
    
class bird(animal):
    def move(self):
        print("i can move by flying")

class snake(animal):
    def move(self):
        print("i can move by crawling")
    
class fish(animal):
    def move(self):
        print("i can move by swimming")

h1 = human()
h1.move()
s1 = snake()
s1.move()
b1.move()
f1 = fish()
f1.move()
