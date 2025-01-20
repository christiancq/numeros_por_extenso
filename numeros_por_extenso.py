from math import ceil

unidades_e_especiais = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove","dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
milhares = ["", "mil", "milhão", "bilhão", "trilhão"]

def extenso999(numero):
    if numero < 20:
        return unidades_e_especiais[numero]
    if numero < 100:
        dezena = numero // 10
        unidade = numero % 10
        texto = dezenas[dezena]
        if unidade != 0:
            texto += f" e {extenso999(unidade)}"
        return texto
    if numero < 1000:
        centena = numero // 100
        resto = numero % 100
        if centena == 1 and resto == 0:
            return "cem"
        texto = centenas[centena]
        if resto != 0:
            texto += f" e {extenso999(resto)}"
        return texto

def quebar_numero(numero):
    str_numero = str(numero)
    tamanho_numero = len(str_numero)
    quantidade_partes = ceil(tamanho_numero / 3)
    posicao_inicial = 0
    posicao_final = tamanho_numero % 3 if tamanho_numero % 3 != 0 else 3
    partes_numero = []
    for _ in range(quantidade_partes):
        partes_numero.append(int(str_numero[posicao_inicial:posicao_final]))
        posicao_inicial = posicao_final
        posicao_final += 3
    return partes_numero

def extenso(numero):
    texto = ""
    for parte in quebar_numero(numero):
        texto += extenso999(parte)
    return texto

for i in range(1000, 1002):
    texto = extenso(i)
    print(texto, i, len(texto))
