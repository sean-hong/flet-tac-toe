import flet as ft

def main(page: ft.Page):
    display_symbols = [''] * 9

    # click event
    def do_something(e):
        e.control.content.value = 'x'
        display_symbols[e.control.key] = 'x'
        page.update()

    # create the grid board
    grid_board = ft.GridView(
        expand = True,
        runs_count = 3
    )

    # fill each grid cell with a click handler
    for i in range(0, 9):
        grid_board.controls.append(
            ft.GestureDetector(
                key = i,
                content = ft.Text(
                    value = '',
                    expand = True,
                    text_align = ft.TextAlign.CENTER,
                    color = "white",
                    size = 50,
                    bgcolor = "blue"
                ),
                mouse_cursor = ft.MouseCursor.CLICK,
                on_tap = do_something
            )
        )

    # add element to the page
    page.controls.append(grid_board)

    # update the view
    page.update()

# run app
ft.app(target=main)
