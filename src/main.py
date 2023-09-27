import flet as ft

def main(page: ft.Page):
    # click event
    def do_something(argv=None):
        print("Hello, world!")

    # create the grid board
    grid_board = ft.GridView(
        expand = True,
        runs_count = 3
    )

    # fill each grid cell with a click handler
    for _ in range(0, 9):
        grid_board.controls.append(
            ft.GestureDetector(
                content = ft.Container(bgcolor=ft.colors.BLUE, width=50, height=50),
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
