#Bren Rodriguez October 25, 2026 DEV 128 LA2
#SI-assisted: I used Claude to understand how to structure a class with__init__and a getStr() method, and why the test line inside the class casued an error.
class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def getStr(self):
        return f"{self.name} ({self.year})"

