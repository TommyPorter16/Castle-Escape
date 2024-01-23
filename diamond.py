"""
CMPUT 175 Assignment 3 - Diamond Class
Tommy Porter
"""

class Diamond:
    def __init__(self, diamonds:int = 1):
        """Initializes the diamond object (amount of diamonds)"""
        self.diamonds = diamonds
        
    def __str__(self):
        """Returns a string representation of the amount of the diamonds"""
        return ("Number of Diamonds: " + str(self.diamonds))
    
    def get_diamonds(self):
        """Returns the amount of diamonds in the object"""
        return self.diamonds
    
    def set_diamonds(self,amount:int):
        """Sets the amount of diamonds in the object"""
        if amount < 0:
            raise Exception("Diamond amount cannot be negative")
        self.diamonds = amount
        
