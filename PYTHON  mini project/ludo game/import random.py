import random

class LudoGame:
    def __init__(self):
        self.players = []
        self.current_player_index = 0
        self.board = Board()

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        print(f"Starting Ludo Game with {len(self.players)} players.")
        print(f"The current player is {self.players[self.current_player_index].name}.")

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        dice_roll = random.randint(1, 6)
        print(f"{current_player.name} rolled a {dice_roll}.")
        
        # Move the player's token on the board
        self.board.move_token(current_player, dice_roll)
        
        # Check for any special conditions (e.g., landing on a star or a snake)
        self.board.check_special_conditions(current_player)

        # Update the current player
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def end_game(self):
        print("Game Over!")

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0  # Starting position on the board

class Board:
    def __init__(self):
        self.tiles = [0] * 30  # Example: 30 tiles on the board

    def move_token(self, player, steps):
        player.position += steps
        if player.position >= len(self.tiles):
            player.position = len(self.tiles)  # Player has reached the end
            print(f"{player.name} has reached the end of the board!")

    def check_special_conditions(self, player):
        # Example: Check if the player landed on a special tile
        if player.position % 5 == 0:  # Example condition
            print(f"{player.name} landed on a special tile!")

    def is_game_over(self):
        # Check if any player has reached the end of the board
        return any(player.position >= len(self.tiles) for player in self.players)

# Create the Ludo Game instance
game = LudoGame()

# Create players
player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")
player4 = Player("Player 4")

# Add players to the game
game.add_player(player1)
game.add_player(player2)
game.add_player(player3)
game.add_player(player4)

# Start the game
game.start_game()

# Play turns until the game is over
while not game.board.is_game_over():
    game.play_turn()

# End the game
game.end_game()