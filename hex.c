#include <stdio.h>
#include <stdlib.h>

// Define the size of the Hex board
#ifndef BOARD_DIM
    #define BOARD_DIM 13
#endif

// Define neighbors for hexagonal connections
int neighbors[] = {-(BOARD_DIM+2) + 1, -(BOARD_DIM+2), -1, 1, (BOARD_DIM+2), (BOARD_DIM+2) - 1};

// Define the structure of the Hex game
struct hex_game {
    int board[(BOARD_DIM+2)*(BOARD_DIM+2)*2];
    int open_positions[BOARD_DIM*BOARD_DIM];
    int number_of_open_positions;
    int moves[BOARD_DIM*BOARD_DIM];
    int connected[(BOARD_DIM+2)*(BOARD_DIM+2)*2];
};

// Declare functions used later in the program
void hg_init(struct hex_game *hg);
int hg_full_board(struct hex_game *hg);
int hg_place_piece_randomly(struct hex_game *hg, int player);
int hg_winner(struct hex_game *hg, int player, int position);
void hg_print(struct hex_game *hg);

// Initialize the game
void hg_init(struct hex_game *hg) {
    for (int i = 0; i < BOARD_DIM+2; ++i) {
        for (int j = 0; j < BOARD_DIM+2; ++j) {
            hg->board[(i*(BOARD_DIM + 2) + j) * 2] = 0;
            hg->board[(i*(BOARD_DIM + 2) + j) * 2 + 1] = 0;

            if (i > 0 && i < BOARD_DIM + 1 && j > 0 && j < BOARD_DIM + 1) {
                hg->open_positions[(i-1)*BOARD_DIM + j - 1] = i*(BOARD_DIM + 2) + j;
            }

            if (i == 0) {
                hg->connected[(i*(BOARD_DIM + 2) + j) * 2] = 1;
            } else {
                hg->connected[(i*(BOARD_DIM + 2) + j) * 2] = 0;
            }

            if (j == 0) {
                hg->connected[(i*(BOARD_DIM + 2) + j) * 2 + 1] = 1;
            } else {
                hg->connected[(i*(BOARD_DIM + 2) + j) * 2 + 1] = 0;
            }
        }
    }
    hg->number_of_open_positions = BOARD_DIM*BOARD_DIM;
}

// Check if the board is full
int hg_full_board(struct hex_game *hg) {
    return hg->number_of_open_positions == 0;
}

// Place a piece randomly
int hg_place_piece_randomly(struct hex_game *hg, int player) {
    int random_empty_position_index = rand() % hg->number_of_open_positions;
    int empty_position = hg->open_positions[random_empty_position_index];

    hg->board[empty_position * 2 + player] = 1;

    // Convert the actual board position to the relative index in a BOARD_DIM x BOARD_DIM grid
    int relative_position = (empty_position / (BOARD_DIM + 2) - 1) * BOARD_DIM + (empty_position % (BOARD_DIM + 2) - 1);
    hg->moves[BOARD_DIM * BOARD_DIM - hg->number_of_open_positions] = relative_position;

    hg->open_positions[random_empty_position_index] = hg->open_positions[hg->number_of_open_positions - 1];
    hg->number_of_open_positions--;

    return empty_position;
}
// Check if a player has won
int hg_winner(struct hex_game *hg, int player, int position) {
    for (int i = 0; i < 6; ++i) {
        int neighbor = position + neighbors[i];
        if (hg->connected[neighbor*2 + player]) {
            return 1;
        }
    }
    return 0;
}

// Print the game board
void hg_print(struct hex_game *hg) {
    for (int i = 0; i < BOARD_DIM; ++i) {
        for (int j = 0; j < i; j++) {
            printf(" ");
        }

        for (int j = 0; j < BOARD_DIM; ++j) {
            if (hg->board[((i+1)*(BOARD_DIM+2) + j + 1)*2] == 1) {
                printf(" X");
            } else if (hg->board[((i+1)*(BOARD_DIM+2) + j + 1)*2 + 1] == 1) {
                printf(" O");
            } else {
                printf(" ·");
            }
        }
        printf("\n");
    }
}

// Main function
int main() {
    struct hex_game hg;
    int winner = -1;

    // Open a file to write the results
    FILE *output_file = fopen("hex_game_results_13.csv", "w");
    if (!output_file) {
        printf("Error opening file!\n");
        return 1;
    }
    // Write the header to the file
    fprintf(output_file, "Game ID,Winner,Moves\n");

    for (int game = 0; game < 10000000; ++game) {
        hg_init(&hg);
        int player = 0;
        winner = -1;

        // Simulate the game
        while (!hg_full_board(&hg)) {
            int position = hg_place_piece_randomly(&hg, player);
            if (hg_winner(&hg, player, position)) {
                winner = player;
                break;
            }
            player = 1 - player;
        }

        // Write the result to the file
        fprintf(output_file, "%d,%d,", game, winner);

        // Write the moves
        for (int i = 0; i < BOARD_DIM*BOARD_DIM - hg.number_of_open_positions; ++i) {
            fprintf(output_file, "%d ", hg.moves[i]);
        }
        fprintf(output_file, "\n");

        if (game % 100000 == 0) {
            printf("Game %d completed\n", game);
        }
    }

    fclose(output_file);  // Close the file
    return 0;
}
