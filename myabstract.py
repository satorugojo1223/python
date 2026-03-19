from abc import ABC,abstractmethod
class abcclass(ABC):
    def print(self,x):
        print("the value is ",x)

        @abstractmethod
        def task(self):
            pass

class subclass(abcclass):
    def task(self):
        print("i am from subclass")


obj1 = subclass()
obj1.print(123)
obj1.task()