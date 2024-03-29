''' Algoritmo em Python com estrutura condicional IF, operador lógico AND
e operador de comparação TRUE que pergunta sem tem idade para dirigir.
(Versão 3).

autor: Daniel Caixeta @dfcaixeta em 24.mar.2024 '''

idade = 17

tem_permissao = True

if idade > 16 and tem_permissao == True:
    print('Pode dirigir!', 'Você tem', idade, 'anos de idade!')

else:
    print('Você ainda não tem permissão para dirigir!')

print()

# EOF