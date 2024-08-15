# Crie um programa onde o computador escolhe um número aleatório entre 1 e 100 e o usuário deve 
# tentar adivinhar o número. O programa deve dar dicas se o número escolhido é maior ou menor 
# que a tentativa do usuário.

import random
num_desconhecido = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input('Adivnhe o número entre 1 a 100: '))
    tentativas += 1
    if chute < num_desconhecido:
        print('O número é maior do que o que você digitou.')
    elif chute > num_desconhecido:
        print('O número é menor do que o que você digitou.')
    else:
        print(f'Parabéns! Você acertou o número em {tentativas} tentativas')