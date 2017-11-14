#Character creator
#This app will create a hero with 4 atrributes and 30 points to dispatch between them

print("Welcome in to the Character creator. ")
print("You have 30 points to spend. ")
print("What would you like to do: ")
print("\n 1. Change the value of the Strengh. \
      \n 2. Change the value of the Wisdom. \
      \n 3. Change the value of the Health. \
      \n 4. Change the value of the Flexibility. \
      \n 5. Exit. ")

points = 30
strengh = 0
wisdom = 0
health = 0
flex = 0


choice = input("\n\n What is your choice? ")

while points >= 0:
    if choice == "1":
        str_choice = input("Would you like to add or remove? ")
        str_choice = str_choice.lower()
        if str_choice == "add":
            str_value = int(input("How many point would you like to add? "))
            strengh += str_value
            points -= str_value
        elif str_choice == "remove":
            str_value = int(input("How many point would you like to remove? "))
            strengh -= str_value
            points += str_value
        choice = input("What is your next choice? ")
    elif choice == "2":
        wisdom_choice = input("Would you like to add or remove? ")
        wisdom_choice = wisdom_choice.lower()
        if wisdom_choice == "add":
            wisdom_value = int(input("How many point would you like to add? "))
            wisdom += wisdom_value
            points -= wisdom_value
        elif wisdom_choice == "remove":
            wisdom_value = int(input("How many point would you like to remove? "))
            wisdom -= wisdom_value
            points += wisdom_value
        choice = input("What is your next choice? ")
    elif choice == "3":
        health_choice = input("Would you like to add or remove? ")
        health_choice = health_choice.lower()
        if health_choice == "add":
            health_value = int(input("How many point would you like to add? "))
            health += health_value
            points -= health_value
        elif health_choice == "remove":
            health_value = int(input("How many point would you like to remove? "))
            wisdom -= health_value
            points += health_value
        choice = input("What is your next choice? ")
    elif choice == "4":
        flex_choice = input("Would you like to add or remove? ")
        flex_choice = flex_choice.lower()
        if flex_choice == "add":
            flex_value = int(input("How many point would you like to add? "))
            flex += flex_value
            points -= flex_value
        elif flex_choice == "remove":
            flex_value = int(input("How many point would you like to remove? "))
            flex -= flex_value
            points += flex_value
        choice = input("What is your next choice? ")
    elif choice == "5":
        break
    else:
        print("Wrong value!")
        choice = input("What is your next choice? ")
        
            
    
