'''
 Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the
  right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array *in place*, do not return anything from your function.
input: [1,0,2,3,0,4,5,0]
output: null
After calling the function input array is now [1,0,0,2,3,0,0,4]
'''

def double_zeros(a):
    n=len(a)
    for i in range(n):
        if(a[i]==0):
            for j in range(n-1, i+1, -1):
                a[j]=a[j-1]
        #a[i+1]=0
        #i+=1
    print("The array with double zeros is: ", a)

a=[1,0,2,3,0,4,5,0]
print("the given array is: ", a)
double_zeros(a)
