import os
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Caminho para o ChromeDriver
CHROMEDRIVER_PATH = r'C:\Users\diogo.gerardo\Desktop\CODE\NEWS\traffic\chromedriver.exe'

# Configurações do WebDriver (aqui usamos Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executa o navegador em modo headless (sem interface gráfica)
options.add_argument('--disable-gpu')  # Desabilita GPU
options.add_argument('--window-size=800,600')  # Define o tamanho da janela para a captura de tela

# Inicializa o WebDriver do Chrome
driver = webdriver.Chrome(service=ChromeService(CHROMEDRIVER_PATH), options=options)

# Caminho para o repositório
repo_path = r'C:\Users\diogo.gerardo\Desktop\CODE\NEWS\arrow_Icons-1'
image_filename = os.path.join(repo_path, "mapa_com_transito.png")  # Define o caminho da imagem no repositório

try:
    # Muda para o diretório do repositório
    os.chdir(repo_path)

    # Faz o pull do repositório para garantir que está atualizado
    subprocess.run(["git", "pull", "origin", "main"], check=True)

    # URL do arquivo HTML local com o mapa
    html_file = r'file:///C:/Users/diogo.gerardo/Desktop/CODE/NEWS/transito.html'

    # Acessa o arquivo HTML com o mapa e a camada de trânsito
    driver.get(html_file)

    # Espera alguns segundos para o mapa carregar completamente
    time.sleep(5)

    # Tira a captura de tela da div do mapa
    map_element = driver.find_element(By.ID, "map")
    map_element.screenshot(image_filename)  # Salva a captura de tela diretamente no repositório

    print(f"Captura de tela salva como '{image_filename}'")

    # Adiciona a imagem ao git
    subprocess.run(["git", "add", image_filename], check=True)

    # Faz commit com uma mensagem
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    commit_message = f"Adicionar captura de tela do tráfego em {timestamp}"
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Envia as alterações para o repositório remoto
    subprocess.run(["git", "push", "origin", "main"], check=True)

    print("A imagem foi enviada para o repositório com sucesso.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fecha o navegador
    driver.quit()
