import edge_tts as et
import asyncio
import flet as ft
import os
from datetime import datetime

# Função para gerar o áudio a partir do texto
async def texto_para_audio(page, pb, vozes, finalizado, texto):
    voz = vozes.value
    
    # Cria um nome único para o arquivo com base no timestamp
    nome_do_arquivo = f"C:/Users/{os.getlogin()}/Documents/Audios Gerados/audio_gerado_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')}.mp3"
    
    tts = et.Communicate(texto, voz)

    try:
        print(f'Gerando áudio... Salvará em: {nome_do_arquivo}')
        await tts.save(nome_do_arquivo)  # Salva o áudio no arquivo
        print(f'Áudio salvo com sucesso em: {nome_do_arquivo}')
        finalizado.value = f"Áudio salvo em: {nome_do_arquivo}"
    except Exception as ex:
        finalizado.value = f"Erro ao gerar o áudio: {str(ex)}"
    finally:
        pb.visible = False
        page.update()

# Função principal que configura o layout do aplicativo
def main(page: ft.Page):
    texto_input = ft.TextField(
        label="Escreva seu texto aqui",
        border_color='white',
        label_style=ft.TextStyle(color='white'),
        color='grey',
        multiline=True,
        cursor_color='white'
    )

    pb = ft.ProgressBar(
        border_radius=360,
        width=40,
        height=40,
        color='white',
        visible=False  # Inicialmente a barra de progresso está invisível
    )

    finalizado = ft.Text()
    
    # Cria o diretório para salvar os áudios
    diretorio = f"C:/Users/{os.getlogin()}/Documents/Audios Gerados"
    os.makedirs(diretorio, exist_ok=True)
    print(f'Diretório criado ou já existe: {diretorio}')

    # Carregar vozes do arquivo
    vozes_txt = "vozes.txt"
    opcoes_voz = []
    if os.path.exists(vozes_txt):
        with open(vozes_txt, 'r') as arquivo:
            for linha in arquivo:
                voz = linha.split()[0]  # Pega apenas a primeira coluna
                opcoes_voz.append(ft.dropdown.Option(voz))
    else:
        print(f"Arquivo {vozes_txt} não encontrado. Usando vozes padrão.")
        opcoes_voz = [
            ft.dropdown.Option("pt-BR-AntonioNeural"),
            ft.dropdown.Option("pt-BR-FranciscaNeural"),
            ft.dropdown.Option("pt-BR-ThalitaMultilingualNeural")
        ]

    vozes = ft.Dropdown(
        hint_content=ft.Text("Escolha uma voz"),
        options=opcoes_voz
    )

    # Função para gerar o áudio quando o botão for clicado
    def gerar_audio(e):
        finalizado.value = None
        texto = texto_input.value.strip()  # Pega o texto inserido no campo
        if texto and vozes.value:  # Verifica se o texto e a voz foram selecionados
            pb.visible = True  # Exibe a barra de progresso
            page.update()  # Atualiza a interface
            print(f'Gerando áudio para o texto: {texto}')
            # Executa a função assíncrona
            asyncio.run(texto_para_audio(page, pb, vozes, finalizado, texto))
        else:
            finalizado.value = "Por favor, insira um texto e escolha uma voz."
            page.update()

    # Adiciona os controles na página
    page.add(
        ft.Column(
            expand=True,
            alignment='center',
            horizontal_alignment='center',
            controls=[
                vozes,
                texto_input,
                ft.ElevatedButton(
                    "Gerar Áudio",
                    bgcolor='purple',
                    color='white',
                    on_click=gerar_audio
                ),
                pb,  # Barra de progresso
                finalizado
            ]
        )
    )

if __name__ == '__main__':
    ft.app(target=main,assets_dir="assets")
