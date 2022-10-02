'''
 * write an algorithm to reverse first 3 numbers, then next 3 numbers, then next 3 numbers. The number will be based on var k.
 * Array=[3,2,4,7,0,3,1,5,8,4] k=3 Output=[4,2,3,3,0,7,8,5,1,4]
'''
def reverse_k_numbers(a,k):
    n=len(a)
    for i in range(0, n, k):
        left =i
        right=min(i+k-1, n-1)
        temp=a[left]
        a[left]=a[right]
        a[right]=temp
    print("The sorted array is: ", a)


a=[3,2,4,7,0,3,1,5,8,4]
print("The given array is: ", a)
k=3
reverse_k_numbers(a,k)