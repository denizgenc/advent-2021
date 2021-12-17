#!/usr/bin/env python
from adventinput import get_data

def get_draws_and_tables():
    data = get_data(4)

    draws = [int(s) for s in data.pop(0).split(",")]

    boards = []
    temp_board = []
    for line in data:
        if line == "":
            if len(temp_board) == 0:
                continue
            else:
                boards.append(temp_board)
                temp_board = []
                continue
        else:
            # We want to create a 1 dimensional list instead of 5x5, so we use extend instead of
            # append.
            temp_board.extend([{"value": int(s), "marked": False} for s in line.split()])

    return draws, boards

def play_bingo(draws, boards):
    for draw_num, draw in enumerate(draws, start=1):
        # Mark boards
        for board in boards:
            if board is not None: # Previously winning board
                for num in board: # At this point it's clear I'm doing things the dumb way
                    if num["value"] == draw:
                        num["marked"] = True

        # Check for winners
        winning_boards = []
        if draw_num > 4: # Premature optimisation - can't win with less than 5 draws 😎
            for board_num, board in enumerate(boards):
                if board is None: # Previously winning board, skip
                    continue
                # why do I keep torturing myself with list comprehensions
                rows = [sum([num["marked"] for num in row]) for row in
                        [board[a:a+5] for a in range(0,21,5)]
                       ]
                if 5 in rows:
                    print(f"Board number {board_num} won!")
                    yield calculate_score(board, draw)
                    winning_boards.append(board_num)
                    continue
                cols = [sum([num["marked"] for num in col]) for col in
                        [board[a:-1:5] for a in range(0, 5)]
                       ]
                if 5 in cols:
                    print(f"Board number {board_num} won!")
                    yield calculate_score(board, draw)
                    winning_boards.append(board_num)

        # Clear winning boards from list
        for i in winning_boards:
            boards[i] = None

def calculate_score(board, draw):
    unmarked_sum = sum([num["value"] for num in board if not num["marked"]])
    return draw * unmarked_sum

if __name__ == "__main__":
    draws, boards = get_draws_and_tables()

    game = play_bingo(draws, boards)
    score = next(game)

    print(f"The score of the first board to win is {score}")

    # Get last item from generator. From https://stackoverflow.com/a/48232574
    *_, last = game
    print(f"The score for the final board to win is {last}")
