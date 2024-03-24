''' Algoritmo em Python com estrutura condicional IF e operador lógico AND que pergunta
sem tem idade para dirigir. (Versão 2).

autor: Daniel Caixeta @dfcaixeta em 23.mar.2024 '''

idade = 17

tem_permissao = True

if idade > 16 and tem_permissao:
    print('Pode dirigir!', 'Você têm', idade, 'anos de idade!')

else:
    print('Você não tem permissão para dirigir!')

print()

# EOF