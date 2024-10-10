import random
import numpy as np

# Define the size of the Hex board
BOARD_DIM = 13

# Define neighbors for hexagonal connections
neighbors = [-(BOARD_DIM+2) + 1, -(BOARD_DIM+2), -1, 1, (BOARD_DIM+2), (BOARD_DIM+2) - 1]

# Define the structure of the Hex game as a class
class HexGame:
    def __init__(self):
        # The board is initialized as a 2D array (flattened for convenience)
        self.board = np.zeros(((BOARD_DIM+2)*(BOARD_DIM+2)*2), dtype=int)
        self.open_positions = [(i*(BOARD_DIM + 2) + j) for i in range(1, BOARD_DIM+1) for j in range(1, BOARD_DIM+1)]
        self.number_of_open_positions = BOARD_DIM * BOARD_DIM
        self.moves = np.zeros(BOARD_DIM * BOARD_DIM, dtype=int)
        self.connected = np.zeros(((BOARD_DIM+2)*(BOARD_DIM+2)*2), dtype=int)
        self._init_board()

    # Initialize the game board
    def _init_board(self):
        for i in range(BOARD_DIM+2):
            for j in range(BOARD_DIM+2):
                if i == 0:
                    self.connected[(i*(BOARD_DIM + 2) + j) * 2] = 1
                if j == 0:
                    self.connected[(i*(BOARD_DIM + 2) + j) * 2 + 1] = 1

    # Check if the board is full
    def full_board(self):
        return self.number_of_open_positions == 0

    # Place a piece randomly
    def place_piece_randomly(self, player):
        random_empty_position_index = random.randint(0, self.number_of_open_positions - 1)
        empty_position = self.open_positions[random_empty_position_index]

        self.board[empty_position * 2 + player] = 1

        # Convert the actual board position to the relative index in a BOARD_DIM x BOARD_DIM grid
        relative_position = (empty_position // (BOARD_DIM + 2) - 1) * BOARD_DIM + (empty_position % (BOARD_DIM + 2) - 1)
        self.moves[BOARD_DIM * BOARD_DIM - self.number_of_open_positions] = relative_position

        # Update the list of open positions
        self.open_positions[random_empty_position_index] = self.open_positions[self.number_of_open_positions - 1]
        self.number_of_open_positions -= 1

        return empty_position

    # Check if a player has won
    def winner(self, player, position):
        for i in range(6):
            neighbor = position + neighbors[i]
            if self.connected[neighbor * 2 + player]:
                return True
        return False

    # Print the game board
    def print_board(self):
        for i in range(BOARD_DIM):
            print(" " * i, end="")
            for j in range(BOARD_DIM):
                if self.board[((i+1)*(BOARD_DIM+2) + j + 1)*2] == 1:
                    print(" X", end="")
                elif self.board[((i+1)*(BOARD_DIM+2) + j + 1)*2 + 1] == 1:
                    print(" O", end="")
                else:
                    print(" ·", end="")
            print()

# Main function to simulate games
def main():
    # Open a file to write the results
    with open("hex_game_results_13.csv", "w") as output_file:
        output_file.write("Game ID,Winner,Moves\n")
        for game in range(100):
            hg = HexGame()
            player = 0
            winner = -1

            # Simulate the game
            while not hg.full_board():
                position = hg.place_piece_randomly(player)
                if hg.winner(player, position):
                    winner = player
                    break
                player = 1 - player  # Switch player

            # Write the result to the file
            output_file.write(f"{game},{winner},")
            output_file.write(" ".join(map(str, hg.moves[:BOARD_DIM*BOARD_DIM - hg.number_of_open_positions])))
            output_file.write("\n")

            if game % 100000 == 0:
                print(f"Game {game} completed")

if __name__ == "__main__":
    main()
