def is_prime(check_number):
    prime = True
    if check_number <= 1:
        prime = False
    elif check_number % 2 == 0 and check_number != 2:
        prime = False
    elif check_number ** 0.5 == 0:
        prime = False
    
    return prime

check_number = 4

if is_prime(check_number) == False:
    print("The number is not a prime number!")
else:
    print("This number is a prime!")

