import validate_docbr as valid

def validar_cpf(cpf):
    return valid.CPF().validate(cpf)

def validar_cnpj(cnpj):
    return valid.CNPJ().validate(cnpj)

def validar_pis(pis):
    return valid.PIS().validate(pis)

def validar_cnh(cnh):
    return valid.CNH().validate(cnh)

def validar_TituloEleitoral(titulo):
    return valid.TituloEleitoral().validate(titulo)

def validar_renavam(renavam):
    return valid.RENAVAM().validate(renavam)



cpf = "372.798.df-01"  # Substitua pelo CPF que deseja validar
validacao_result = {}
validacao_result['cpf'] = ('CPF válido!' if validar_cpf(cpf) else 'CPF inválido!')

print(validacao_result)

if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido.")

print(validar_cnpj('99.181.173/0001-10'))
