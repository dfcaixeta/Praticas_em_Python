''' Estudos sobre function, imports ... em Python:

1. Estrutura para retorno da função.
# 2. Usando o módulo import.

Autor: Daniel Caixeta @dfcaixeta - 09.jun.2023
'''

# 1. Estrutura para retorno da função.
print('Imprime a função foo() como retorno de função: ')
def foo():
    return "retorno da função"
print(foo())

print('=' * 10)
print()

# 2. Usando o módulo import.
import math # Importa todos os módulo math.

print('Calcula a raiz quadrada de um número: ')

valor_str = input('Entre com um número: ') # Entrada do número.

valor_int = int(valor_str) # Casting str to int.

print(f'A raiz quadrada de {valor_int} é igual a:', math.sqrt(valor_int))

print('=' * 10)
print()

... # Estudos import datetime



# EOF