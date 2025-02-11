import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

#aqui vamos colocar o caminho para o arquivos excel
#definindo uma variavel para o caminho 
caminho_arquivo = "C:/Users/Isaac/OneDrive/Desktop/enviar_mensagem/wpp.xlsx"

#ler o arquivo excel
df = pd.read_excel(caminho_arquivo)

#aqui é o comando para abrir o navegador na página do whatsapp 
driver = webdriver.Edge()
driver.get("https://web.whatsapp.com/")
input("Escaneie o QR code e pressione Enter para continuar")

for indez, row in df.iterrows():
    numero = row["numeros"] #nome da coluna com os números
    mensagem = "Te amo, amor da minha vida <3"

link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
driver.get(link)
time.sleep(10) #tempo para a página carregar

try:
    send_button = driver.find_element(By.XPATH, '//footer//button[@aria-label="Enviar"]')
    send_button.click()
    time.sleep(3)
    print(f"Mensagem enviada para {numero}")
except Exception as e: 
    print(f"Erro ao enviar para {numero}: {e}")

driver.quit()
print("Automação concluída")
