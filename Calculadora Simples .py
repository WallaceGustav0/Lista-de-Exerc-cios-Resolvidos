# Crie um programa que peça dois números e a operação desejada (+, -, *, /) e exiba o resultado.

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

operacoes = input('Digite uma operação (+, -, *, /): ')

if operacoes == '+':
    print('O resultado da soma é: ', numero1 + numero2)
elif operacoes == '-':
    print('O resultado da subtração é: ', numero1 - numero2)
elif operacoes == '*':
    print('O resultado da multiplicação é: ', numero1 * numero2)
elif operacoes == '/':
    print('O resultado da divisão é: ', numero1 / numero2)
