hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
sub = int(input('Escreva um número para escrever o número médio:'))
hat_list[2] = sub
del hat_list[4]
print("New list's length:", len(hat_list)) 

print(hat_list)