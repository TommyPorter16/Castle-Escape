"""
CMPUT 175 Assignment 3 - Game Class
Tommy Porter
"""
from diamond import Diamond
from room import Room
from player import Player
from castle import Castle

class Game:
    def __init__(self):
        """This function initializes the Game"""
        self.castle = Castle()
        self.p1 = Player(0)
        self.p2 = Player(1)
        self.players = [self.p1, self.p2]
        self.finished = [False,False]
        self.turn = 0
        
    def __str__(self):
        """This function returns a string representation of the castle in the game"""
        return str(self.castle)
        
    def initialize_from_file(self, filename):
        """
        This function gets the data from the file and initializes all
        the rooms in the castle and the starting position for the players
        """
        new_data =[]
        with open("castle.txt","r") as file:
            data = file.readlines()
        for line in data:
            new_line = line.strip("\n")
            new_line = new_line.replace(":",",")
            new_line = new_line.split(', ')
            if len(new_line) == 5:
                new_line[4] = new_line[4].strip(",")
            new_data.append(new_line)       
        for i in range(2,len(new_data)):
            P = False
            W = False
            D = None
            if len(new_data[i]) == 6:
                if new_data[i][5] == "P":
                    P = True                
                elif new_data[i][5] == "W":
                    W = True
                else:
                    D = Diamond(len(new_data[i][5]))
            for j in range(5):
                if new_data[i][j] == "E":
                    new_data[i][j] = "entrance"
                elif new_data[i][j] == "X":
                    new_data[i][j] = "exit"
                elif new_data[i][j] == "0":
                    new_data[i][j] = None
                else:
                    new_data[i][j] = int(new_data[i][j])
            
            self.castle.add_room(Room(new_data[i][0],new_data[i][1],new_data[i][2],new_data[i][3],new_data[i][4],P,W,D))
        for player in self.players:
            player.set_position(int(new_data[0][1]))
    
    def get_turn(self):
        """This function returns the current turn"""
        return self.turn
    
    def set_turn(self, turn):
        """This function sets the current turn if the turn is valid"""
        if turn != 0 and turn != 1:
            raise Exception("Turn must be 0 or 1.")
        self.turn = turn
        
    def next_turn(self,turn):
        """This function checks whos turn it will be next"""
        if (turn == 0 and self.finished[1] == False) or self.finished[0] == True:
            self.set_turn(1)
        else:
            self.set_turn(0)
    
    def get_player(self, player_id):
        """This function returns the player for the given player ID if the ID is valid"""
        if player_id != 0 and player_id != 1:
            raise Exception("Player ID must be either 0 or 1.")
        return self.players[player_id]
    
    def move(self):
        """
        This function gets a valid direction from the user, moves the player to
        the next room, and prints where the player was previoussly and is now.
        """
        directions = ["north", "east", "south", "west"]
        direction = input("Which direction would you like to go? ")
        current_room = self.players[self.turn].get_position()
        while direction not in directions or self.castle.get_next_room(current_room,direction) == (None, False, False):
            direction = input("Which direction would you like to go? ")
        next_room,P,W = self.castle.get_next_room(current_room,direction)
        self.players[self.turn].add_to_path(current_room,direction)
        self.players[self.turn].move(next_room)
        print("Player " + str(self.turn +1) + ", previous room " + str(current_room))
        if P:
            print("You entered a Portal")
        if W:
            print("A Wormhole devoured you")
        if next_room == "exit":
            print("Player " + str(self.turn +1) + " exited the castle!")
        else:
            self.update_diamonds()
            print("Player " + str(self.turn +1) + ", " + str(direction) + ", next room " + str(next_room))
            
    def is_finished(self):
        """
        This function checks if both the players are finished and returns 
        whether the game is over
        """
        finish = False
        for i in range(len(self.players)):
            if self.players[i].get_position() == "exit":
                self.finished[i] = True
        if self.finished[0] == True and self.finished[1] == True:
            finish = True
        return finish
    
    def update_diamonds(self):
        """
        This function adds the current rooms diamonds to the players diamonds
        and sets the current rooms diamonds to None
        """
        current_player = self.players[self.turn]
        current_room_id = current_player.get_position()
        current_room = self.castle.get_room(current_room_id)
        if current_room.get_diamond():
            current_player.set_diamonds(current_player.get_diamonds()+current_room.get_diamond().get_diamonds())
            print("Number of Diamonds: " + str(current_room.get_diamond().get_diamonds()) + ", Total: " + str(current_player.get_diamonds()))
            current_room.set_diamond(None)