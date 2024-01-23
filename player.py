"""
CMPUT 175 Assignment 3 - Player Class
Tommy Porter
"""
class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.position = None
        self.diamonds = 0
        self.path = []
        
    def __str__(self):
        return ("Player " + str(self.player_id)+ ". Diamond count: " + str(self.diamonds))
    
    def get_position(self):
        if not self.position:
            raise Exception("Position is not defined.")
        return self.position
    
    def set_position(self, position):
        if position < 1 or position > 25:
            raise Exception("Position is out of range.")   
        self.position = position
        
    def get_player_id(self):
        return self.player_id
    
    def get_diamonds(self):
        return self.diamonds
    
    def set_diamonds(self, count):
        if type(count) != int:
            raise Exception("Diamond amount must be an interger.")
        self.diamonds = count
        
    def print_path(self):
        route = ""
        for i in range(len(self.path)):
            route += self.path[i]
            if i < len(self.path)-1:
                route += ", "
        print(route)
        
    def add_to_path(self, room_id, door_id):
        self.path.append(str(room_id) + " -> " + str(door_id))
        
    def move(self, room_id):
        self.position = room_id
        
