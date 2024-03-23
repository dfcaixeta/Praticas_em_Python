'''
Algoritmo em Python que calcula a exponenciação de um número base (b) e potência (p)
 usando a função def e pow (função para exponenciação ou potenciação).
E.g., def nome_funcao(args).
E.g., pow(2, 2) = 2 ** 2.

Autor: Daniel Caixeta @dfcaixeta 27.set.2023 '''

print()

# Definindo a função ...
def exp(b, p):
    # retorna a soma de dois números
    return pow(b, p)

# Testar a função com alguns exemplos
print('Os resultados são: ')
print('A potência de (2 ** 2) =', pow(2, 2)) # Deve retornar 4.
print('A potência de (3 ** 3) =', pow(3, 3)) # Deve retornar 27.
print('A potência de (5 ** 2) =', pow(5, 2)) # Deve retornar 25.
print('A potência de (2 ** 10) =', pow(2, 10)) # Deve retornar 1024.

print()

print('Teste da função realizada com sucesso!')

print()

# EOF