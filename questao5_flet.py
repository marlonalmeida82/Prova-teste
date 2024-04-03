#importando pacote - as(apelido)
import flet as ft

def main(page:ft.Page): #definição do objeto página
    #Text - Títilo
    #TextField - caixinha de texto
    #button - (entrar no site flet.dev, ir na parte de configuração lá tem os tipos de botões)
    def clique_btn1(e): # e = evento 
        print("Janeiro")
        page.update()
    def clique_btn2(e): # e = evento 
        print("Fevereiro")
        page.update()
    def clique_btn3(e): # e = evento 
        print("Março")
        page.update()
    def clique_btn4(e): # e = evento 
        print("Ablil")
        page.update()
    def clique_btn5(e): # e = evento 
        print("Maio")
        page.update()
    def clique_btn6(e): # e = evento 
        print("Junho")
        page.update()
    def clique_btn7(e): # e = evento 
        print("julho")
    def clique_btn8(e): # e = evento 
        print("Agosto")
    def clique_btn9(e): # e = evento 
        print("Setembro")
    def clique_btn10(e): # e = evento 
        print("Outubro")
    def clique_btn11(e): # e = evento 
        print("Novembro")
    def clique_btn12(e): # e = evento 
        print("Dezembro")
        page.update()
    btn1 = ft.ElevatedButton("Janeiro",on_click=clique_btn1)
    btn2 = ft.ElevatedButton("Fevereiro",on_click=clique_btn2)
    btn3 = ft.ElevatedButton("Março",on_click=clique_btn3)
    btn4 = ft.ElevatedButton("Abril",on_click=clique_btn4)
    btn5 = ft.ElevatedButton("Maio",on_click=clique_btn5)
    btn6 = ft.ElevatedButton("Junho",on_click=clique_btn6)
    btn7 = ft.ElevatedButton("Julho",on_click=clique_btn7)
    btn8 = ft.ElevatedButton("Agosto ",on_click=clique_btn8)
    btn9 = ft.ElevatedButton("Setembro",on_click=clique_btn9)
    btn10 = ft.ElevatedButton("Outubro",on_click=clique_btn10)
    btn11 = ft.ElevatedButton("Novembro",on_click=clique_btn11)
    btn12 = ft.ElevatedButton("Dezembro",on_click=clique_btn12)
    page.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)

    pass

ft.app(target=main)