#Create function to add age values to the list

#Function to add age values to the list
def add_age(ages):
    age = int(input("Enter age: "))
    ages.append(age)
def display_ages(ages):
   print("age: ", ages)  
def calculate_statistics(ages):
   if not ages:
      print("List is empty.No statistics to calculate")
      return
   avg_age=sum(ages)/len(ages)
   max_age=max(ages)
   min_age=min(ages)
   print("Average age: ", avg_age)
   print("Max age: ", max_age)
   print("Min age: ", min_age)
def delete_age(ages):
   if not ages:
      print("List is empty.No elements to delete.")
      return
   print("current list:", ages)
   try:
      index=int(input("enter index of element to delete"))
      if 0<=index<len(ages):
         del ages[index]
         print("element deleted successfully.")
      else:
         print("inviled input. Please enter a viled index.")
   except ValueError:
   
         print("invalid index! Please enter a valid index")
# Initialize an empty list to store age values
age_list = []
while True:
# Display menu options
  print("\nMenu:")
  print("1. Add age")
  print("2. Display ages")
  print("3. Calculate")
  print("4. Delete ages")
  print("5. Exit")
  choice = input("Enter your choice (1/2/3/4/5): ")
  if choice == "1":
     add_age(age_list)
  elif choice == "2":
     display_ages(age_list)
  elif choice == "3":
     calculate_statistics(age_list)
  elif choice == "4":
     delete_age(age_list)
  elif choice == "5":
   print("Exiting program...")
   break
else:
   print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")