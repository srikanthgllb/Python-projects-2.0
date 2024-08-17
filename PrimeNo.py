import math

k = int(input("Enter a num to verify it is prime"))
def isPrime(n):
    m = int(math.sqrt(n))
    prime = True

    for divisor in range(2, m + 1):
        if n % divisor == 0:
            prime = False
            break
    return prime


if k > 2:
    if isPrime(k):
        print(k, "is prime number")
    else:
        print(k, "is composite number")
else:
    print(k, "is neither prime nor composite number")

# z=12.5
# print(int(z))