# Exercício Python 03: Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento

def aumento(x):
    salario = x*0.15
    salario_novo = x + salario
    print(salario_novo)

salario = int(input("dgite seu salario e saiba qual o seu aumento"))
aumento(salario)