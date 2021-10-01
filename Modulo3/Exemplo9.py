blocks = int(input("Enter the number of blocks: "))
height = 0
x = 0

while blocks > x:
    x += 1
    blocks = blocks - x
    height += 1
           
print("The height of the pyramid:", height)
    
