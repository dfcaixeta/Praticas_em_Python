''' Algoritmo em Python que recebe um número inteiro e imprime seu dígito das dezenas.
Versão 2.

autor: Daniel Caixeta @dfcaixeta em 04.jun.23 '''

print("    ----------------------------------------------------    ")
print("          Algoritmo que imprime o dígito da dezena          ")
print("    ----------------------------------------------------    ")
print()

entraInt = int(input("Digite um número inteiro: "))

print()

resultFinal = (entraInt // 10) % 10

print('O dígito da dezena é', resultFinal)

print()

# EOF