import requests
import os
import random
import string

# Função para exibir o banner
def exibir_banner():
    print("━━━┒✨✨✨┎━━━")
    print("   Welcome!")
    print("  Let's find some pages!")
    print("━━━┖✨✨✨┚━━━")

# Resto do código permanece inalterado

# Função para fazer tentativas de login com as senhas da wordlist
def tentar_logins(base_url, lines):
    if lines is None:
        return

    for item in lines:
        senha = item.strip()
        
        # Personalize estas informações para o site que você deseja testar
        payload = {
            'username_field_name': 'seu_nome_de_usuario',
            'password_field_name': senha,
        }
        
        # Faça a solicitação de login aqui usando a biblioteca 'requests'
        # Você deve usar a base_url, os nomes reais dos campos de nome de usuário e senha, 
        # e também lidar com a resposta para determinar se o login foi bem-sucedido.
        
        # Exemplo fictício de como fazer uma solicitação POST de login:
        response = requests.post(base_url + '/login', data=payload)
        
        # Exemplo fictício de verificação de sucesso com base na resposta:
        if 'Bem-vindo' in response.text:
            print(f'✅ Login bem-sucedido com a senha: {senha}')
        else:
            print(f'❌ Tentativa de login com a senha: {senha} falhou')

# Resto do código permanece inalterado

# Função principal
def main():
    exibir_banner()

    # Opção para escolher a base URL
    base_url = input('Digite a base URL (exemplo: http://exemplo.com/): ')

    lines = selecionar_wordlist()  # Modificado para selecionar ou criar uma wordlist
    if lines is not None:
        tentar_logins(base_url, lines)

    print("🐾 Tentativas de login concluídas! Tenha um ótimo dia! 🐾")

# Resto do código permanece inalterado

# Função para selecionar ou criar uma wordlist
def selecionar_wordlist():
    escolha = input("Deseja selecionar uma wordlist existente (S) ou criar uma nova (N)? ").strip().lower()
    if escolha == "s":
        return ler_wordlist()
    elif escolha == "n":
        criar_wordlist()
        return ler_wordlist()
    else:
        print("Opção inválida. Escolha 'S' para selecionar ou 'N' para criar uma nova wordlist.")
        return selecionar_wordlist()

# Função para ler a wordlist
def ler_wordlist():
    loq = input('Digite o caminho da sua wordlist: ')
    try:
        with open(loq, 'r', encoding='latin-1') as dirs:  # Modifique a codificação para 'latin-1'
            lines = dirs.readlines()
        return lines
    except FileNotFoundError:
        print("Oops! O arquivo não foi encontrado. Certifique-se de fornecer o caminho correto.")
        return None

# Função para verificar as páginas
def verificar_paginas(base_url, lines):
    if lines is None:
        return

    for item in lines:
        senha = item.strip()
        url = base_url + senha
        req = requests.get(url)
        if req.status_code == 200:
            print(f'✅ {senha} - {url} - Status 200')
        else:
            print(f'❌ {senha} - {url} - Status 404')

# Resto do código permanece inalterado

# Função principal
def main():
    exibir_banner()

    # Opção para escolher a base URL
    base_url = input('Digite a base URL (exemplo: http://vetagro.com.br/): ')

    lines = selecionar_wordlist()  # Modificado para selecionar ou criar uma wordlist
    if lines is not None:
        verificar_paginas(base_url, lines)

    print("🐾 Busca concluída! Tenha um ótimo dia! 🐾")

# Executar o programa
if __name__ == "__main__":
    main()
    