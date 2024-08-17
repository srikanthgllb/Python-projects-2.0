#154=1^2 +5^2 + 4^2
import math
def countDigits(n):
    l=0
    t=n
    while(t>0):
        t=t//10
        l+=1
    print(l)
    return l



def isArmstrong(n):
    l=countDigits(n)
    mod=10
    sum=0
    m=n
    while(m>0):
        sum=sum + pow(m%10,l)
        m=m//10

    if sum == n:
        print(sum," is Armstrong")
    else:
        print(sum,"is not armstrong")


print(isArmstrong(153))