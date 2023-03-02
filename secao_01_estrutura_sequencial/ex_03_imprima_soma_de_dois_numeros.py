"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça dois números inteiros e imprima a soma.

    >>> from secao_01_estrutura_sequencial import ex_03_imprima_soma_de_dois_numeros
    >>> numeros =['42', '43']
    >>> ex_03_imprima_soma_de_dois_numeros.input = lambda k: numeros.pop()
    >>> ex_03_imprima_soma_de_dois_numeros.imprima_a_soma_de_dois_numeros()
    A soma dos dois números informados é 85

"""

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
soma = numero_1 + numero_2
print(f'A soma dos numeros é {soma}')

"""
Digite o primeiro numero: 42
Digite o segundo numero: 43
A soma dos numeros é 85
"""
