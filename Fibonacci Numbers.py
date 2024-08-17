num = int(input("Enter a num"))
numbers = []
t1 = 0
t2 = 1
for i in range(num):
    print(t1)
    numbers.append((t1))

    t3 = t2 + t1
    t1 = t2
    t2 = t3
#print(numbers)
print(','.join(map(str, numbers)))
print("Sum of series", sum(numbers))

