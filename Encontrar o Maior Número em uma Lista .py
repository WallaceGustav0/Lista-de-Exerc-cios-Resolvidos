# Peça ao usuário para digitar uma lista de números e exiba o maior número dessa lista.

numeros = list(map(int, input("Digite a lista de números separados por espaço: ").split()))

maior_num = max(numeros)
print(f"O maior número da lista é: {maior_num}")