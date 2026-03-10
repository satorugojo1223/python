class employee:
    def __init__(self):
        print("the object is created")

    def __del__(self):
        print("the object is destructed")

emp1 = employee()
del emp1