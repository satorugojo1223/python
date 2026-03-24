def mirrored_triangle(n):
    for i in range(1, n+1):
        print(" " * (n - i) + "*" * i)

# Example usage
rows = int(input("Enter number of rows: "))
mirrored_triangle(rows)