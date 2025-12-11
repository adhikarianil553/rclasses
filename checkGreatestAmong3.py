a=int(input("enter a number"))
# this is the first number
b=int(input("enter a number"))
# this is the second number
c=int(input("enter a number"))
# this is the third number
#check if a is greater than both b and c
if a>b and a>c:
    print("a is greatest")
    #if a is not greatest, check if b is greater than both a and c
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")