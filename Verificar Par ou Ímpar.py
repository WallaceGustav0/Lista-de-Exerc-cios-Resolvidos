# Peça ao usuário para digitar um número inteiro e informe se o número é par ou ímpar.

numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')