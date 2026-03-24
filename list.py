# 1. Squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)

# 2. Even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

# 3. Convert words to uppercase
words = ["python", "list", "comprehension"]
upper_words = [w.upper() for w in words]
print(upper_words)

# 4. First letter of each word
first_letters = [w[0] for w in words]
print(first_letters)
