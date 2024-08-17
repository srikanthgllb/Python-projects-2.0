import math

x = int(input("Enter the lower interval"))
y = int(input("Enter the upper interval"))
list = []


def Primes(x, y):
    if (x>2 and y > 2) is not True:
        print("It is Invali Input")
    else:
        for digit in range(x, y + 1):
            for divisor in range(2, int(math.sqrt(digit)) + 1):
                if digit % divisor == 0:
                    break
            else:
                list.append(digit)
        #return list
        return ','.join(map(str,list))


print(Primes(x, y))
yt=243
print(int(math.sqrt(yt)))