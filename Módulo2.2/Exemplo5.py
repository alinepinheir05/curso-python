a = input('Palavra que geral:')
a = a.lower()
b = input('Palavra que deseja encontrar:')
b = b.lower()

word = True
for letter in b:
    if a.find(letter) == -1:
        word = False
        print('no')
if word == True:
    print('yes')