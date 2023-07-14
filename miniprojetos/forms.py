from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange

class FormGeradorSenha(FlaskForm):
    comprimento_senha = IntegerField('Comprimento da Senha', validators=[DataRequired(), NumberRange(min=1, max=100, message='Mensagem')])
    itens = SelectMultipleField('Itens a serem incluidos', choices=[('hexdigits', 'Hexadecimais'), ('punctuation', 'Pontuação')], widget=widgets.ListWidget(prefix_label=False), option_widget=widgets.CheckboxInput())
    btn_gerar_senha = SubmitField('Gerar Senha')

    def get_selected_items(self):
        return self.itens.data