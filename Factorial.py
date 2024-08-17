#5! = 5*4*3*2*1
n = int(input("Enter a num to find its factorial: "))
srt = []
fact = 1
for i in range(n, 0, -1):
    fact = fact * i
    srt.append(str(i))
print(f"{n}! = {' * '.join(srt)} = {fact}")


#using Recursion
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print("factorial of ", n, " is", fact(n))
