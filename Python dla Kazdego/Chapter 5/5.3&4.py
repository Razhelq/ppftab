# Dictionary app
# User can check who is father or grandfather of people in the dictionary.

Parents = {"Adolf Hitler" : "Alios Hitler", "Alios Hitler" : "Johann Goeg Hieder"}

print("What would you lake to do? \
\n 1. Check the father or grandfather of the person. \
\n 2. Add son and father \
\n 3. Delete son and father \
\n 4. Exit)")

choice = input("What would you like to do?")
finish = True

while choice is not "4":
    if choice == "1":
        who = input("What person would you like to check? ")
        parent = input(" father or grandfather? ")
        parent = parent.lower()
        if parent == "father":
            print(Parents[who])
        elif parent == "grandfather":
            grand = Parents[who] 
            print(Parents[grand])
        else:
            print("Are you sure?")
        choice = input("What next?")

    elif choice == "2":
        son = input("Who will be the son: ")
        Parents[son] = input("... and father: ")
        choice = input("What next?")  

    elif choice == "3":
        to_delete = input("Which son would you like to delete? ")
        if to_delete in Parents:
            del Parents[to_delete]
        else:
            print("Wrong name! ")
        choice = input("What next?")
      
      

