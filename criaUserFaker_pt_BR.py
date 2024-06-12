''' Script que cria usuários falsos (fakes) no idioma Português-BR.
Autor: @pycodebr <instagram>
Adaptado: Daniel Caixeta <@dfcaixeta>
Data: 12.jun.2024 '''

# Importando a biblioteca
from faker import Faker

# Instanciando a bibliotca para o idioma pt-BR.
fake = Faker(locale='pt-br')

# Instanciando as classes do objeto.
nome = fake.name()
email = fake.email()
usuario = fake.user_name()
endereco = fake.address()
telefone = fake.cellphone_number()

# Imprimindo a saída.
print()
print(f'Nome: {nome}')
print(f'Email: {email}')
print(f'Usuário: {usuario}')
print(f'Endereço: {endereco}')
print(f'Telefone: {telefone}')
print()

# EOC


