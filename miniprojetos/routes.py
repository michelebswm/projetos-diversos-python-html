from flask import Flask, render_template, url_for, request, flash
from miniprojetos import app
from miniprojetos.forms import FormGeradorSenha, FormGeradorCitacao, FormGeradorCitacaoPensador, FormTradutor
import requests
# from translate import Translator
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
            translator = Translator(to_lang="pt")
            citacao_traduzida = translator.translate(response['quote'])
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