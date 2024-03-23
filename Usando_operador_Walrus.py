# Usando o operador Walrus

print()
print("Usando o operador Walrus ...")
print()
if (vendas:=float(input("Vendas do funcionário R$: "))) > 1000:
    bonus = 0.05 * vendas

else:
    bonus = 0

print()
print(f"O bônus recebido pelo funcionário é de 'R$: {bonus}' pelas vendas.")
print()

# EOF