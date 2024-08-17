'''An Anagram of a string is an another string that contains
same characters only the order of characters can be different '''
"heart=earth"
str1 = input("Enter first string: ")
str1=sorted(str1.lower())
str2 = input("Enter second string: ")
str2=sorted(str2.lower())

if len(str1)==len(str2):
    if str1 == str2:
        print("The given strs is Anagram")
    else:
        print("The given strs is not Anagram")
else:
    print("The given strs is not Anagram")
