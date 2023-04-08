# Desenvolvido por Prô Terra - MakerZine
# Para mais detalhes, acesse: https://www.makerzine.com.br
# Alterado @dfcaixeta em 08.abr.23

print(" ** Conversão base decimal para base binária ** ")
print('')
dividendo = int(input("Entre com um número decimal para ser convertido em base 2: "))

numero_digitado = dividendo
quociente = 1
lista = []

while quociente >= 1:
  resto = dividendo%2
  lista.insert(0,resto)
  quociente = dividendo // 2
  dividendo = quociente

binario = ''.join([str(item) for item in lista])

print('')

print("O número decimal" ,numero_digitado," => " ,binario, "(binário)")

print('')

# EOF