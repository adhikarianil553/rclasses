# 1. Add name 
# 2. Remove name 
# 3. Display name 
# names ko empty list banyeraw garnu



names=[]
def add_name(name):
    names.append(name)
def remove_name(name):
    if name in names:
        names.remove(name)
    else:
        print("name not found")
def display_name():
    for name in names:
        print(name)
while(1):
    print("1.add_name")
    print("2.remove_name")
    print("3.display_name")
    choice=int(input('choose your choice:'))
    if (choice==1):
        name=input("enter your name")
        add_name(name)
    elif (choice==2):
        name=input("enter your name")
        print("1.add_name")
        
        remove_name(name)
    elif (choice==3):
        display_name()
        
    else:
        break