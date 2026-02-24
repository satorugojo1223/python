# Take input from user
set1 = set(map(int, input("Enter numbers for Set 1 separated by space: ").split()))
set2 = set(map(int, input("Enter numbers for Set 2 separated by space: ").split()))

# Find symmetric difference
result = set1.symmetric_difference(set2)

# Print result
print("Symmetric Difference is:", result)