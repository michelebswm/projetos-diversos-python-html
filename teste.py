import requests

assunto = 'saudade e'
assunto = assunto.replace(' ', '+')
print(assunto)
quantidade = 10

url = f'https://pensador-api.vercel.app/?term={assunto}&max={quantidade}'
response = requests.get(url)

if response.status_code == 200:
    response = response.json()
    texto = []
    if response:
        for item in response['frases']:
            texto.append(item['texto'])
else:
    print("Não foi possível obter as citações do Pensador")

for citacao in texto:
    print(citacao.strip())