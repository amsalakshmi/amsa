num = int(input("Enter the limit: "))
for n in range(2, num + 1):
    is_prime = True
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
            print(n)