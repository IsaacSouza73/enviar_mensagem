import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#aqui vamos colocar o caminho para o arquivos excel
#definindo uma variavel para o caminho 
caminho_arquivo = "C:/Users/Public/enviar_mensagem/wpp.xlsx"

#ler o arquivo excel
df = pd.read_excel(caminho_arquivo)

#aqui é o comando para abrir o navegador na página do whatsapp 
driver = webdriver.Edge()
driver.get("https://web.whatsapp.com/")
input("Escaneie o QR code e pressione Enter para continuar")

for index, row in df.iterrows():
    numero = str(row["numeros"]) #nome da coluna com os números
    mensagem = "Oi, [Nome do Técnico], tudo bem? 😊Sou Isaac, do time de Sucesso do Técnico da FindUP. Temos uma oportunidade de atendimento presencial em Cristalina - GO e pensei em te chamar para entender se faz sentido para você.Se quiser saber mais, é só me chamar aqui! Aguardo seu retorno."

    if pd.isna(numero) or numero.strip() == "":
        continue

    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    driver.get(link)

    try:
        send_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'footer button[aria-label="Enviar"]'))
        )

        send_button.click()
        
        print(f"Mensagem enviada para {numero}")
        time.sleep(5)
    except Exception as e: 
        print(f"Erro ao enviar para {numero}: {e}")

driver.quit()
print("Automação concluída")
