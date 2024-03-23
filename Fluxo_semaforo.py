''' Código fluxo estado de um sinal de trânsito em condições normais
usando blocos condicionais (if ... elif ... else).

 - Verde -> Siga!
 - Vermelho -> Pare!
 - Amarelo -> Atenção!
 - Nenhum -> Semáforo desligado.

Autor: Daniel Caixeta @dfcaixeta em 03.jun.23 '''

# Input com as condições do semáforo.
print('Escolha: verde, vermelho, amarelo, nenhum ...')

print('')

sinal = input('Indique o status do sinal: ')

print('')

# Condição do semafóro.
if sinal == 'verde': 
    print('Sinal aberto ... Siga!')

elif sinal == 'vermelho':
    print('Sinal fechado ... Pare!')

elif sinal == 'amarelo':
    print('Cuidado ... Atenção!')

elif sinal == 'nenhum':
      print('Sinal de trânsito desligado!')

elif sinal != 'verde' 'vermelho' 'amarelo':
    print('Condição não satisfeita')

else :
    print('Sinal de trânsito desligado!')

print('')

# EOF
