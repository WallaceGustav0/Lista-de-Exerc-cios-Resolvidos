# Escreva um programa que converta uma temperatura de graus Celsius para Fahrenheit.
# formula = (0 °C × 9/5) + 32 = 32 °F

celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (celsius * 9/5) + 32

print(f'{celsius}°C é igual a {fahrenheit}°F')