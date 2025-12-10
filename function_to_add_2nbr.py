def add_numbers(a, b):
    print(f"sum of numbers{a+b}")
def dif_numbers(a, b):
    print(f"dif of numbers{a-b}")
def mul_numbers(a, b):
    print(f"mul of numbers{a*b}")
def div_numbers(a, b):
    print(f"div of numbers{a/b}")

while (True):
    print('Enter the operation to be Performed: ')
    print('1. Add 2 numbers')
    print('2. Subtract 2 numbers')
    print('3. Divide 2 numbers')
    print('4. Multiply 2 numbers')
    print('5. Exit')
    choice = int(input())
    if choice in [1,2,3,4]:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
    if(choice == 1):
        add_numbers(num1, num2)

    elif(choice == 2):
        dif_numbers(num1, num2)
    elif(choice == 3):
        div_numbers(num1, num2)
    elif(choice == 4):
        mul_numbers(num1, num2)
    elif(choice == 5):
        break
    else:
        print('Invalid input')