'''
Tentativa de criação de uma código para a criação de 15 números aleatórios
baseados nas estatisticas de números quentes (hots_numb) e máxima ocorrência nos
últimos 20 sorteios (max_occur).

Atribuições do programa:
    1. Listar números quentes ... (hots_numb)
    2. Lista números de mais ocorrências ... (max_occur)
    3. Comparar listas e separar os números sem repetição ...
    4. Gerar listas com 15 números (lista1, lista2, ...) randômicas

'''

# Importando função random

import random

''' Listas de números gerados manual através do aplicativo mobile Loto LF Mais Fácil (Google Play).
Lista atualizada manualmente através das estatísticas apresentadas pelo App.

hots_numb = Números mais sorteados nos últimos sorteios (Números quentes).
max_occur = Máxima ocorrência de números de acordo com os últimos 20 sorteios.

Autor: Daniel Caixeta - 17.abr.2023 (v.1)
'''

# Parâmetros de entrada.

hots_numb = [3, 4, 7, 8, 9, 10, 11, 12, 14, 15, 18, 19, 20, 21, 23, 25] 
max_occur = [20, 25, 4, 12, 13, 23, 1, 7, 8, 11, 19, 24, 2, 10, 21, 9, 22, 3, 6, 14, 17]

# Combinação e ordenação das duas listas (hots_numb + max_occur -> join_list)

#join_list = (sorted(set(hots_numb + max_occur)))
join_list = (hots_numb + max_occur)

# Organização das lista unida (join_list) e colocar em ordem ...
unique_list = sorted(map(lambda x: x[1], filter(lambda x: x[1] not in
                join_list[:x[0]], enumerate(join_list))))

# Impressão da lista única

print('')
print('Lista completa e ordenada com', len(unique_list), 'números')
print(unique_list)

print('')

# Criando listas randômicas com a lista criada ...

random.shuffle(unique_list)

# print("Resultado: ", sorted(unique_list[0:15])) # Outro método para gerar uma lista ...

# Criando 3 interações possíveis com os números processados ...

random_list1 = random.sample(unique_list, 15)
random_list2 = random.sample(unique_list, 15)
random_list3 = random.sample(unique_list, 15)

# Impressão das interações processadas.

print('Resultado da interação para {3} interações:')
print(f'Resultado {1}', sorted(random_list1))
print(f'Resultado {2}', sorted(random_list2))
print(f'Resultado {3}', sorted(random_list3))

# EOF






print('')


