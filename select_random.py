'''' Código em Python que seleciona itens aleatórios de uma lista usando
o módulo random e o método sample()
Referência: https://diegomariano.com/selecionando-itens-aleatorios-de-uma-lista-com-python/
Modificação/alteração: dfcaixeta - 17.abr.2023
 '''

import random

# Criação da lista ...

lista = [1, 2, 3, 4, 5, 6, 7]

# Selecionando três itens da lista acima.

aleatorio = random.sample(lista, 3)

print('Impressão dos números aleatórios ...')
print('')
print(aleatorio)
print('')

# EOF