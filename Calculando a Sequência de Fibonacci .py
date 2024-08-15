# Escreva um programa que gera os primeiros 10 números da sequência de Fibonacci.

def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia
    
fibonacci_10 = fibonacci(10)

print('Os primeiros 10 números da sequência de Fibonacci são: ', fibonacci_10)