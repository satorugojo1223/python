import random
import string

# Define characters to use
characters = string.ascii_letters + string.digits  

# Generate password of length 8
password = ''.join(random.choice(characters) for _ in range(8))

print("Your random password is:", password)