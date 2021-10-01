secret_number = 777
numero = int(input('Escreva um número:'))

while numero != secret_number:
    print("Ha ha! You're stuck in my loop!")
    numero = int(input('Escreva um número:'))
print("Well done, muggle! You are free now.")
print("+================================+")
print("| Welcome to my game, muggle!    |")
print("| Enter an integer number        |")
print("| and guess what number I've     |")
print("| picked for you.                |")
print("| So, what is the secret number? |")
print("+================================+")