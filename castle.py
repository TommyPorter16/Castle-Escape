"""
CMPUT 175 Assignment 3 - Castle Class
Tommy Porter
"""
from diamond import Diamond
from room import Room

class Castle:
    def __init__(self):
        """This function initializes the Castle with a rooms dictionary"""
        self.rooms = {}
    
    def __str__(self):
        """This function returns a string representation of the Castle"""
        string = ""
        for ID,room in self.rooms.items():
            string += (str(ID) + " ")
        return string
    
    def add_room(self, room):
        """This function adds a room to the Castle"""
        if room.get_id() in self.rooms:
            raise Exception("This room is already in the castle.")
        self.rooms[room.get_id()] = room     
    
    def get_room(self, ID):
        """This function gets a room from the Castle if the given ID is valid"""
        if ID not in self.rooms:
            raise Exception("This room ID is not in the castle.")
        return self.rooms[ID]
    
    def change_room(self, ID, new_room):
        """This function changes a given room to a new room"""
        if ID < 1 or ID > 25:
            raise Exception("Room ID is invalid.")
        self.rooms[ID] = new_room
    
    def get_entrance_id(self):
        """This function returns the ID of the room with the entrance"""
        entrance = None
        directions = ["north","east","south","west"]
        for ID,room in self.rooms.items():
            for direction in directions:
                if room.get_door(direction) == "entrance":
                    entrance = ID
        return entrance
    
    def get_exit_id(self):
        """This function returns the ID of the room with the exit"""
        exit = None
        directions = ["north","east","south","west"]
        for ID,room in self.rooms.items():
            for direction in directions:
                if room.get_door(direction) == "exit":
                    exit = ID
        return exit        
    
    def get_next_room(self, room_id, door):
        """
        This function returns the next room for a given room and door
        as well as whether the next room has a Portal or Wormhole
        """
        P = False
        W = False
        room = self.rooms[room_id]
        next_room = room.get_door(door)
        if isinstance(next_room,int):
            next_room = self.rooms[next_room]
            if next_room.get_portal():
                next_room = self.get_entrance_id()
                P = True
            elif next_room.get_wormhole():
                next_room = next_room.generate_random_room_id()
                W = True
            else:
                next_room = next_room.get_id()
        return next_room, P, W