from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, SelectMultipleField, widgets, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange

class FormGeradorSenha(FlaskForm):
    comprimento_senha = IntegerField('Comprimento da Senha', validators=[DataRequired(), NumberRange(min=1, max=100, message='Mensagem')])
    itens = SelectMultipleField('Itens a serem incluidos', choices=[('hexdigits', 'Hexadecimais'), ('punctuation', 'Pontuação')], widget=widgets.ListWidget(prefix_label=False), option_widget=widgets.CheckboxInput())
    btn_gerar_senha = SubmitField('Gerar Senha')

    def get_selected_items(self):
        return self.itens.data

class FormGeradorCitacao(FlaskForm):
    btn_gerar_citacao = SubmitField('Gerar Citação')


class FormGeradorCitacaoPensador(FlaskForm):
    assunto = StringField('Assunto', validators=[DataRequired()])
    quantidade = IntegerField('Quntidade de citações a serem geradas', validators=[DataRequired(), NumberRange(min=1, max=10, message='Limite a ser gerado')])
    btn_gerar_pensador = SubmitField('Gerar Citação')


class FormTradutor(FlaskForm):
    texto = TextAreaField('Digitar texto', validators=[DataRequired(), Length(1, 5000)])
    btn_traduzir = SubmitField('play_arrow')
    btn_limpar = SubmitField('delete_sweep')


lista_moedas = [
    ("AUD", "Dólar australiano"),
    ("CAD", "Dólar canadense"),
    ("CHF", "Franco suíço"),
    ("DKK", "Coroa dinamarquesa"),
    ("EUR", "Euro"),
    ("GBP", "Libra Esterlina"),
    ("JPY", "Iene"),
    ("NOK", "Coroa norueguesa"),
    ("SEK", "Coroa sueca"),
    ("USD", "Dólar dos Estados Unidos"),
    ("REAL", "Real")
]
class FormConversorMoeda(FlaskForm):
    data_cotacao = DateField('Data da Cotação', validators=[DataRequired()])
    moeda_origem = SelectField('Converter de ', choices=lista_moedas, validators=[DataRequired()])
    moeda_destino = SelectField('Para', choices=lista_moedas, validators=[DataRequired()])
    btn_converter_moeda = SubmitField('paid')
    btn_limpar_consulta = SubmitField('Limpar Histórico')
