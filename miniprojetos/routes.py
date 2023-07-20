from flask import Flask, render_template, url_for, request, flash
from miniprojetos import app
from miniprojetos.forms import FormGeradorSenha, FormGeradorCitacao, FormGeradorCitacaoPensador, FormTradutor, FormConversorMoeda
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


def consulta_cotacao_atual(moeda):
    data_atual = time.strftime('%m-%d-%Y')
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='{moeda}'&@dataCotacao='{data_atual}'&$top=1&$format=json&$select=cotacaoCompra"
    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
        valor_moeda = response['value'][0]['cotacaoCompra']
    else:
        valor_moeda = 'Cotação não localizada na API do Banco Central do Brasil (BCB)'
    return valor_moeda

@app.route('/conversordemoedas', methods=['GET', 'POST'])
def converte_moedas():
    form_conversormoeda = FormConversorMoeda()
    moeda_origem = ''
    moeda_destino = ''
    conversao = ''
    if form_conversormoeda.validate_on_submit():
        if form_conversormoeda.moeda_origem.data != 'REAL':
            moeda_origem = consulta_cotacao_atual(form_conversormoeda.moeda_origem.data)
        else:
            moeda_origem = 1.0
        if form_conversormoeda.moeda_destino.data != 'REAL':
            moeda_destino = consulta_cotacao_atual(form_conversormoeda.moeda_destino.data)
        else:
            moeda_destino = 1.0
        try:
            conversao = moeda_origem / moeda_destino
        except:
            conversao = 'Não definido'
    return render_template('conversordemoedas.html', form_conversormoeda=form_conversormoeda, moeda_origem=moeda_origem, moeda_destino=moeda_destino, conversao=conversao)