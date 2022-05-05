'''
/*Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array *in place*, do not return anything from your function.
input: [1,0,2,3,0,4,5,0]
output: null
After calling the function input array is now [1,0,0,2,3,0,0,4]
'''
def duplicate_zeros(A):
    n = len(A)
    for i in range(n-1):
        if A[i]==0:
            for j in range(n-1, i+1, -1):
                A[j]=A[j-1]
        A[i+1]=0
        i+=1

    print("The duplicate array is: ", A)
A=[1,0,2,3,0,4,5,0]
print("The given array is: ", A)
duplicate_zeros(A)
