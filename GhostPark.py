import os
import sys
import subprocess
from colorama import init, Fore, Style

# Inicializa o colorama
init(autoreset=True)

def run_command(command):
    """Executa um comando do shell."""
    process = subprocess.run(command, shell=True, check=True)
    return process.returncode

def print_panel():
    """Imprime o painel com o nome 'Ghost-Park'."""
    print(Fore.GREEN + """
  ____             _           _____           
 / ___| ___  ___ | | ___ ___ | ____| ___ _ __ 
| |  _ / _ \/ _ \| |/ _ / _ \|  _| / _ \ '__|
| |_| |  __/ (_) | |  __/  __/| |__|  __/ |   
 \____|\___|\___/|_|\___|\___||_____\___|_|   
                                              
    """)
    print(Fore.RED + "[-] YouTube: SeuCanal")
    print(Fore.RED + "[-] GitHub: seuusuario")
    print(Fore.GREEN + "[01] Option 1")
    print(Fore.GREEN + "[02] Exit")
    print(Style.RESET_ALL + "[::] Choose an option: ", end='')

def main():
    # Atualizar e fazer upgrade dos pacotes
    run_command("apt update -y && apt upgrade -y")

    # Instalar git e python-pip
    run_command("pkg install git python-pip -y")

    # Clonar o repositório
    run_command("git clone https://github.com/GhostPark-Men/GhostPark-Men.git")

    # Acessar o diretório do repositório
    os.chdir("GhostPark-Men")

    # Instalar as dependências necessárias
    run_command("pip install -r requirements.txt")

    # Exibir o painel
    print_panel()

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        sys.exit(1)
