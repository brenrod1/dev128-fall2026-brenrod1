# Bren Rodriguez, DEV128, October 30, 2026 Lab 3 - objects.py
# I used Claude to explain inheritance concepts and to debug errors.

from dataclasses import dataclass

@dataclass
class Product:
    name:str = ""
    price:float = 0.0
    discountPercent:int = 0

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name

@dataclass
class Media(Product):
    format:str = ""
    
@dataclass
class Book(Media):
    author:str = ""
   
    def getDescription(self):
        return f"{super().getDescription()} by {self.author}"
    
@dataclass        
class Movie(Media): 
    year:int = 0
    
    def getDescription(self):
        return f"{super().getDescription()} ({self.year})"

@dataclass
class Album(Media):
    artist:str = ""

    def getDescription(self):
        return f"{super().getDescription()} by {self.artist}"
    
@dataclass
class VideoGame(Media):
    platform:str = ""

    def getDescription(self):
        return f"{super().getDescription()} for {self.platform}"
