#!/usr/bin/env python3

import math


# define Rectangle class

class Rectangle:

    def __init__(self, length, width):
        self.setLength(length)
        self.setWidth(width)

    def getLength(self):
        return self.__length

    def setLength(self, length):
        if length < 0:
            length = 1
        self.__length = length

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        if width < 0:
            width = 1
        self.__width = width

    def getArea(self):
        return self.__length * self.__width

    def __str__(self):
        return "Length: " + str(self.getLength()) + " feet \n" + "Width: " + str(self.getWidth()) + " feet \n"



# create child class, Rug, from Rectangle and inherit

class Rug(Rectangle):

    def __init__(self, length, width, price):
        Rectangle.__init__(self, length, width)
        self.setPrice(price)

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        if price < 0:
            price = price * -1
##        if price > 0:
##            price = Rectangle.getLength(self) * Rectangle.getWidth(self) * price
        self.__price = price

    def __str__(self):
        return Rectangle.__str__(self) + "Price: $" + str(self.getPrice()) + "\n"


# create a child class of, Carpet, from Rectangle and inherit

class Carpet(Rectangle):

    def __init__(self, length, width, price_per_square_foot):
        Rectangle.__init__(self, length, width)
        self.setPrice(price_per_square_foot)

    def getPrice(self):
        return self.__price_per_square_foot

    def setPrice(self, price_per_square_foot):
        if price_per_square_foot < 0:
            price_per_square_foot = price_per_square_foot * -1
        if price_per_square_foot > 0:
            price_per_square_foot = Rectangle.getLength(self) * Rectangle.getWidth(self) * price_per_square_foot
        self.__price_per_square_foot = price_per_square_foot
        # figuring price would never be negative, but also would not change to 1

    def __str__(self):
        return Rectangle.__str__(self) + "Price: $" + str("{:.2f}".format(self.getPrice())) + "\n"
        
        
    

# create main function
# Wasn't sure how much detail needed to be gone into here.
# Just used a simple for loop to run the list.

def main():
    
    print("Below is a sample list of Rug and Carpet prices. Rugs can be identified")
    print("by a fixed pricing ending in .99 cents, while carpets can be identified")
    print("by an example length of 10', which will cause the price to vary by width.")
    print()

    rugAndcarpetList = [ Rug( 3, 5, 49.99), Rug( 5, 8, 99.99), Rug( 9, 12, 199.99),
                        Rug( 12, 15, 249.99), Carpet( 10, 12, 1.09),
                         Carpet( 10, 13.5, 1.99), Carpet( 10, 15, 0.99)]

    for x in rugAndcarpetList:
        print(x)
        print()
        
main()

    
    
        
        







        
