# Peça ao usuário para digitar um número e imprima a tabuada desse número de 1 a 10.

numero = int(input('Digite um número: '))

for num in range(1, 11):
    print(f'{numero} x {num} = {numero * num}')