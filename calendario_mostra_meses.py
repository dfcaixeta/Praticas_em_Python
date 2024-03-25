''' Algoritmo em python que apresenta um calendário dos meses com os anos.
É necessário importar a biblioteca (lib) calendar. 

@utor: Daniel Caixeta - @dfcaixeta - 24.mar.2024 '''

# Importando a biblioteca.

import calendar

# Definindo a função mostrar_calendario.

def mostrar_meses(ano):

    # Mostra os meses do ano especificado
    for mes in range(1, 13):

        # Obtém o calendário do mês
        cal = calendar.month(ano, mes)
        print(f"Calendário do mês {mes} do ano {ano}:\n")
        print(cal)

# Solicita entrada do usuário para o ano desejado   
ano = int(input("Digite o ano (ex: 2023): "))

# Chama a função para mostrar os meses do ano
mostrar_meses(ano)

# EOF