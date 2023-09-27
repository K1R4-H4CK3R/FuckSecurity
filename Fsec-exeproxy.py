import os

def activate_proxy(proxy_ip, proxy_port, command):
    # Comando para executar com proxy
    proxy_command = f'proxychains4 -q -f /data/data/com.termux/files/usr/etc/proxychains.conf {command}'

    # Configurar o proxy temporariamente
    os.environ['http_proxy'] = f'socks4://{proxy_ip}:{proxy_port}'
    os.environ['https_proxy'] = f'socks4://{proxy_ip}:{proxy_port}'

    # Executar o comando com proxy
    os.system(proxy_command)

if __name__ == "__main__":
    proxy_ip = "103.151.41.7"
    proxy_port = "80"
    comando_a_executar = "proxy-list.txt"

    activate_proxy(proxy_ip, proxy_port, comando_a_executar)
    
    