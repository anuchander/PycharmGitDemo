'''
Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}
'''

def positive_negative_sort(a):
    n=len(a)
    j=-1
    temp=0
    for i in range(n):
        if (a[i]<0):
            j+=1
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
    print("The positive and negative sorted array is", a)
    #alternative positive and negative in array
    neg=0
    pos=j+1
    while(a[neg]<0 and pos<n and neg<pos):
        temp=a[neg]
        a[neg]=a[pos]
        a[pos]=temp
        pos+=1
        neg+=2
    print("The finally sorted positive and negative number array is: ", a )


a=[1,2,3,-4,-1,4]
print("the given array is: ", a)
positive_negative_sort(a)
