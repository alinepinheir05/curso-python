palavra = input('Insira uma palavra:')
palavracerta = 'chupacabra'

# while palavra != palavracerta:
#    palavra = input('Insira uma palavra:')
# print("You've successfully left the loop.")

while True:
    if palavra == palavracerta:
        print("You've successfully left the loop.")
        break
    palavra = input('Insira uma palavra:')    
