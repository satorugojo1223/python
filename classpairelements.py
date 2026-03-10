class pair_elements:

    def twosum(self, tuple1, target):
        lookup = {}
        sum = 0
        for i, value in enumerate(tuple1):
            sum = sum + value
            lookup[i] = sum
            if sum >= target:
                print(lookup)
                return i


tuple1 = (10, 20, 30, 40, 50, 60, 70)
target = 100
obj1 = pair_elements()
print("the tuple reaches the target in the iteration",obj1.twosum(tuple1,target))