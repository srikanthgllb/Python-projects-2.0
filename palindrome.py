inp=input("Entr a string: ")
if inp==inp[::-1]:
    print(inp+" is palindrome")
else:
    print(inp + " is not  palindrome")

string='amuls'
#string[start:end:step]
print(string[1:4])
print( string[1:4:2])
print( string[::1]) #no start,no stop,print each step
print( string[::-1]) #no start,no stop,print reverse step