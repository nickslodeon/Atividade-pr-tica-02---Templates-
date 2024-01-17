#Importa o módulo flet
import flet as ft

#Informa o preenchimento obrigatório em campos vazios de um formulário 
def validate_required_text_field(e):
    if e.control.value == "":
       e.control.error_text = "Preenchimento obrigatório"
       e.control.update()

#Cria um formulário
def create_form(pg):
    return ft.SafeArea(
        ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[

                #Cria campos de texto com diferetes rótulos, referentes ao cadastro de clínicas
                ft.TextField (
                    label="Nome",
                    keyboard_type=ft.KeyboardType.NAME,
                    on_blur=validate_required_text_field,
                ),
                ft.TextField (
                    label="CNPJ",
                    keyboard_type=ft.KeyboardType.NAME,
                    on_blur=validate_required_text_field,
                ),
                ft.TextField (
                    label="Especialidades",
                    keyboard_type=ft.KeyboardType.NAME,
                    on_blur=validate_required_text_field,
                ),
                ft.TextField (
                    label="Email",
                    keyboard_type=ft.KeyboardType.NAME,
                    on_blur=validate_required_text_field,
                ),
                ft.TextField (
                    label="Telefone",
                    keyboard_type=ft.KeyboardType.NAME,
                    on_blur=validate_required_text_field,
                ),
                ft.TextField (
                    label="Endereco",
                    keyboard_type=ft.KeyboardType.NAME,
                    on_blur=validate_required_text_field,
                ),       
            ]   
        ),
    )

#Cria a função Principal
def main(page: ft.Page):

    #Define o título da página e o modo de rolagem
    page.title = "AraClin: Catálogo de Clínicas Médicas"
    page.scroll = "adaptive"

    #Adiciona textos e o formulário à página
    page.add(
        ft.Text("AraClin", size=30, color="green"),
        ft.Text("Cadastro de Clínica", size=20),
        create_form(main),
    )

    #Cria uma função, que será executada após o clique no botão de cadastrar, para informar o êxito
    def btn_click(e):
        page.add(ft.Text("Clínica cadastrada com sucesso!", color="green"))

    #Cria um botão com o texto "Cadastrar" e associa a função btn_click ao evento de clique
    page.add(
        ft.ElevatedButton("Cadastrar", on_click=btn_click),
    )

#Inicia a aplicação flet com a função principal como alvo e exibe no navegador web.
if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
