"""
CMPUT 175 Assignment 3 - Main function
Tommy Porter
"""
from game import Game

def main():
    """
    This function runs the game, does the moves, sets the turns and prints the 
    paths and Diamonds of both players
    """
    game = Game()
    game.initialize_from_file("castle.txt")
    
    while not game.is_finished():
        print("It is Player " + str(game.get_turn()+1) + " turn")
        game.move()
        if not game.is_finished():
            game.next_turn(game.get_turn())
            
    print("The game is finished!")
    game.get_player(0).print_path()
    game.get_player(1).print_path()
    print("Final score is... Player 1: " + str(game.get_player(0).get_diamonds()) + " diamonds, Player 2: " + str(game.get_player(1).get_diamonds()) + " diamonds! Good Game!")
        
main()