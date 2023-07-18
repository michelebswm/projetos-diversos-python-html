# from translate import Translator
from googletrans import Translator

texto = '''July 16 (Reuters) - An already rain-soaked New England braced for more downpours, with four people dead from flooding, and the National Weather Service warned of extreme heat for nearly a quarter of the U.S. population.

The NWS said parts of New England and the Mid-Atlantic areas will get hit with storms "capable of producing torrential rainfall" ahead of a cold front approaching from the west. The areas under risk include major cities like New York, Boston and Philadelphia.

"Given some parts of the Northeast contain saturated and sensitive soils from recent heavy rainfall over the past 10 days, this is a setup primed to produce flash flooding that could be significant in affected areas," the NWS said in a Sunday morning forecast.

New York Governor Kathy Hochul on Sunday urged residents in her state to avoid travel until the rain passes, saying that "your car can go from a place of safety to a place of death" if swept up in a flash flood.

The NWS said the northeast could experience impassable roadways, tornadoes and even mudslides in some areas of higher terrain.

At least four people were swept away and killed by a flash flood on Saturday in Upper Makefield Township in Pennsylvania, about 20 miles northeast of Philadelphia, local police said in a written statement. Rescuers said Sunday they are searching for another three people, including a nine-month old boy, his two-year-old sister and also a adult woman.

Flooding inundated the northeast in recent days, with Vermont in particular reporting catastrophic flooding in its capital Montpelier, which is under a flash flood warning again on Sunday.

Outside of the northeast, the NWS forecast heavy rains for some stretches of the central plains and the middle Mississippi Valley, along with eastern Texas, some portions of Arkansas and Louisiana and parts of the Gulf Coast.'''


def dividir_texto(texto, tamanho_max=500):
    palavras = texto.split()
    partes = []
    parte_atual = ''

    for palavra in palavras:
        if len(parte_atual) + len(palavra) + 1 <= tamanho_max:
            parte_atual += palavra + ' '
        else:
            partes.append(parte_atual.strip())
            parte_atual = palavra + ' '

    if parte_atual:
        partes.append(parte_atual.strip())

    return partes


from googletrans import Translator
translator = Translator()
traducao = translator.translate(texto, dest='pt')

print(traducao.text)

# divisao = dividir_texto(texto)
# print(divisao)
# print(len(divisao))
# list_texto_traduzido = []
# for i in divisao:
#     print(len(i))
#     translator = Translator(to_lang="pt")
#     texto_traduzido = translator.translate(i)
#     list_texto_traduzido.append(texto_traduzido)
#
# print(list_texto_traduzido)
#
# print(' '.join(list_texto_traduzido))