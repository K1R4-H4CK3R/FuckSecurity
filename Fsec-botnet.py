import os
import time

def exibir_banner():
    banner = """
\033[91m
███████╗██╗  ██╗ █████╗ ██╗   ██╗███████╗
██╔════╝██║  ██║██╔══██╗██║   ██║██╔════╝
███████╗███████║███████║██║   ██║█████╗  
╚════██║██╔══██║██╔══██║╚██╗ ██╔╝██╔══╝  
███████║██║  ██║██║  ██║ ╚████╔╝ ███████╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝
                                            
Criado por: Kira
Tipo de Ataque: Botnet
\033[0m
"""
    print(banner)

def executar_arquivo(arquivo, vezes):
    print(f"\nExecutando o arquivo '{arquivo}' {vezes} vezes:")
    for i in range(vezes):
        os.system(arquivo)
        print(f"Execução {i + 1} de {vezes}")
        time.sleep(1)  # Aguarda 1 segundo entre as execuções

def listar_arquivos(diretorio):
    print(f"\nArquivos no diretório '{diretorio}':")
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            print(os.path.join(root, file))

def criar_arquivo(nome, conteudo):
    with open(nome, 'w') as arquivo:
        arquivo.write(conteudo)
    print(f"Arquivo '{nome}' criado com sucesso!")

def main():
    exibir_banner()
    arquivo = input("Digite o caminho do arquivo que deseja executar: ")
    vezes = int(input("Digite quantas vezes deseja executar o arquivo: "))

    if os.path.isfile(arquivo):
        continuar = input(f"Tem certeza que deseja executar '{arquivo}' {vezes} vezes? (Y/N): ").strip().lower()
        if continuar == 'y':
            executar_arquivo(arquivo, vezes)
        elif continuar == 'n':
            print("Operação cancelada.")
        else:
            print("Opção inválida. Por favor, digite 'Y' para continuar ou 'N' para cancelar.")
    else:
        print(f"O arquivo '{arquivo}' não existe.")

if __name__ == "__main__":
    main()
    