#Character creator
#This app will create a hero with 4 atrributes and 30 points to dispatch between them

print("Welcome in to the Character Creator ver. 2.0 ")
print("You have 30 points to spend. ")
print("What would you like to do? ")
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
    

class Character(object):

    def __init__(self, name, strengh, wisdom, health, flex):
        self.name = name
        self.strengh = strengh
        self.wisdom = wisdom
        self.flex = flex
        self.health = health

    def user_choice(self):
        choices = ["strengh", "wisdom", "health", "flex"]
        choice = int(input("\n\nWhat is your choice? ")) - 1
        if choice < 4  or choice >= 0:
            self.attrib = choices[choice]
            #this is stupid
            if self.attrib == "strengh":
                 
                return self.strengh
            elif self.attrib == "wisdom":
                
                return self.wisdom
            elif self.attrib == "flex":
                
                return self.flex
            elif self.attrib == "strengh":
                 
                return self.strengh   
            
    def manage_point(self, chosen):
        global points
        if points >= 0:
            decision = input("Would you like to add or remove? ")
            decision = decision.lower()
            if decision == "add":
                value = int(input("How many point would you like to add? "))
                chosen += value
                points -= int(value)
            elif decision == "remove":
                value = int(input("How many point would you like to remove? "))
                chosen -= value
                points += int(value)
                        
name = input("What is your name? ")

my_char = Character(name, strengh, wisdom, health, flex)

while points >= 0:    
    attrib = my_char.user_choice()
    my_char.manage_point(attrib)
    print(my_char.name, 'Your Strengh =', my_char.strengh,
          ', Wisdom =', my_char.wisdom,
          ', Flexibility =', my_char.health,
          'and Strengh =', my_char.flex)

print(Character)
