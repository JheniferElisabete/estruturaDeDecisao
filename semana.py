'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''
s = int(input('Informe um numero de 1 a 7 para saber qual dia da semana será '))
if s == 1:
    print('Domingo')
elif s == 2:
    print('Segunda')
elif s == 3:
    print('Terça')
elif s ==4:
    print('Quarta')
elif s == 5:
    print('Quinta')
elif s == 6:
    print('Sexta')
elif s == 7:
    print('Sabado')
else:
    print('Numero invalido')