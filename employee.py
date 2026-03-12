class person:
    def __init__(self,name,id):
        self.id = id
        self.name = name

    def display(self):
        print('my name is',self.name)
        print("my id is",self.id)

class employee(person):
    def __init__(self,name,id,salary,post)
        person.__init__(self,name,id)
        self.salary = salary
        self.post = post
    def display1(self):
        person.display(self)
        print("my salary is",self.salary)
        print("my post is ",self,post)

emp1 = employee("john",1234321,50000,"supervisior")

emp1.display()
