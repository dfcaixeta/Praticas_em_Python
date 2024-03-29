# Usando o operador Walrus

''' Com esse operador, é possível atribuir um valor a uma variável dentro de uma expressão.
Isso pode simplificar o código e deixá-lo mais legível, principalmente em casos em que é necessário
verificar uma condição antes de atribuir um valor a uma variável. '''

# @utor: Daniel Caixeta - dfcaixeta - Data: 23.mar.2024

print('-' * 30)
print("Usando o operador Walrus ...")
print('-' * 30)

print()

# Dados de entrada ...
funcionario = input("Digite o nome do funcionário: ")

# Usando o operador walrus :=
if (vendas:=float(input("Vendas do funcionário R$: "))) > 1000:
    bonus = 0.05 * vendas

    print()
    print(f"O bônus recebido pelo funcionário {funcionario} é de 'R$: {round(bonus, 2)}' pelas vendas.")

else:
    bonus = 0
    print()
    print(f'O funcionário {funcionario} não recebeu bônus por vendas!')

print()

# EOF