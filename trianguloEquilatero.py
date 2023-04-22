''' Programa em Python que calcula todos os parâmetros de um triângulo equilátero
autor: Daniel Caixeta @dfcaixeta em 22.abr.2023

Para obter os resultados, temos que listar os seguintes parâmetros:
lado = Lado do triângulo equilátero ...
perimetro = Perimetro do triângulo ...
semiperimetro = Semiperimetro do triângulo ...
area = Área do triângulo equilatéro ...
altura = Altura do triângulo ... '''

import math as math 

# vamos ler a altura do triângulo equilátero
altura = float(input("Informe a altura do triângulo: "))

print('')
     
# calcular a medida do lado do triângulo equilátero
lado = (2 / math.sqrt(3)) * altura

# calcular o perímetro do triângulo equilátero
perimetro = 3 * lado

# calcular o semiperímetro do triângulo equilátero
semiperimetro = (3 * lado) / 2

# calcular a área do triângulo equilátero
area = 1/4 * (math.sqrt(3)) * (lado ** 2)

# Resultados dos cálculos ...
print('Os resultados são:')
print('')
print(f'A altura do triângulo é {round(altura, 2)} mts.')
print(f'O lado corresponde a {round(lado, 2)} mts.')
print(f'O perímetro corresponde a {round(perimetro, 2)} mts.')
print(f'O semiperimetro corresponde a {round(semiperimetro, 2)} mts.')
print(f'A área do triângulo é {round(area, 2)} mts quad.')

print('')

# EOF