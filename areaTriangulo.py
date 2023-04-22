''' Programa em Python para calcular a área de um triângulo

autor: Daniel Caixeta @dfcaixeta em 21.abr.2023

Para calcular a área de um triângulo precisamos das seguintes informações:

area = Pârametro área ..
base = Base do triângulo ...
h = Altura do triângulo ...
Fórmula --> area = (b * h) / 2
'''

# Header to code piece
print('')
print('-' * 36)
print(' Cálculando da área de um triângulo' )
print('-' * 36)
print('')

# Parâmetros de entrada para o cálculo da área do triângulo
b = float(input('Entre com a base [mts]: '))
h = float(input('Entre com a altura [mts]: '))

# Fórmula para a área do triângulo

area = (b * h) / 2

# Resultado do cálculo ...
print('')
print(f'A área do triângulo é: {round(area, 2)} mts quad.')
print('')

# EOF