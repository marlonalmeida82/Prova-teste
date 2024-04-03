import flet as ft

def main(page: ft.Page):
    a1 = ft.Image(
       src="Logo.jpg",
       height=222
    )

    texto = ft.TextField(
        label=("Informe o seu nome: "),
        width=222,
        height=55,
    )

    msg = ft.Text("")

    def btn_click(e):
        msg.value = texto.value.upper()
        texto.value = ""

        page.update()

    btn = ft.ElevatedButton(
        "CONVERTER",
        width=222,
        height=55,
        on_click=btn_click
    )
    page.horizontal_alignment="CENTER"
    page.vertical_alignment="CENTER"
    page.add(a1, texto, btn, msg)
   
ft.app(target=main)


