a = float(input('Informe o preço do primeiro produto '))
b = float(input('Informe o preço do segundo produto '))
c = float(input('Informe o preço do terceiro produto '))
if a < b and a < c:
    print('O primeiro produto é o mais barato')
elif b < a and b < c:
    print('O segundo produto é o mais barato')
else:
    print('O terceiro produto é o mais batato')