aniversario = input("Digite a data de seu aniversário(DDMMAAAA): ")

def somador(aniversario):
    resultado = 0
    for numero in aniversario:
        resultado = resultado + int(numero)
    if (len(str(resultado)) > 1):
        resultado = somador(str(resultado))
    return resultado
    
soma = somador(aniversario)

print(soma)
