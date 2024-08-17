a = int(input("Entr a value of 'a': "))
b = int(input("Entr a value of 'b': "))
# #Method 1
# temp=a
# a=b
# b=temp
#method 2let(a=10,b=5)
a = a + b  #15=10+5
b = a - b  #10=15-5
a = a - b  #5=15-10
#Method 3
# a,b=b,a

print("After Swapping")
print("value of 'a' is ", a)
print("value of 'b' is ", b)
