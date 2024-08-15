# Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário.

string = input('Digite uma string: ').lower()

vogais = 'aeiou'
quantidade = 0

for letra in string:
    if letra in vogais:
        quantidade += 1
print(f'A string tem {quantidade} vogais.')