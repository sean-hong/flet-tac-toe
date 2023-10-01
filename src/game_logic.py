def game_is_tied(grid: list) -> bool:
    return '' in grid

def check_for_win(grid: list, player: str, computer: str) -> None:
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
        pass
    elif COMPUTER_WIN in WINNING_VALUES:
        pass
    elif game_is_tied:
        pass
    else:
        pass
