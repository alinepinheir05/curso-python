def is_prime(num):
    (num > 1 and num % 1 == num and num % num == 0) 

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()