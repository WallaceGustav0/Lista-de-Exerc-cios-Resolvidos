# Peça ao usuário para digitar um número e calcule o fatorial desse número.

numero = int(input('Digite um número: '))

fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i

print(f'O fatorial de {numero} é {fatorial}')