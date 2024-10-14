from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

# Caminho para o ChromeDriver
CHROMEDRIVER_PATH = r'C:\Users\diogo.gerardo\Desktop\CODE\NEWS\traffic\chromedriver.exe'

# Configurações do WebDriver (aqui usamos Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executa o navegador em modo headless (sem interface gráfica)
options.add_argument('--disable-gpu')  # Desabilita GPU
options.add_argument('--window-size=800,600')  # Define o tamanho da janela para a captura de tela

# Inicializa o WebDriver do Chrome
driver = webdriver.Chrome(service=ChromeService(CHROMEDRIVER_PATH), options=options)

try:
    # URL do teu arquivo HTML local com o mapa
    html_file = r'file:///C:/Users/diogo.gerardo/Desktop/CODE/NEWS/transito.html'

    # Acessa o arquivo HTML com o mapa e a camada de trânsito
    driver.get(html_file)

    # Espera alguns segundos para o mapa carregar completamente
    time.sleep(5)

    # Tira a captura de tela da div do mapa
    map_element = driver.find_element(By.ID, "map")
    map_element.screenshot("mapa_com_transito.png")  # Salva a captura de tela

    print("Captura de tela salva como 'mapa_com_transito.png'")

finally:
    # Fecha o navegador
    driver.quit()
