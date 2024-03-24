''' Algoritmo em python que apresenta um calendário com ano e mês.
É necessário importar a biblioteca (lib) calendar. 

@utor: Daniel Caixeta - @dfcaixeta - 23.mar.2024 '''

# Importando a biblioteca.

import calendar

# Definindo a função mostrar_calendario.

def mostrar_calendario(ano, mes):
    
    # Mostra o calendário do ano e mês especificados.
    cal = calendar.month(ano, mes)
    return cal

# Solicita ao usuário informações para o ano e mês desejados.

ano = int(input("Digite o ano (Por exemplo: 1900): "))
mes = int(input("Digite o mês (1-12): "))

# Chama a função para mostrar o calendário.

calendario = mostrar_calendario(ano, mes)
print(f"\nCalendário do mês {mes} do ano {ano}:\n")
print(calendario)

# EOF
