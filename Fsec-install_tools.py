#!/bin/bash

# Instalação das Ferramentas de Pentesting

# Ferramentas Iniciais
apt update -y
apt upgrade -y
apt install git -y
apt install python -y
apt install python2 -y
apt install python3 -y
apt install nmap -y
apt install metasploit-framework -y
apt install wireshark -y
apt install aircrack-ng -y
apt install john -y
apt install gobuster -y
apt install hydra -y
apt install sqlmap -y

# Ferramentas Adicionais
apt install dirsearch -y
apt install sublist3r -y
apt install gitleaks -y
# Nessus: Baixe do site oficial.
apt install wpscan -y
apt install dirb -y
# Recon-ng: Já instalado, mas pode ser executado com recon-ng.
apt install beef-xss -y
apt install snort -y
# Nikto: Já instalado, mas pode ser executado com nikto.
apt install aquatone -y
apt install wfuzz -y
apt install sn1per -y
apt install brutespray -y
apt install crackmapexec -y
# Subfinder: Já instalado, mas pode ser executado com subfinder.
apt install dnsrecon -y
apt install wafw00f -y
apt install sublist3r -y
# SecLists: Já instalado, mas pode ser acessado na pasta /usr/share/seclists.
apt install bbqsql -y
apt install fruitywifi -y
apt install radare2 -y
apt install jd-gui -y
# Sn1per: Já instalado, mas pode ser executado com sniper.
apt install subfinder -y
apt install yersinia -y
# Nessus: Baixe do site oficial.
apt install cr3d0v3r -y
apt install davtest -y
apt install lynis -y
apt install masscan -y
apt install joomscan -y
apt install shellnoob -y
apt install autorecon -y
apt install striker -y
apt install sniffjoke -y
apt install joomscan -y
apt install ghost-phisher -y
apt install ruler -y
# Recon-ng: Já instalado, mas pode ser executado com recon-ng.
apt install owasp-zsc -y
apt install wpscan -y
apt install xsser -y
apt install set -y
apt install w3af -y
# ZAP (OWASP Zed Attack Proxy): Já instalado, mas pode ser executado com zaproxy.
apt install raccoon -y
# Armitage: Já instalado, mas pode ser executado com armitage.
apt install metagoofil -y
apt install whatweb -y
# Hydra: Já instalado, mas pode ser executado com hydra.
# Hashcat: Já instalado, mas pode ser executado com hashcat.

echo "Instalação concluída!"
