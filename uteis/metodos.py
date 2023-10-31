# metodos.py

import os
import pywhatkit
from datetime import datetime
from time import sleep
from pynput.keyboard import Key, Controller
from config import contatos_arquivo, mensagem_arquivo, diretorio_imagens, tempo_entre_envios, tempo_fechar_guia

def fechar_guia():
    """Gera um comando de 'CTRL' + 'W' para fechar a guia do navegador"""
    tecla = Controller()
    tecla.press(Key.ctrl)
    tecla.press('w')
    tecla.release(Key.ctrl)
    tecla.release('w')
    sleep(tempo_fechar_guia)  # Aguarda um tempo para fechar a guia

def carregar_lista():
    """Carrega a lista de contatos do arquivo especificado"""
    try:
        lista = list()
        with open(contatos_arquivo, 'r') as arq:
            for valor in arq:
                lista.append(valor.replace('\n', ''))
    except:
        print('Erro ao localizar o arquivo de contatos!')
    finally:
        arq.close()
    return lista

def ler_mensagem():
    """Lê o conteúdo do arquivo de mensagem e retorna como mensagem"""
    with open(mensagem_arquivo, 'r', encoding='utf-8') as file:
        mensagem = file.read()
    return mensagem

def enviar_mensagens_com_imagens():
    lista = carregar_lista()
    if not lista:
        print("Lista de contatos vazia.")
        return

    caminhos_imagens = [os.path.join(diretorio_imagens, img) for img in os.listdir(diretorio_imagens) if os.path.isfile(os.path.join(diretorio_imagens, img))]

    if not caminhos_imagens:
        print(f'Nenhuma imagem encontrada em {diretorio_imagens}.')
        return

    try:
        log_sucesso = []
        log_falha = []

        mensagem = ler_mensagem()

        for contato in lista:
            for caminho_imagem in caminhos_imagens:
                try:
                    pywhatkit.sendwhats_image(contato, caminho_imagem, mensagem, datetime.now().hour, datetime.now().minute + 1)
                    log_sucesso.append(contato)
                except Exception as e:
                    log_falha.append(f"Erro ao enviar para {contato}: {str(e)}")

                sleep(tempo_entre_envios)
            
            if contato != lista[-1]:
                sleep(tempo_entre_envios)

        fechar_guia()  # Fechar a guia do navegador após enviar todas as mensagens

        print('\033[7m\n -> Mensagens enviadas!\033[m')
        print(f'\033[32mEnvio realizado com sucesso para: {log_sucesso}\033[m')
        print(f'\033[31mFalha no envio para: {log_falha}\033[m')

        # Salvar logs em arquivos separados
        with open('envios_sucesso.log', 'w') as file:
            file.write('\n'.join(log_sucesso))

        with open('envios_falha.log', 'w') as file:
            file.write('\n'.join(log_falha))

    except Exception as e:
        print(f'Falha ao enviar mensagens. Erro: {str(e)}')

if __name__ == "__main__":
    enviar_mensagens_com_imagens()