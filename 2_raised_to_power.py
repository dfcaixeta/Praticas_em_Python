''' Código em Python para exibição de potência de 2 (inteiros) usando uma 
função anônima.
Autor: https://www.programiz.com/python-programming/examples/power-anonymous
Modificado/alterado: Daniel Caixeta @dfcaixeta em 11.abr.23 '''

# Mostra a potência de 2 usando uma função anônima (lambda) no Python

print('')
print('-' * 20)
print('Raised to power')
print('-' * 20)
print('')

# Descomente o trecho abaixo para entrar com a variável estática.

# terms = 10 # Variável estática ...

# Ou descomente o código abaixo para receber informações do usuário

terms = int(input("How many terms? ")) # Variável global ...

# Usando a função anônima (lâmbda)

results = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:", terms)
for i in range(terms):
   print(" 2 raised to power", i,"is ", results[i])

print('')

# EOF