from flask import Flask, render_template, url_for, request, flash, session, redirect
from miniprojetos import app
from miniprojetos.forms import FormGeradorSenha, FormGeradorCitacao, FormGeradorCitacaoPensador, FormTradutor, FormConversorMoeda, FormConversorUnidades
import requests
import time
from googletrans import Translator
import secrets
import string



@app.route("/")
def home():
    return render_template("home.html")

@app.route('/geradordesenha', methods=['GET', 'POST'])
def gerador_senha():
    form_gerarsenha = FormGeradorSenha()
    senha_gerada = None
    if form_gerarsenha.validate_on_submit() and 'btn_gerar_senha' in request.form:
        tamanho = form_gerarsenha.comprimento_senha.data
        itens_selecionados = form_gerarsenha.get_selected_items()
        itens = ''
        if itens_selecionados:
            if 'hexdigits' in itens_selecionados:
                itens += string.hexdigits
            if 'punctuation' in itens_selecionados:
                itens += string.punctuation
        if itens:
            senha_gerada = ''.join(secrets.choice(itens) for _ in range(tamanho))
        else:
            flash('Nenhuma opção selecionada', 'alert-danger')

    return render_template("geradordesenha.html", form_gerarsenha=form_gerarsenha, senha_gerada=senha_gerada)


@app.route('/geradordecitacao', methods=['GET', 'POST'])
def gerador_citacao():
    form_geradorcitacao = FormGeradorCitacao()
    form_citacaopensador = FormGeradorCitacaoPensador()
    citacao_traduzida = ''
    lista_citacoes = []
    if form_geradorcitacao.validate_on_submit() and 'btn_gerar_citacao' in request.form:
        url = 'https://api.kanye.rest'
        response = requests.get(url)
        if response.status_code == 200:
            response = response.json()
            translator = Translator()
            citacao_traduzida = translator.translate(response['quote'], dest='pt').text
        else:
            citacao_traduzida = 'Não foi possível obter as citações'
    if form_citacaopensador.validate_on_submit() and 'btn_gerar_pensador' in request.form:
        assunto = form_citacaopensador.assunto.data
        assunto = assunto.replace(' ', '+')
        quantidade = form_citacaopensador.quantidade.data
        url = f'https://pensador-api.vercel.app/?term={assunto}&max={quantidade}'
        response = requests.get(url)
        if response.status_code == 200:
            response = response.json()
            if not response['frases']:
                lista_citacoes.append("Não foi possível obter as citações do Pensador com o assunto escolhido")
            else:
                for item in response['frases']:
                    lista_citacoes.append(item['texto'])
        else:
            lista_citacoes.append("Não foi possível obter as citações do Pensador")

    return render_template('geradordecitacao.html', form_geradorcitacao=form_geradorcitacao, form_citacaopensador=form_citacaopensador,  citacao_traduzida=citacao_traduzida, lista_citacoes=lista_citacoes)


@app.route('/tradutordetexto', methods=['GET', 'POST'])
def traduzir_texto():
    texto_final = ''
    form_tradutor = FormTradutor()
    if form_tradutor.validate_on_submit() and 'btn_traduzir' in request.form:
        texto = form_tradutor.texto.data
        translator = Translator()
        traducao = translator.translate(texto, dest='pt')
        texto_final = traducao.text
    if form_tradutor.validate_on_submit() and 'btn_limpar' in request.form:
        form_tradutor.texto.data = ''
        texto_final = ''
    return render_template('tradutordetexto.html', form_tradutor=form_tradutor, texto_final=texto_final)


def consulta_cotacao_atual(moeda, data):
    data_atual = data.strftime('%m-%d-%Y')
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='{moeda}'&@dataCotacao='{data_atual}'&$top=1&$format=json&$select=cotacaoCompra"
    response = requests.get(url)
    valor_moeda = 'Cotação não localizada na API do Banco Central do Brasil (BCB)'
    if response.status_code == 200:
        response = response.json()
        if response['value']:
            valor_moeda = response['value'][0]['cotacaoCompra']

    return valor_moeda

@app.route('/conversordemoedas', methods=['GET', 'POST'])
def converte_moedas():
    form_conversormoeda = FormConversorMoeda()

    # Verifica se já existe um histórico na sessão e cria uma lista vazia caso contrário
    historico = session.get('historico', [])

    if form_conversormoeda.validate_on_submit() and 'btn_converter_moeda' in request.form:
        data_cotacao = form_conversormoeda.data_cotacao.data
        moeda_origem = form_conversormoeda.moeda_origem.data
        moeda_destino = form_conversormoeda.moeda_destino.data
        # usamos a função next() para encontrar o label (descrição) correspondente ao valor selecionado no campo SelectField
        moeda_origem_label = next((label for value, label in form_conversormoeda.moeda_origem.choices if value == moeda_origem), None)
        moeda_destino_label = next((label for value, label in form_conversormoeda.moeda_destino.choices if value == moeda_destino), None)

        if moeda_origem == 'REAL':
            moeda_origem_cotacao = 1.0
        else:
            moeda_origem_cotacao = consulta_cotacao_atual(moeda_origem, data_cotacao)

        if moeda_destino == 'REAL':
            moeda_destino_cotacao = 1.0
        else:
            moeda_destino_cotacao = consulta_cotacao_atual(moeda_destino, data_cotacao)

        try:
            conversao = moeda_origem_cotacao / moeda_destino_cotacao
        except:
            conversao = 'Não definido'

        # Adiciona as informações da consulta atual ao histórico
        consulta_atual = {
            'moeda_origem_label': moeda_origem_label,
            'moeda_origem_cotacao': moeda_origem_cotacao,
            'moeda_destino_label': moeda_destino_label,
            'moeda_destino_cotacao': moeda_destino_cotacao,
            'conversao': conversao
        }
        historico.append(consulta_atual)
        # Atualiza a sessão com o novo histórico
        session['historico'] = historico

    if form_conversormoeda.validate_on_submit() and 'btn_limpar_consulta' in request.form:
        # Remove a chave 'historico' da sessão
        session.pop('historico', None)
        return redirect(url_for('converte_moedas'))

    return render_template('conversordemoedas.html', form_conversormoeda=form_conversormoeda, historico=historico)


def converte_un(quantidade, medida_origem, medida_destino):
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
    siglas = {
        'Angstrom': 'Å',
        'Centimetro': 'cm',
        'Decimetro': 'dm',
        'Metro': 'm',
        'Micrometro': 'µm',
        'Milimetro': 'mm',
        'Nanometro': 'nm',
        'Quilometro': 'km'
    }

    if medida_origem in conversao_dict and medida_destino in conversao_dict[medida_origem]:
        conversao = quantidade * conversao_dict[medida_origem][medida_destino]
        sigla = siglas[medida_destino]
        return conversao, sigla

@app.route('/conversordeunidades', methods=['GET', 'POST'])
def conversor_unidades():
    form_conversorunidades = FormConversorUnidades()
    conversao = None
    sigla = ''
    if form_conversorunidades.validate_on_submit() and 'btn_converter_unidade' in request.form:
        quantidade = form_conversorunidades.quantidade.data
        unidade_origem = form_conversorunidades.unidade_origem.data
        unidade_destino = form_conversorunidades.unidade_destino.data
        conversao, sigla = converte_un(quantidade, unidade_origem, unidade_destino)
    return render_template('conversorunidades.html', form_conversorunidades=form_conversorunidades, conversao=conversao, sigla=sigla)