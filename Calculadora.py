import flet as ft

def main(pagina: ft.Page):
    
    # configuração
    pagina.title = "Calculadora DBJ"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    #funções

    def margem(evento):
        margem_bruta.value = str((float(caixa_pvc.value)*float(unidades.value)) - float(caixa_pvv.value))
        margem_percentual.value = str(round(((float(caixa_pvc.value)*float(unidades.value)) / float(caixa_pvv.value)-1)*100, 2))
        pagina.update()

    # itens
    txt_titulo = ft.Text("Calculadora de Margem DBJ")
    txt_pvv = ft.Text("Insira o preço de venda: ")
    caixa_pvv = ft.TextField(value=0, width=100)
    txt_pvc = ft.Text("Insira o preço na ponta: ")
    caixa_pvc = ft.TextField(value=0, width=100)
    txt_unidades = ft.Text("Insira a quantidade de unidades por embalagem: ")
    unidades = ft.TextField(value=0, width=100)
    botao_calcular = ft.ElevatedButton(text="Calcular", on_click=margem)
    txt_margem_bruta = ft.Text("Margem Bruta: R$")
    margem_bruta = ft.Text(value="0")
    txt_margem_percentual = ft.Text("Margem Percentual: ")
    margem_percentual = ft.Text(value="0")
    percentual = ft.Text("%")

    # mostrar itens na pagina
    pagina.add(
        ft.Row([txt_titulo], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([txt_pvv, caixa_pvv], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([txt_pvc, caixa_pvc], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([txt_unidades, unidades], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([botao_calcular], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([txt_margem_bruta, margem_bruta], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([txt_margem_percentual, margem_percentual, percentual], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)