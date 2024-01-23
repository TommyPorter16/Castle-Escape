"""
CMPUT 175 Assignment 3 - Room Class
Tommy Porter
"""
from diamond import Diamond
import random

class Room:
    def __init__(self, ID = None, north = None, south = None, east = None, west = None, portal: bool = False, wormhole: bool = False, diamond: Diamond = None):
        """This function initializes the room with each direction and state"""
        self.ID = ID
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.portal = portal
        self.wormhole = wormhole
        self.diamond = diamond
        self.directions = [self.north, self.east, self.south, self.west]
        
    def __str__(self):
        """This function returns a string representation of the room"""
        return ("This is room " + str(self.ID))
    
    def get_id(self):
        """This function returns the ID of the room"""
        return self.ID
    
    def set_id(self, ID: int):
        """This function sets the ID of the room if the ID is valid"""
        if type(ID) != int:
            raise Exception("Room ID must be an interger.")
        self.ID = ID
    
    def generate_random_room_id(self):
        """This function returns a random ID for a new room"""
        new_ID = self.ID
        if self.wormhole == False:
            raise Exception("There is no wormhole in this room.")
        while new_ID == self.ID:
            new_ID = random.randint(1,25)
        return new_ID
    
    def get_portal(self):
        """This function returns whether there is a portal in the room"""
        return self.portal
    
    def set_portal(self, portal: bool):
        """This function puts a portal in the room if possible"""
        print(self.wormhole)
        print(self.diamond)
        if self.wormhole or self.diamond:
            raise Exception("A portal cannot be added to this room.")
        self.portal = portal
    
    def get_wormhole(self):
        """This function returns whether there is a wormhole in the room"""
        return self.wormhole
    
    def set_wormhole(self, wormhole: bool):
        """This function puts a wormhole in the room if possible"""
        if self.portal or self.diamond:
            raise Exception("A wormhole cannot be added to this room.")        
        self.wormhole = wormhole
    
    def get_diamond(self):
        """This function returns the amount of diamonds in the room"""
        if self.diamond == None:
            return 0
        else:
            return self.diamond
    
    def set_diamond(self, diamond: Diamond):
        """This function puts a Diamond in the room if possible"""
        if self.wormhole or self.portal:
            raise Exception("A Diamond cannot be added to this room.")        
        self.diamond = diamond
    
    def get_door(self,direction: str):
        """This function returns whatever is in a given direction of the room"""
        directions = ["north", "east", "south", "west"]
        if direction not in directions:
            raise Exception("Pick a valid direction.")
        for i in range(len(directions)):
            if direction == directions[i]:
                return self.directions[i]  
    
    
    def set_link(self,direction: str, val):
        """This function sets the link to the next room in a given direction"""
        directions = ["north", "east", "south", "west"]
        if direction not in directions:
            raise Exception("Pick a valid direction.")     
        if not isinstance(val,int) and val != None and val != "entrance" and val != "exit":
            raise Exception("Invalid link.")
        for i in range(len(directions)):
            if direction == directions[i]:
                self.directions[i] = val        
        
    
    def isthere_entrance_exit_door(self):
        """This function checks whether there is an entrance or exit in the room"""
        in_out = False
        for direction in self.directions:
            if direction == "entrance" or direction == "exit":
                in_out = True
        return in_out
    
    
def main():
    r = Room(1)
    r.set_portal(True)
main()