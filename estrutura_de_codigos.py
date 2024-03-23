''' Estudos sobre estrutura de códigos em Python:

1. Acessar +infos pelo index.
2. Percorrendo strings (string lopping).
3. Controle de fluxo (condicionais). Exemplos 1 e 2.
4. Laços de repetição com os comandos FOR e WHILE...

Autor: Daniel Caixeta @dfcaixeta - 09.jun.2023
'''

# Acessando a informação pelo index ...
# p y t h o n
# 0 1 2 3 4 5

print()

# 1. Entrar com a string.
string_name = 'Python'
#              012345 -> Posição dos números no indice.

print(f'Imprime a string {string_name} em ordem crescente (->)')
print(string_name[0], string_name[1], string_name[2], string_name[3],
      string_name[4], string_name[5])

print()

print(f'Imprime a string {string_name} em ordem decrescente (<-)')
print(string_name[5], string_name[4], string_name[3], string_name[2],
      string_name[1], string_name[0])

print('=' * 10)
print()

# 2. Percorrendo strings (string lopping).
print('Imprime a variável letter na vertical: ')
for letter in "Python":
    print(letter)

print('=' * 10)
print()

...
# 3. Controle de fluxo (condicionais). Exemplo 1.
print('Imprime o fluxo condicional do Exemplo 1.')
expressao = True

if expressao == True:
    print('true')
else:
    print('false')

print('=' * 10)
print()

# 3. Controle de fluxo (condicionais). Exemplo 2.
print('Imprime o fluxo condicional do Exemplo 2.')
answer = 4

if answer > 5:
    print(1)

elif answer < 5:
    print(-1)

else:
    print(0)

print('=' * 10)
print()

# 4. Laços de repetição com os comandos FOR e WHILE...
print('Imprime uma lista usando o comando "for".')
lista = ["p", "y", "t", "h", "o", "n"]
for item in lista:
    print (item)

print('=' * 10)
print()

print('Imprime uma lista usando o comando "while".')
count = 0

while count <= 5:
    print(count)
    count += 1

print('=' * 10)
print()

# EOF