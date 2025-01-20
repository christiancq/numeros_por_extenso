unidades_e_especiais = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove","dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
milhares = ["", "mil", "milhão", "bilhão", "trilhão"]

def extenso(numero):
    if numero < 20:
        return unidades_e_especiais[numero]
    if numero < 100:
        dezena = numero // 10
        unidade = numero % 10
        texto = dezenas[dezena]
        if unidade != 0:
            texto += f" e {extenso(unidade)}"
        return texto
    if numero < 1000:
        centena = numero // 100
        resto = numero % 100
        texto = centenas[centena]
        if resto != 0:
            texto += f" e {extenso(resto)}"
        return texto

for i in range(100, 201):
    texto = extenso(i)
    print(texto, i, len(texto))
