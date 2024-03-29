''' Código em Python para exibição de potência de 2 (inteiros) usando uma 
função anônima (lambda).
Autor: https://www.programiz.com/python-programming/examples/power-anonymous

Modificado/alterado: Daniel Caixeta @dfcaixeta em 11.abr.23 '''

# Mostra a potência de 2 usando uma função anônima (lambda) no Python

print('')
print('-' * 23)
print('Potência de dois [...]')
print('-' * 23)
print('')

# Descomente o trecho abaixo para entrar com a variável estática.
# termos = 10 # Variável estática ...

# Ou descomente o código abaixo para receber informações do usuário

termos = int(input("Quantos termos? ")) # Variável global ...

# Usando a função anônima (lâmbda)

resultados = list(map(lambda x: 2 ** x, range(termos)))
print()

print("O total de termos são:", termos)
print()

for i in range(termos):
   print("2 elevado a", i,"=", resultados[i])

print()

# EOF