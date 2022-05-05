'''
// String str = Here is the string with duplicate words duplicate string
'''

A='Here is the string with duplicate words duplicate string'
B= A.split(' ')
print("The given string is :", A)
print("The split string is:", B)
dictB ={}
for i in B:
    if i in dictB:
        dictB[i]=dictB[i]+1
    else:
        dictB[i]=1
print(dictB)

for i in dictB:
    print(i, ":", dictB[i])