import socket
import nmap

def banner():
    print("\033[91m██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗")
    print("██║  ██║██╔══██╗████╗  ██║██╔═══██╗████╗  ██║")
    print("███████║███████║██╔██╗ ██║██║   ██║██╔██╗ ██║")
    print("██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║")
    print("██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║")
    print("╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝\033[0m")

def get_ip(site):
    try:
        ip = socket.gethostbyname(site)
        return ip
    except Exception as e:
        print(f"[!] Ocorreu um erro ao verificar o IP: {str(e)}")
        return None

def scan_ports(site):
    try:
        nm = nmap.PortScanner()
        nm.scan(site)

        open_ports = []
        for host in nm.all_hosts():
            for port, info in nm[host]['tcp'].items():
                open_ports.append(f"Porta {port}: {info['name']} ({info['state']})")

        return open_ports
    except Exception as e:
        print(f"[!] Ocorreu um erro ao verificar as portas: {str(e)}")
        return []

def scan_vulnerabilities(site):
    try:
        nm = nmap.PortScanner()
        nm.scan(site)

        vulnerabilities = []
        for host in nm.all_hosts():
            for port, info in nm[host]['tcp'].items():
                if 'cpe' in info:
                    vulnerabilities.append(f"{info['cpe']} ({info['name']})")

        return vulnerabilities
    except Exception as e:
        print(f"[!] Ocorreu um erro ao verificar vulnerabilidades: {str(e)}")
        return []

def main():
    banner()
    site = input("Digite o site alvo: ")

    ip = get_ip(site)
    if ip:
        print(f"[*] IP do site {site}: {ip}")

    open_ports = scan_ports(site)
    if open_ports:
        print(f"[*] Portas abertas para {site}:")
        for port_info in open_ports:
            print(f"  - {port_info}")

    vulnerabilities = scan_vulnerabilities(site)
    if vulnerabilities:
        print(f"[*] Vulnerabilidades detectadas em {site}:")
        for vuln_info in vulnerabilities:
            print(f"  - {vuln_info}")

if __name__ == "__main__":
    main()