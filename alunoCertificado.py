''' Algoritmo em Python que informa se o(a) aluno(a) conquistou a certificação.
Aqui usamos a estrutura condicional IF ... ELSE e o operador lógico OR.
(versão português do código average_grade.py)

Autor: Daniel Caixeta @dfcaixeta 22.mar.2024 '''

# Entrada de dados com variáveis dinâmicas.

print('-' * 20)
print('CERTIFICAÇÃO - FORMAÇÃO EM PYTHON')
print('Critérios para a aprovação ')
print('Nota = A ou Pontuação final >= 7')
print('-' * 20)

print()

nome_aluno = input('Digite o nome: ')
mencao = input("Mençao recebida: ")
pontuacao_final = input("Pontuação final igual a: ")
pont_final_float = float(pontuacao_final) # Castin str para int.

print()

# Estrutura condicional & Lógica operacional.

if mencao == 'A' or pont_final_float >= 7.0:
    print(f'O(a) aluno(a) {nome_aluno} alcançou a Certificação! Nota = {mencao}-{pont_final_float}')

else:
    print(f'Desculpe! {nome_aluno}. Não foi dessa vez. Tente em outra oportunidade!')

print()

# EOF