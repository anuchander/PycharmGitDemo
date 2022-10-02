'''
int []a = {3,1,7,6,5,91,87,67,45, 37};
'''

def binsearch(A,sel):
    n=len(A)
    beg=0
    end=n-1
    while(beg<=end):
        mid = int((beg + end) / 2)
        if A[mid]==sel:
            return mid
        elif sel>A[mid]:
            beg=mid+1
        else:
            end=mid-1



'''
A=[]
x = int(input("Enter no of elements: "))
print("Enter the elements")
for i in range(x):
    ele=int(input())
    A.append(ele)
'''
A=[3,1,7,6,5,91,87,67,45, 37]
print("The elements are: ", A)
sel = int(input("Enter the element to search"))
val = binsearch(A, sel)
print("The value of ", sel, " in Array is: ", val)