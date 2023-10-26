def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for number in range(2, 251):
    if is_prime(number):
        print(number)

# Open the file in write mode
with open("results.txt", "w") as file:
    for number in range(2, 251):
        if is_prime(number):
            # Write prime numbers to the file
            file.write(str(number) + "\n")

print("Prime numbers have been stored in results.txt.")