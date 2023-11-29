import subprocess
import os

def install_jadx():
    # Verifica se o JADX já está instalado.
    try:
        subprocess.run(["jadx", "--version"], check=True)
        print("O JADX já está instalado.")
    except subprocess.CalledProcessError:
        # Instala o JADX usando o gerenciador de pacotes apt (ou ajuste para o seu sistema).
        try:
            print("Instalando o JADX...")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "jadx"], check=True)
            print("O JADX foi instalado com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao instalar o JADX: {e}")
            exit(1)

def decompile_apk(apk_path):
    # Verifica se o caminho contém uma barra, indicando um caminho completo.
    if "/" in apk_path:
        apk_name = os.path.basename(apk_path).split(".")[0]
    else:
        # Se não contiver barra, procurar localmente pelo APK com base no nome.
        for file in os.listdir("."):
            if file.startswith(apk_path.split(".")[0]):
                apk_name = file.split(".")[0]
                apk_path = os.path.join(os.getcwd(), file)
                break
        else:
            print(f"APK '{apk_path}' não encontrado localmente.")
            exit(1)

    # Decompilar o APK usando o JADX.
    output_path = os.path.join(os.getcwd(), f"{apk_name}_output")
    subprocess.run(["jadx", "-d", output_path, apk_path])
    print(f"APK decompilado com sucesso em '{output_path}'.")

if __name__ == "__main__":
    # Instala o JADX no início do script.
    install_jadx()

    # Restante do script para decompilar o APK.
    apk_input = input("Digite o caminho ou nome do APK (com caractere-coringa * se necessário): ")
    decompile_apk(apk_input)
