class StringReverse:
    def __init__(self, text):
        self.__text = text   # private variable (encapsulation)

    def reverse_words(self):
        words = self.__text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)


# Example usage
s = StringReverse("Hello this is Percy Jackson")
result = s.reverse_words()
print(result)