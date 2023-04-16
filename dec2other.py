''' Código em Python para conversão de um número deciamal para outros
sistemas numéricos (binário, octal e hexadecimal)
Autor: https://www.programiz.com/python-programming/examples/conversion-binary-octal-hexadecimal
Modificado/alterado: Daniel Caixeta @dfcaixeta em 15.abr.23 '''

# Programa em Python para conversão decimal para as bases bin, oct, hexa

#dec = 344 # Para fazer a conversão direta descomenta ...
#print("The decimal value of", dec, "is:")

dec = int (input('Enter with decimal value: '))

print('')
print('-' * 44)
print('Decimal conversion for {} to another bases' .format(dec))
print('-' * 44)

print('')

print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

print('')

# EOF