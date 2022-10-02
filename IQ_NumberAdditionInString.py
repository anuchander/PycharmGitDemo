'''
//Two Number in string _ Add those and print their Addition number
String str="abcd4andalso58";
'''

def add_numbers_in_string(s):
    sum=0
    for i in s:
        if i.isdigit()==True:
            sum+=int(i)
    print("The sum of integers in given string is: ", sum)

s="abcd4andalso58"
print("The given string with numbers is: ", s)
add_numbers_in_string(s)
