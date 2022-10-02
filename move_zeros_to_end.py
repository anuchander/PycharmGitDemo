'''
/*
 * Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0};
 */
'''

def move_zeros_to_right(a):
    n= len(a)
    count=0
    for i in range(n-1):
        if(a[i]!=0):
            a[count]=a[i]
            count+=1
    while(count<n):
        a[count]=0
        count+=1
    print("The arranged array with zeros to the end is: ", a)

a=[1,2,0,4,3,0,5,0]
print("the given array is: ", a)
move_zeros_to_right(a)
