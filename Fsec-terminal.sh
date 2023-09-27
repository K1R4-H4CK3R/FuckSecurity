#!/bin/bash
clear

# Função para exibir prompt personalizado
function exibir_prompt {
  local usuario=$(whoami)
  local diretorio_atual=$(basename $(pwd))  # Obtém o nome da pasta atual
  local data_hora=$(date +"%Y-%m-%d %H:%M:%S")
  
  echo -e "\e[1;34m╭────────────────────────────╮\e[0m"
  echo -e "\e[1;34m│\e[0m\e[1;36m   ___  _    _ _   _ _ _ _\e[1;34m   │\e[0m"
  echo -e "\e[1;34m│\e[0m\e[1;36m  / _ \| |  | | | | | | | |\e[1;34m  │\e[0m"
  echo -e "\e[1;34m│\e[0m\e[1;36m | (_) | |  | | |_| | | | |\e[1;34m  │\e[0m"
  echo -e "\e[1;34m│\e[0m\e[1;36m  \__, | |  | |  _  | | | |\e[1;34m  │\e[0m"
  echo -e "\e[1;34m│\e[0m\e[1;36m    / /| |__| | | | | | | |\e[1;34m  │\e[0m"
  echo -e "\e[1;34m│\e[0m\e[1;36m   /_/  \____/|_| |_|_|_|_|\e[1;34m  │\e[0m"
  echo -e "\e[1;34m│\e[0m\e[1;36m                           \e[1;34m  │\e[0m"
  echo -e "\e[1;34m│\e[0m\e[1;32mBem-vindo ao \e[0m\e[1;31mTerminal Fsec\e[1;32m, $usuario!\e[1;34m  │\e[0m"
  echo -e "\e[1;34m│\e[0m\e[1;33mDiretório atual: $diretorio_atual\e[1;34m         │\e[0m"
  echo -e "\e[1;34m│\e[0m\e[1;33mData/Hora: $data_hora\e[1;34m               │\e[0m"
  echo -e "\e[1;34m│\e[0m\e[1;35mDigite 'help' para ver os comandos disponíveis.\e[1;34m │\e[0m"
  echo -e "\e[1;34m╰────────────────────────────╯\e[0m"
}

# Resto do seu script (sem alterações)

# ...


# Função para completar nomes de arquivos/diretórios
function completar {
  local text="${1}"
  local completions=($(compgen -f "${text}"))
  COMPREPLY=("${completions[@]}")
}

# Histórico de Comandos
comandos=()

while true; do
  exibir_prompt

  # Leitura com autocompletar
  read -e -p "FuckSecurity$ " comando
  if [ -n "$comando" ]; then
    # Adicionar comando ao histórico
    comandos+=("$comando")

    case "$comando" in
      "ls")
        diretorio_atual=$(pwd)  # Define o diretório atual corretamente
        ls -a "$diretorio_atual"
        ;;
      "pwd")
        echo "$diretorio_atual"
        ;;
      "cd "*)
        novo_diretorio="${comando#cd }"  # Extrai o argumento do comando "cd"
        if [ -d "$novo_diretorio" ]; then
          cd "$novo_diretorio"
          diretorio_atual="$(pwd)"
        else
          echo "Diretório não encontrado: $novo_diretorio"
        fi
        ;;
      "python "*)
        script_python="${comando#python }"  # Extrai o argumento do comando "python"
        eval "python $script_python"
        ;;
      "bash "*)
        script_bash="${comando#bash }"  # Extrai o argumento do comando "bash"
        eval "bash $script_bash"
        ;;
      "chmod "*)
        permissao_arquivo="${comando#chmod }"  # Extrai o argumento do comando "chmod"
        arquivo_criar="${comando#chmod $permissao_arquivo }"  # Extrai o nome do arquivo
        eval "chmod $permissao_arquivo $arquivo_criar"  # Aplica as permissões ao arquivo
        ;;
      "touch "*)
        arquivo_criar="${comando#touch }"  # Extrai o argumento do comando "touch"
        touch "$arquivo_criar"
        ;;
      "rm "*)
        arquivo_remover="${comando#rm }"  # Extrai o argumento do comando "rm"
        rm -rf "$arquivo_remover"
        ;;
      "mkdir "*)
        diretorio_criar="${comando#mkdir }"  # Extrai o argumento do comando "mkdir"
        mkdir -p "$diretorio_criar"
        ;;
      "date")
        date
        ;;
      "whoami")
        whoami
        ;;
      "cal")
        cal
        ;;
      "cat "*)
        arquivo_mostrar="${comando#cat }"  # Extrai o argumento do comando "cat"
        cat "$arquivo_mostrar"
        ;;
      "ps")
        ps aux
        ;;
      "top")
        top
        ;;
      "df")
        df -h
        ;;
      "du "*)
        diretorio_uso="${comando#du }"  # Extrai o argumento do comando "du"
        du -h "$diretorio_uso"
        ;;
      "netstat")
        netstat -tuln
        ;;
      "ifconfig")
        ifconfig
        ;;
      "git clone "*)
        repositorio_git="${comando#git clone }"  # Extrai o argumento do comando "git clone"
        git clone "$repositorio_git"
        ;;
      "apt-get install "* | "pkg install "*)
        pacote_instalar="${comando#apt-get install }"  # Extrai o argumento do comando "apt-get install" ou "pkg install"
        eval "$comando"
        ;;
      "help")
        echo "Comandos disponíveis:"
        echo "ls - Listar arquivos e diretórios"
        echo "pwd - Mostrar diretório atual"
        echo "cd [diretório] - Mudar de diretório"
        echo "python [script] - Executar um script Python"
        echo "bash [script] - Executar um script Bash"
        echo "chmod [permissões] [arquivo] - Alterar permissões de arquivo"
        echo "touch [arquivo] - Criar um arquivo"
        echo "rm [arquivo/diretório] - Remover um arquivo ou diretório"
        echo "mkdir [diretório] - Criar um diretório"
        echo "date - Mostrar a data atual"
        echo "whoami - Mostrar o nome de usuário atual"
        echo "cal - Mostrar o calendário"
        echo "cat [arquivo] - Exibir o conteúdo de um arquivo"
        echo "ps - Listar processos"
        echo "top - Monitorar os principais processos em execução"
        echo "df - Mostrar uso de espaço em disco"
        echo "du [diretório] - Mostrar uso de espaço em disco de um diretório"
        echo "netstat - Exibir informações de rede"
        echo "ifconfig - Exibir informações de interface de rede"
        echo "git clone [repositório] - Clonar um repositório Git"
        echo "apt-get install [pacote] - Instalar um pacote (Linux Debian/Ubuntu)"
        echo "pkg install [pacote] - Instalar um pacote (Linux Fedora/RHEL)"
        echo "help - Exibir esta mensagem de ajuda"
        echo "exit - Sair do Terminal Dhack"
        echo "history - Exibir o histórico de comandos"
        ;;
      "history")
        for idx in "${!comandos[@]}"; do
          echo "$idx: ${comandos[$idx]}"
        done
        ;;
      "exit")
        echo "Saindo do Terminal Dhack. Até logo!"
        exit 0
        ;;
      "./"*)
        script_executavel="${comando#./}"  # Extrai o argumento do comando "./"
        if [ -x "$script_executavel" ]; then
          "./$script_executavel"
        else
          echo "Script não encontrado ou não é executável: ./$script_executavel"
        fi
        ;;
      *)
        # Se o comando não for reconhecido, executa no shell padrão
        eval "$comando"
        ;;
    esac
  fi
done
