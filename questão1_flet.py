import flet as ft

def main (page: ft.page):
    txt_hello = ft.Text("Alô Mundo!")

    page.add(txt_hello)

ft.app(target=main)