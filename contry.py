class India:
    def capital(self):
        print("the capital of india is delhi")
    def language(self):
        print("the widely spoken language in india is hindi")
    def weather(self):
        print("THE WEATHER OF INDIA is HOT")

class USA:
    def capital(self):
        print("the capital of usa is washington dc")
    def language(self):
        print("the widely spoken language in usa is english")
    def weather(self):
        print("THE WEATHER OF USA is ColD")

ob1 = India()
obj2 = USA()

for country in (obj1,obj2):
    country.capital()
    country.language()
    country.weather()