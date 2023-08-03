

# Conversor - Comprimento
def converte_un(quantidade, medida_origem, medida_destino, casas_decimais):
    conversao_dict = {
        'Angstrom': {'Angstrom': 1, 'Centimetro': 1e-8, 'Decimetro': 1e-9, 'Metro': 1e-10, 'Micrometro': 0.1, 'Milimetro': 1e-7, 'Nanometro': 1e-11, 'Quilometro': 1e-13, 'sigla': 'Å'},
        'Centimetro': {'Angstrom': 100000000, 'Centimetro': 1, 'Decimetro': 0.1, 'Metro': 0.01, 'Micrometro': 10000, 'Milimetro': 10, 'Nanometro': 10000000, 'Quilometro': 0.00001, 'sigla': 'cm'},
        'Decimetro': {'Angstrom': 1000000000, 'Centimetro': 10, 'Decimetro': 1, 'Metro': 0.1, 'Micrometro': 100000, 'Milimetro': 100, 'Nanometro': 100000000, 'Quilometro': 0.0001, 'sigla': 'dm'},
        'Metro': {'Angstrom': 10000000000, 'Centimetro': 100, 'Decimetro': 10, 'Metro': 1, 'Micrometro': 1000000, 'Milimetro': 1000, 'Nanometro': 1000000000, 'Quilometro': 0.001, 'sigla': 'm'},
        'Micrometro': {'Angstrom': 10000000, 'Centimetro': 0.0001, 'Decimetro': 0.00001, 'Metro': 0.000001, 'Micrometro': 1, 'Milimetro': 0.001, 'Nanometro': 1000, 'Quilometro': 1e-9, 'sigla': 'µm'},
        'Milimetro': {'Angstrom': 10000000000, 'Centimetro': 0.1, 'Decimetro': 0.01, 'Metro': 0.001, 'Micrometro': 1000, 'Milimetro': 1, 'Nanometro': 1000000, 'Quilometro': 1e-6, 'sigla': 'mm'},
        'Nanometro': {'Angstrom': 1000000000, 'Centimetro': 1e-7, 'Decimetro': 1e-8, 'Metro': 1e-9, 'Micrometro': 0.001, 'Milimetro': 1e-6, 'Nanometro': 1, 'Quilometro': 1e-12, 'sigla': 'nm'},
        'Quilometro': {'Angstrom': 10000000000000, 'Centimetro': 100000, 'Decimetro': 10000, 'Metro': 1000, 'Micrometro': 1000000000, 'Milimetro': 1000000, 'Nanometro': 1000000000000, 'Quilometro': 1, 'sigla': 'km'}
    }

    if medida_origem in conversao_dict and medida_destino in conversao_dict[medida_origem]:
        conversao = quantidade * conversao_dict[medida_origem][medida_destino]
        conversao = '{:,.{casas}f}'.format(conversao, casas = casas_decimais).replace('.','|').replace(',','.').replace('|', ',')
        sigla = conversao_dict[medida_origem]['sigla']
        return conversao, sigla

medida_origem = 'Milimetro'
medida_destino = 'Nanometro'
quantidade = 623
casas_decimais = 5

conversao, sigla = converte_un(quantidade, medida_origem, medida_destino, casas_decimais)
print(conversao, sigla)