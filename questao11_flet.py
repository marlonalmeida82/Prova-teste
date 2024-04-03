import flet as ft

def main(page: ft.Page):
    # Cria uma lista vazia para armazenar as compras
    compras = []
    
    # Cria um Text para exibir a lista de compras
    lista_compras_text = ft.Text(value=" ")

    # Cria um campo de texto para inserir o nome da fruta
    nome_item_input = ft.TextField(
        label="Adicione um item à lista",
        autofocus=True,
    )

    # Cria um botão para adicionar um novo item
    def adicionar_novo_item(e):
        # Obtém o nome do item do campo de texto
        nome_item = nome_item_input.value

        # Adiciona o novo item à lista
        compras.append(nome_item)

        # Atualiza o texto da lista
        lista_compras_text.value = "\n".join(compras)

        # Limpa o campo de texto
        nome_item_input.value = ""

        # Atualiza a página
        page.update()

    # Cria um botão para remover o último item
    def remover_ultimo_item(e):
        # Remove o último item da lista
        compras.pop()

        # Atualiza o texto da lista
        lista_compras_text.value = "\n".join(compras)

        # Atualiza a página
        page.update()
    def ordenar_lista(e):
        # Ordena a lista
        compras.sort()

        page.update()

        # Atualiza o texto da lista
        lista_compras_text.value = "\n".join(compras)

        # Atualiza a página
        page.update()

    def inverte_lista(e):
        compras.reverse()

        lista_compras_text.value = "\n".join(compras)

        page.update()

    # Cria um botão para adicionar um novo item
    adicionar_novo_item_btn = ft.ElevatedButton(
        text="Adicionar",
        on_click=adicionar_novo_item,
    )
    ordenar_lista_btn = ft.ElevatedButton(
        text="Ordenar",
        on_click=ordenar_lista,
    )
    # Cria um botão para remover o último item
    remover_ultimo_item_btn = ft.ElevatedButton(
        text="Remover",
        on_click=remover_ultimo_item,
    )

    inverter_lista_btn = ft.ElevatedButton(
        text="Inverter",
        on_click=inverte_lista
    )
    page.horizontal_alignment="CENTER"
    
    page.update()
    # Adiciona os widgets à página
    page.add(
        nome_item_input,
        adicionar_novo_item_btn,
        remover_ultimo_item_btn,
        ordenar_lista_btn,
        inverter_lista_btn,
        lista_compras_text,

    )

ft.app(target=main)   


