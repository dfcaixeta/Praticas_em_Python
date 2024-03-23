import calendar

def mostrar_calendario(ano, mes):
    # Mostra o calendário do ano e mês especificados
    cal = calendar.month(ano, mes)
    return cal

# Solicita entrada do usuário para o ano e mês desejados
ano = int(input("Digite o ano (ex: 2023): "))
mes = int(input("Digite o mês (1-12): "))

# Chama a função para mostrar o calendário
calendario = mostrar_calendario(ano, mes)
print(f"\nCalendário do mês {mes} do ano {ano}:\n")
print(calendario)
