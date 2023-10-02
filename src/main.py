import flet as ft
from game_logic import check_for_game_over, computer_move

def main(page: ft.Page):
    display_symbols = [''] * 9

    game_over = False

    player_symbol = 'X'
    computer_symbol = 'O'

    # click event
    def show_action(e):
        nonlocal game_over

        if not game_over:
            e.control.content.controls[1].content.value = player_symbol
            display_symbols[e.control.key] = player_symbol

            # update page
            page.update()

            # check game results
            if check_for_game_over(display_symbols, player_symbol, computer_symbol):
                game_over = True
                return

            computer_action = computer_move(display_symbols)
            grid_board.controls[computer_action].content.controls[1].content.value = computer_symbol
            display_symbols[computer_action] = computer_symbol

            # update page
            page.update()

            # check game results
            if check_for_game_over(display_symbols, player_symbol, computer_symbol):
                game_over = True
                return

    # create the grid board
    grid_board = ft.GridView(expand=True, runs_count=3)

    # fill each grid cell with a click handler
    for i in range(0, 9):
        grid_board.controls.append(
            ft.GestureDetector(
                key = i,
                content = ft.Stack([
                    ft.Image("https://www.svgrepo.com/show/101416/square-outline.svg", expand=True),
                    ft.Container(
                        content = ft.Text('', expand=True, text_align=ft.TextAlign.CENTER, size=50, color="white"),
                        expand = True,
                        alignment = ft.alignment.center
                    )
                ]),
                mouse_cursor = ft.MouseCursor.CLICK,
                on_tap = show_action
            )
        )

    # add widget to the page
    page.controls.append(grid_board)

    # update the view
    page.update()

# run app
ft.app(target=main)
