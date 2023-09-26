import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="white")
    page.controls.append(t)
    page.update()

ft.app(target=main)
