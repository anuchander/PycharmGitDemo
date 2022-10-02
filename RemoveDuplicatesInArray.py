'''
remove duplicates from sorted array arr=[10,20,20,30,30,40,50,50]
'''
def remove_duplicates(a):
    n=len(a)
    count=0
    for i in range(n-1):
        if (a[i] != a[i+1]):
            a[count]=a[i]
            count += 1
    a[count]=a[n-1]
    for i in range(count+1):
        print(a[i], end=' ,')


a=[10,20,20,30,30,40,50,50]
print("The given array is: ", a)
remove_duplicates(a)
