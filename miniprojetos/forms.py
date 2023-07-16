from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, SelectMultipleField, widgets
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
