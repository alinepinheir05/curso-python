year = int(input("Enter a year: "))
if year % 4 != 0:
    print('Ano Comum!')
elif year % 100 != 0:
    print('Ano Bissexto!')
elif year % 400 != 0:
    print('Ano Comum!')
else:
    print('Ano Bissexto!')
