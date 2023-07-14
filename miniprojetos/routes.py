from flask import Flask, render_template, url_for, request, flash
from miniprojetos import app
from miniprojetos.forms import FormGeradorSenha
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
