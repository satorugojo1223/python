def shutdown(command):
    if command.lower() == "yes":
        return "Shutting down..."
    elif command.lower() == "no":
        return "Shutdown aborted!"
    else:
        return "Invalid input"

# Example usage
print(shutdown("yes"))
print(shutdown("no"))
print(shutdown("maybe"))