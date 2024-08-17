'''When GCD of two number is 1,then that two numbers are called as co-prime.
#coprime
21 -> 1,3,7,21
22 -> 1,2,11,22{1 is GCD.so,it is coprime}
#NO-coprime
21 -> 1,3,7,21
24 -> 1,2,3,4,6,8,12,24{GCD is 3,so not coprime}
'''
from math import gcd

num1 = int(input("Enter a num1: "))
num2 = int(input("Enter a num2: "))
# div1 = [i for i in range(1,num1) if num1 % i == 0]
# print(div1)
# div2 = [i for i in range(1,num2) if num2 % i == 0]
# print(div2)
print("GCD is: ", gcd(num1, num2))
if gcd(num1, num2) == 1:
    print(num1, "and", num2, 'are co-primes')
else:
    print(num1, "and", num2, 'are NOT co-primes')
