import pandas as pd

# Leitura do arquivo Excel
df = pd.read_excel("C:/Users/Public/enviar_mensagem/wpp.xlsx")

# Itera diretamente sobre a coluna "Número"
for index, row in df.iterrows():
    numero = row["numeros"] #nome da coluna com os números
    mensagem = "Oi, [Nome do Técnico], tudo bem? 😊Sou Isaac, do time de Sucesso do Técnico da FindUP. Temos uma oportunidade de atendimento presencial em Cristalina - GO e pensei em te chamar para entender se faz sentido para você.Se quiser saber mais, é só me chamar aqui! Aguardo seu retorno."