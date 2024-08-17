# 6 -->divisors of 6(except 6) =(1,2,3)
# 1+2+3=6 #perfect number exmple:6,28,496,8128
import math
#n = int(input("Enter a num to find Whether it is Perfect number"))
# n = 8128
# print(int(math.sqrt(n))+2)
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum += i
#         #print(i)
# if n == sum:
#     print(n, "is Perfect number")
# else:
#     print(n, "is not Perfect number")


# GENERAL TO FIND PERFECT NUMBERS BETWEEN INTERVALS   ##
import math

# st = int(input("Enter a lower interval number"))
# ed = int(input("Enter a higher interval number"))
#
#
# def Perfect_Numbers(st, ed):
#     stg = []
#     total = 0
#     for number in range(st, ed + 1):
#         total = sum(i for i in range(1, number) if number % i == 0)
#
#         if total == number:
#             stg.append(total)
#
#     return stg
#
# print(Perfect_Numbers(st, ed))

## ANOTHER METHOD  ##
lower = int(input("Enter a lower interval number"))
upper = int(input("Enter a higher interval number"))
for num in range(lower, upper + 1):
    result = 0
    for i in range(1, num):
        if num % i == 0:
            result += i
    if result == num:
        print(num)
