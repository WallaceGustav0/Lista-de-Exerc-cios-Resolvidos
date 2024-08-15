# Dada uma lista de números, crie um programa que exiba apenas os números pares.

lista = list(map(int, input('Digite a lista de números separados por espaço: ').split()))

num_pares = [num for num in lista if num % 2 == 0]

print('Os numeros pares da lista são: ', num_pares)