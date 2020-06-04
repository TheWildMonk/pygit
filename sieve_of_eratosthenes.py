# Sieve of Eratosthenes Algorithm

user_input = int(input("Please enter the range of Prime Numbers: "))

prime_numbers_list = [prime_numbers for prime_numbers in range(user_input+1)]

prime_numbers_list[0] = False
prime_numbers_list[1] = False

for prime_numbers in range(2, user_input+1):
    if not prime_numbers_list[prime_numbers]:
        continue
    for strike_out in range(prime_numbers*prime_numbers, user_input+1, prime_numbers):
        prime_numbers_list[strike_out] = False

for prime_numbers in range(2, user_input+1):
    if prime_numbers_list[prime_numbers]:
        print(prime_numbers_list[prime_numbers])
        
