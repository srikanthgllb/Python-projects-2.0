sentence = [2, "hi how are you?", 1, 2, 3, 1.4, 1, 2]

#sentence=sentence.strip()
print(sentence)
lst = []
duplicates_count = 0
for char in sentence:
    if char not in lst:
        lst.append(char)
    else:
        print("Index of duplicate:", sentence.index(char))
        duplicates_count += 1
print("duplicates_count:", duplicates_count)
print(lst)
print("="*30)

#Youtube
list1=["amul",1,1,1,4,5,6,5]
list2=[i for i in range(len(list1)) if list1[i]==1]
print(list2)