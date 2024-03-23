''' Em Python, a instrução break oferece a possibilidade de sair de um loop quando uma condição
externa é acionada. A instrução break é colocada dentro de uma condião IF, onde caso 
for verdadeira, o loop se encerra.'''

# Estrutura condicional For ... If ... Break
number = 0
print('OUTPUT with Break ...')

for number in range(5):
    if number == 3:
        break       # Encerra o loop.

    print('Numero: ' + str(number))

print('Fora do loop')
print()
print('*' * 10)
print()


''' A instrução continue dá a opção de ignorar a parte de um loop onde uma condição
externa é acionada, mas continua a completar o resto do loop.'''

# Estrutura condicional For ... If ... Break
number = 0
print('OUTPUT with Continue ...')

for number in range(5):
    if number == 3:
        continue       # Pula o loop.

    print('Numero: ' + str(number))

print('Fora do loop')
print()

# EOF