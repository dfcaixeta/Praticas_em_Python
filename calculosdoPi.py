''' Calculando o Pi com o Python.
Autor: Daniel Caixeta @dfcaixeta - 04.jun.2023
'''

''' 
Método 1: usando a fórmula de Leibniz
 - Initialize k = 1 -> Esta variável será usada como o denominador da fórmula de leibniz,
                       será incrementada em 2.
 - Initialize sum = 0 -> sum adicionará todos os elementos da série.
 - Execute um loop for de 0 a 1000000 -> Com este valor, obtemos o valor mais preciso de Pi. 
Dentro do loop for, verifique se i % 2 == 0 então faça sum = sum + 4 / k. Caso contrário, faça
sum = sum-4 / k.
 - Incremente k em 2, vá para a etapa 3 '''

k = 1
s = 0

for i in range(1000000):
    if i % 2 == 0:
        s += (4/k)
    else:
        s -= (4/k)
    k += 2

print()
print('O valor de Pi encontrado com o método de Leibniz é:',s)
print()

print('-' * 23)

'''Método 2: usando o módulo matemático
Python tem uma biblioteca chamada math, podemos simplesmente importar matemática
e imprimir o valor de pi.
'''

print()

import math

print('Valor de Pi da biblioteca math em Python: ', math.pi)

print()

# EOF