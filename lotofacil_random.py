'''
Tentativa de criação de uma código para a criação de 15 números aleatórios
baseados nas estatisticas de números quentes (hots_numb), máxima ocorrência nos
últimos 20 sorteios (max_occur) e números primos < 25 (primes_numb)

Atribuições do programa:
    1. Listar números quentes ... (hots_numb).
    2. Listar números de mais ocorrências ... (max_occur).
    3. Listar números primos menores que 25 ... (primes_numb).
    3. Comparar listas e separar os números sem repetição ...
    4. Gerar listas com 15 números (lista1, lista2, ...) randômicas

'''

# Importando função random

import random

''' Listas de números gerados manual através do aplicativo mobile Loto LF Mais Fácil (Google Play).
Lista atualizada manualmente através das estatísticas apresentadas pelo App.

hots_numb = Números mais sorteados nos últimos sorteios (Números quentes).
max_occur = Máxima ocorrência de números de acordo com os últimos 20 sorteios.
primes_numb = Lista de números primos menores que 25.

Autor: Daniel Caixeta - 19.abr.2023 (versão atualizada - Inclusão dos números primos < 25)
'''

# Parâmetros de entrada.

hots_numb = [1, 5, 6, 8, 9, 10, 11, 14, 15, 16, 17, 18, 20, 21, 23, 24] 
max_occur = [20, 25, 4, 12, 13, 23, 1, 7, 8, 11, 19, 24, 2, 10, 21, 9, 22, 3, 6, 14, 17]
primes_numb = [2, 3, 5, 7, 11, 13, 17, 19, 23] # Parâmetro de entrada fixo (não varia)...
fibonacci_numb = [1, 2, 3, 5, 8, 13, 21]

# Combinação e ordenação das duas listas (hots_numb + max_occur -> join_list)

#join_list = (sorted(set(hots_numb + max_occur + primes_numb)))
join_list = (hots_numb + max_occur + primes_numb)

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
#random_list4 = random.sample(unique_list, 15)
#random_list5 = random.sample(unique_list, 15)
#random_list6 = random.sample(unique_list, 15)
#random_list7 = random.sample(unique_list, 15)

# Impressão das interações processadas.

print('Resultado da interação para {4} interações:')
print(f'Resultado {1}', sorted(random_list1))
print(f'Resultado {2}', sorted(random_list2))
print(f'Resultado {3}', sorted(random_list3))
#print(f'Resultado {4}', sorted(random_list4))
#print(f'Resultado {5}', sorted(random_list5))
#print(f'Resultado {6}', sorted(random_list6))
#print(f'Resultado {7}', sorted(random_list7))

print('')

# EOF