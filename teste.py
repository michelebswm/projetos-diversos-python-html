import requests
import time
def conversor(moedaOrigem, moedaDestino, quantidade):
    dic_moeda = {
        'USDBRL': None,
        'EURBRL': None,
        'BTCBRL': None
    }

    url = f'http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL'
    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
        for moeda in dic_moeda:
            dic_moeda[moeda] = response[moeda]['bid']
    else:
        print('Moeda não encontrada')

    dic_moeda['REAL'] = 1.0
    print(dic_moeda)

    conversao = (quantidade * float(dic_moeda[moedaOrigem])) / float(dic_moeda[moedaDestino])
    return conversao

# result = conversor(moedaOrigem='EURBRL', moedaDestino='REAL', quantidade=1)
# print(result)

def consulta_cotacao_atual(moeda):
    data_atual = time.strftime('%m-%d-%Y')
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='{moeda}'&@dataCotacao='{data_atual}'&$top=1&$format=json&$select=cotacaoCompra"
    response = requests.get(url)
    response = response.json()
    valor_moeda = response['value'][0]['cotacaoCompra']
    return valor_moeda


