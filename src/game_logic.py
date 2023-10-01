from random import randrange

def computer_move(grid: list) -> int:
    random_index = randrange(len(grid))
    random_cell = grid[random_index]

    while random_cell:
        random_index = randrange(len(grid))
        random_cell = grid[random_index]

    return random_index

def game_is_playable(grid: list) -> bool:
    return '' in grid

def check_for_win(grid: list, player: str, computer: str) -> bool:
    # moves that win the game
    WINNING_MOVES = {
        'row1': f'{grid[0]}{grid[1]}{grid[2]}',
        'row2': f'{grid[3]}{grid[4]}{grid[5]}',
        'row3': f'{grid[6]}{grid[7]}{grid[8]}',
        'col1': f'{grid[0]}{grid[3]}{grid[6]}',
        'col2': f'{grid[1]}{grid[4]}{grid[7]}',
        'col3': f'{grid[2]}{grid[5]}{grid[8]}',
        'diag1': f'{grid[0]}{grid[4]}{grid[8]}',
        'diag2': f'{grid[2]}{grid[4]}{grid[6]}'
    }

    # 3 symbols required for a win
    PLAYER_WIN = player * 3
    COMPUTER_WIN = computer * 3

    # list of winning moves
    WINNING_VALUES = WINNING_MOVES.values()

    if PLAYER_WIN in WINNING_VALUES:
        print(f"{player} wins!")
        return True
    elif COMPUTER_WIN in WINNING_VALUES:
        print(f"{computer} wins!")
        return True
    elif not game_is_playable:
        print(f"tie")
        return True
    else:
        pass
