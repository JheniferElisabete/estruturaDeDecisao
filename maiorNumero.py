a = int(input('Informe o primeiro numero '))
b = int(input('Informe o segundo numero '))
if a > b:
    print(f'O primeiro numero ({a}) é maior que o segundo numero ({b})')
elif a < b:
    print(f'O Segundo numero ({b}) é maior que o primeiro numero ({a})')
else:
    print('Os numeros são iguais')