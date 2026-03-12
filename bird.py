class bird:
    def __init__(self):
        print("the bird is initialized")

    def feathers(self):
        print("i have feathers and wings")

class penguin(bird):
    def __init__(self):

        super().__init__()
        print("the penguin is ready")
    def swim(self):
        print("i am an expert swimmer")

penguin1 = penguin()
penguin1.feathers()
penguin1.swim()
