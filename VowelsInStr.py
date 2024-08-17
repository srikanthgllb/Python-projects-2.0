sentence="hi,how are you?"
count=0
for i in sentence.lower():
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
        print(i)
print("Vowels",count)

sentence="hi,how are you?"
count=0
list=['a','e','i','o','u']
for char in sentence:
    if char in list:
        print(char)
        count+=1
print('No of vowels is :',count)
