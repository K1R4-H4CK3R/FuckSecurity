import os
import pcap
import socket
import struct
from scapy.all import *

GREEN_BANNER = """\033[32;1m
███████╗██╗   ██╗███████╗██╗   ██╗███╗   ██╗███████╗
██╔════╝██║   ██║██╔════╝██║   ██║████╗  ██║██╔════╝
███████╗██║   ██║███████╗██║   ██║██╔██╗ ██║███████╗
╚════██║██║   ██║╚════██║██║   ██║██║╚██╗██║╚════██║
███████║╚██████╔╝███████║╚██████╔╝██║ ╚████║███████║
╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
\033[0m"""

def packet_handler(pktlen, data, timestamp):
    if data:
        pkt = Ether(data)
        print(f"[*] Capturado pacote {pkt.summary()}")

        if IP in pkt:
            ip_src = pkt[IP].src
            ip_dst = pkt[IP].dst
            print(f"  - Origem IP: {ip_src}")
            print(f"  - Destino IP: {ip_dst}")

        if TCP in pkt:
            src_port = pkt[TCP].sport
            dst_port = pkt[TCP].dport
            print(f"  - Porta de Origem: {src_port}")
            print(f"  - Porta de Destino: {dst_port}")

        if pkt.haslayer(HTTP):
            http_request = pkt[HTTP].Request
            if http_request:
                print(f"  - HTTP Request: {http_request.decode('utf-8')}")

        if pkt.haslayer(DNS):
            dns_query = pkt[DNS].qd.qname.decode('utf-8')
            if dns_query:
                print(f"  - DNS Query: {dns_query}")

def capturar_trafego(interface, salvar_pcap=None):
    print(GREEN_BANNER)
    try:
        pc = pcap.pcap(name=interface, promisc=True, immediate=True)
        
        if salvar_pcap:
            dumper = pc.dump_open(salvar_pcap)

        pc.loop(packet_handler)
    except Exception as e:
        print(f"[!] Ocorreu um erro ao capturar tráfego: {str(e)}")

def main():
    interface = input("Digite o nome da interface de rede (por exemplo, eth0): ")
    salvar_pcap = input("Digite o nome do arquivo PCAP para salvar (deixe em branco para não salvar): ")

    if salvar_pcap and not salvar_pcap.endswith(".pcap"):
        salvar_pcap += ".pcap"

    capturar_trafego(interface, salvar_pcap)

if __name__ == "__main__":
    main()
    