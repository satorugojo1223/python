# Mirrored Right-Angled Triangle

rows = 5  # You can change this number for bigger/smaller triangle

for i in range(1, rows + 1):
    # Print spaces first, then stars
    print(" " * (rows - i) + "*" * i)