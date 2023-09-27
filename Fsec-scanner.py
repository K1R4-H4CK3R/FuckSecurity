import socket
import threading
import time

# Função para imprimir um banner colorido e animado
def imprimir_banner():
    banner = r"""
     ____ _            _      _   
    / ___| | ___   ___| | ___| |_ 
   | |   | |/ _ \ / __| |/ _ \ __|
   | |___| | (_) | (__| |  __/ |_ 
    \____|_|\___/ \___|_|\___|\__|
    
    Fscanner Port Scanner - by Kira
    """

    # Códigos ANSI para cores e animação
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    reset = "\033[0m"
    
    for char in banner:
        if char.isalpha():
            print(red + char, end="", flush=True)
            time.sleep(0.02)
            print(green + char, end="", flush=True)
            time.sleep(0.02)
            print(yellow + char, end="", flush=True)
            time.sleep(0.02)
        else:
            print(char, end="", flush=True)
            time.sleep(0.02)
    
    print(reset)

# Função para verificar se uma porta está aberta
def verifica_porta(ip, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((ip, porta))
    sock.close()
    return resultado == 0

# Função para realizar a varredura de portas em paralelo
def varredura_portas(ip, portas):
    open_ports = []
    for porta in portas:
        if verifica_porta(ip, porta):
            open_ports.append(porta)
    return open_ports

# Função para dividir a lista de portas em partes para varredura paralela
def divide_portas(portas, num_threads):
    return [portas[i::num_threads] for i in range(num_threads)]

# Função para realizar a varredura de portas com várias threads
def varredura_paralela(ip, portas, num_threads):
    open_ports = []
    portas_divididas = divide_portas(portas, num_threads)

    def varredura_thread(portas):
        for porta in portas:
            if verifica_porta(ip, porta):
                open_ports.append(porta)

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=varredura_thread, args=(portas_divididas[i],))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return open_ports

if __name__ == "__main__":
    imprimir_banner()
    ip_alvo = input("Digite o IP ou domínio alvo: ")
    porta_inicial = int(input("Digite a porta inicial do intervalo: "))
    porta_final = int(input("Digite a porta final do intervalo: "))
    num_threads = int(input("Digite o número de threads para varredura paralela: "))

    portas = list(range(porta_inicial, porta_final + 1))

    open_ports = varredura_paralela(ip_alvo, portas, num_threads)

    if open_ports:
        print("Portas abertas:")
        for porta in open_ports:
            print(porta)
    else:
        print("Nenhuma porta aberta encontrada no intervalo.")
        