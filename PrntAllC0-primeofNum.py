from math import gcd

num = int(input("Enter a number"))
lower = int(input("Enter a lower limit"))
upper = int(input("Entr Upper Limit"))
if lower > 0 and lower < upper:
    for i in range(lower, upper+1):
        if gcd(i, num) == 1:
            print(i, end=',')
else:
    print("Invalid Input")
