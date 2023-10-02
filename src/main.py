import flet as ft
from game_logic import check_for_game_over, computer_move

def main(page: ft.Page):
    display_symbols = [''] * 9

    game_over = False

    player_symbol = 'X'
    computer_symbol = 'O'

    # scale grid accordingly
    def update_grid_sizes(_):
        grid_board.width = page.window_width
        grid_board.height = page.window_height
        grid_board.child_aspect_ratio = grid_board.width / grid_board.height

        page.update()

    page.on_resize = update_grid_sizes

    # click event
    def run_game_logic(e):
        nonlocal game_over

        if not game_over:
            e.control.content.content.value = player_symbol
            display_symbols[e.control.key] = player_symbol

            # update page
            page.update()

            # check game results
            if check_for_game_over(display_symbols, player_symbol, computer_symbol):
                game_over = True
                return

            computer_action = computer_move(display_symbols)
            grid_board.controls[computer_action].content.content.value = computer_symbol
            display_symbols[computer_action] = computer_symbol

            # update page
            page.update()

            # check game results
            if check_for_game_over(display_symbols, player_symbol, computer_symbol):
                game_over = True
                return

    # create the grid board
    grid_board = ft.GridView(
        width = page.window_width,
        height = page.window_height,
        expand = True,
        runs_count = 3,
        # child_aspect_ratio = (page.window_width / page.window_height)
    )

    # fill each grid cell with a click handler
    for i in range(0, 9):
        grid_board.controls.append(
            ft.GestureDetector(
                key = i,
                content = ft.Container(
                    content = ft.Text('', expand=True, text_align=ft.TextAlign.CENTER, size=50, color="white"),
                    expand = True,
                    alignment = ft.alignment.center,
                    bgcolor = "red"
                ),
                mouse_cursor = ft.MouseCursor.CLICK,
                on_tap = run_game_logic
            )
        )

    # add widget to the page
    page.controls.append(grid_board)

    # update the view
    page.update()

# run app
ft.app(main)
