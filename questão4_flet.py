#importando pacote - as(apelido)
import flet as ft

def main(page:ft.Page): #definição do objeto página
    #Text - Títilo
    #TextField - caixinha de texto
    #button - (entrar no site flet.dev, ir na parte de configuração lá tem os tipos de botões)
    def clique_btn1(e): # e = evento 
        print("hoje é Domingo")
        page.update()
    def clique_btn2(e): # e = evento 
        print("Hoje é Segunda-feira")
        page.update()
    def clique_btn3(e): # e = evento 
        print("Hoje é Terça-feira")
        page.update()
    def clique_btn4(e): # e = evento 
        print("Hoje é Quarta-feira")
        page.update()
    def clique_btn5(e): # e = evento 
        print("Hoje é Quinta-feira")
        page.update()
    def clique_btn6(e): # e = evento 
        print("Hoje é Sexta-feira")
        page.update()
    def clique_btn7(e): # e = evento 
        print("Dia do senhor")
        page.update()
    btn1 = ft.ElevatedButton("Dia da semana 1",on_click=clique_btn1)
    btn2 = ft.ElevatedButton("Dia da semana 2",on_click=clique_btn2)
    btn3 = ft.ElevatedButton("Dia da semana 3",on_click=clique_btn3)
    btn4 = ft.ElevatedButton("Dia da semana 4",on_click=clique_btn4)
    btn5 = ft.ElevatedButton("Dia da semana 5",on_click=clique_btn5)
    btn6 = ft.ElevatedButton("Dia da semana 6",on_click=clique_btn6)
    btn7 = ft.ElevatedButton("Dia do senhor 7",on_click=clique_btn7)
    page.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    pass

ft.app(target=main)