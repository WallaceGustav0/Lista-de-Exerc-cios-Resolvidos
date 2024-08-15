# Peça ao usuário para digitar uma palavra e verifique se ela é um palíndromo (lê-se da mesma 
# forma de trás para frente).

palavra = input('Digite uma palavra: ').lower()
if palavra == palavra [::-1]:
    print(f'{palavra} é um palíndromo')
else:
    print(f'{palavra} não é um palíndromo')