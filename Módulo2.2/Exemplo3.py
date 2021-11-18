# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
num = int(input("Enter your number: "))

for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + num
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)