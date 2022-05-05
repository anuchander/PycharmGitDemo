'''
Find second largest element in the array: int a[] = {3,67,45,11,2,52,98,70,14,32};
'''
def find_second_max(A):
    n= len(A)

    if n<2:
        return False
    i=0
    j=1
    if A[i]<A[j]:
        first_max=A[j]
        second_max=A[i]
    else:
        first_max=A[i]
        second_max=A[j]
    for k in range(2,n):
        if A[k]>first_max:
            second_max=first_max
            first_max=A[k]
        elif A[k]>second_max:
            second_max=A[k]
    print("The second max element in the array is:", second_max)
    print("The first max element in the array is:", first_max)

A=[3,67,45,11,2,52,98,70,14,32]
print("The given array is: ", A)
find_second_max(A)