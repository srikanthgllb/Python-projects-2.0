num=int(input("Enter a range"))
for divisor in range(2,num+1):
    for i in range(2,divisor):
        if divisor%i==0:
            #print(divisor,"It is not prime")
            break
    else:

        if divisor>10:
            k=str(divisor)
            if  k==k[::-1]:
                print(divisor,"Is palindromic prime")
            else:
                print(divisor,"is prime ")

