"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> from secao_01_estrutura_sequencial import ex_04_notas_bimestrais
    >>> numeros =['7', '8','9','10']
    >>> ex_04_notas_bimestrais.input = lambda k: numeros.pop()
    >>> ex_04_notas_bimestrais.calcular_media()
    A média anual é 8.5

"""


def calcular_media():
    """Escreva aqui em baixo a sua solução"""
notas_01 = int(input("Nota bimestral 01:   ")) 
notas_02 = int(input("Nota bimestral 01:   ")) 
notas_03 = int(input("Nota bimestral 01:   ")) 
notas_04 = int(input("Nota bimestral 01:   ")) 
media = ((notas_01 + notas_02 + notas_03 + notas_04) / 4)
print(f."Suas notas bimestrais são: {notas_01}, {notas_02}, {notas_03} e {notas_04}" e "E sua media anual é: {media}")
