import secrets
import string

# Gerar senhas com caracteres hexadecimais e caracteres especiais de pontuação
itens = (string.hexdigits)
senha = [secrets.choice(itens) for i in range(32)]
senha = ''.join(senha)  # Tira a separação '', da lista
print(senha)