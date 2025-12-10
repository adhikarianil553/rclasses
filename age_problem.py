ages = [] # empty list to store ages
def add_age(age): # function to add age in the list
    ages.append(age)

def display_age():
    for age in ages:
        print(age)
def remove_age(age):
    if age not in ages:
        print('Age is not in the list')
    else:
        ages.remove(age)


def show_stats():
    sum_ages = sum(ages)
    avg = sum_ages/ len(ages)
    print('Sum of ages: ', sum(ages))
    print('Average age', (sum(ages)/len(ages)))
    print('Maximum age: ', max(ages))
    print('Minimum age: ', min(ages))


def exit(): 
    return 0

while (True): # infinite loop 
    print('Select option to Perform: ')
    print('1. Add new Age')
    print('2. Display Age')
    print('3. Delete Age')
    print('4. Show Statistics')
    print('5. Exit')
    choice = int(input())
    if(choice == 1):
        age = int(input('Enter age: '))
        add_age(age)
        print('Age added successfully')
    elif(choice == 2):
        print('Displaying ages...')
        display_age()
    elif(choice == 3):
        age = int(input('Enter age to be delete: '))
        remove_age(age)
    elif(choice == 4):
        print('Showing Stats...')
        show_stats()
    elif(choice == 5):
        break
    else:
        print('Invalid Choice')