class Dog:
    species = "Canine"   # class variable

    def __init__(self, name, breed):
        self.name = name      # instance variable
        self.breed = breed    # instance variable

    def display(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Species:", Dog.species)
        print("-----")


# Creating two dog objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Rocky", "German Shepherd")

# Display details
dog1.display()
dog2.display()