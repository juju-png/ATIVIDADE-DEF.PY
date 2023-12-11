# Exercício Python 02: Crie um programa que leia dois números e mostre a soma, a
# subtração, a multiplicação e a divisão entre eles.

def calculo(num1, num2):
    soma = num1 + num2
    sub = num1 - num2 or num2 - num1
    mult = num1* num2
    div = num1/num2 or num1/num2
    print(soma)
    print(sub)
    print(mult)
    print(div)

num1 =int(input("digite o 1 numero desejado: "))
num2 =int(input("digite o 2 numero desejado: "))

calculo(num1, num2)