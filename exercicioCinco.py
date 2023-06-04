''' Algoritmo em Python que recebe um número inteiro e imprime seu
dígito das dezenas.

autor: Daniel Caixeta @dfcaixeta em 04.jun.23 '''

print("    ----------------------------------------------------    ")
print("          Algoritmo que imprime o dígito da dezena          ")
print("    ----------------------------------------------------    ")
print()

entraInt = int(input("Digite um número inteiro: "))

print()

resultUm = (entraInt // 10)
resultFinal = resultUm % 10

print('O dígito da dezena é', resultFinal)

print()

# EOF
