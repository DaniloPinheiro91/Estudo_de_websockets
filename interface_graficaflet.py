import flet as ft

def main(page):
    # Coloca a página em modo tela cheia
    page.fullscreen = True

    # Caminho para a imagem de fundo
    background = ft.Image(src="kratos.jpg", fit=ft.ImageFit.CONTAIN)

    # Layout com os botões e o título
    layout = ft.Column(
        controls=[
            ft.Text("JOGO GOD OF WAR", size=50, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton("JOGAR"),
            ft.ElevatedButton("CONFIGURAÇÕES"),
            ft.ElevatedButton("SAIR"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Alinha os itens no centro verticalmente
        horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alinha os itens no centro horizontalmente
    )

    # Usando o Stack para sobrepor a imagem de fundo e o layout
    stack = ft.Stack(
        controls=[background, layout],  # Colocando a imagem e o layout na pilha
        alignment=ft.alignment.center,  # Alinha ambos os widgets no centro
    )

    # Adicionando o stack à página
    page.add(stack)

# Iniciando a aplicação
ft.app(target=main)