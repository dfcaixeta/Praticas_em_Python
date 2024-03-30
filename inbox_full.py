''' Algoritmo que indica se caixa de infos está cheia ou não.
Autor: Daniel Caixeta @dfcaixeta em 10.jun.23.'''

print('-' * 15)
# Indica se a caixa está cheia (True) ou não (False) --> bool.
inbox_full = True
show_alert = inbox_full == True

# Bloco condicional ...
if show_alert:
    print("Inbox full!")
    print("Archive some files to continue!")

else:
    print("Inbox has yet space!")

print('-' * 15)

# EOF
