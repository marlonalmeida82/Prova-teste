import flet as ft

def main(page: ft.Page):
    a1 = ft.Image(
       src="Logo.jpg",
       height=222
    )

    nome_maquina = ft.TextField(
        label= ("Informe o nome: "),
        width=222,
        height=55,
    )

    tempo_uso = ft.TextField(
        label= ("Informe o tempo de uso: "),
        width=222,
        height=55,
    )

    ligado = ft.TextField(
        label= ("Informe se está ligado (True - False): "),
        width=222,
        height=55,
    )

    msg1 = ft.Text("")
    msg2 = ft.Text("")
    msg3 = ft.Text("")
    
    def btn_click(e):
        msg1.value = nome_maquina.value
        nome_maquina.value = ""

        msg2.value = tempo_uso.value
        tempo_uso.value = ""

        msg3.value = ligado.value
        ligado.value = ""
        page.update()

    btn = ft.ElevatedButton(
        "ADICIONAR",
        width=222,
        height=55,
        on_click=btn_click
    )
    page.horizontal_alignment="CENTER"
    page.vertical_alignment="CENTER"
    page.add(a1, nome_maquina, tempo_uso, ligado, btn, msg1,msg2,msg3)
   
ft.app(target=main)