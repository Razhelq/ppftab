# Pets farm

# Virtual Pets farm you need to take care of

from random import randrange
import sys

class Critter(object):

    def __init__(self, name, hunger, boredom):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        rep = "Your pet " + self.name + " has the hunger value: " + str(self.hunger) + \
              " and boredom value " + str(self.boredom)
        return rep

    def __time_pass(self):
        self.hunger += 2
        self.boredom += 2

    def mood(self):
        value = self.hunger + self.boredom
        if value < 0:
            value = 0
        if value <= 5 and value >= 0:
            print("Hi, My name is ", self.name, " and I am happy.")
        elif value <= 10 and value > 5:
            print("Hi, My name is ", self.name, " and I am OK.")
        elif value <= 15 and value > 10:
            print("Hi, My name is ", self.name, " and I am soso...")
        elif value <= 20 and value > 15:
            print("Hi, My name is ", self.name, " and I am sad.")
        else:
            print("Hi, My name is ", self.name, " and I am mad as F.")
        self.__time_pass()                  

    def feed(self, food):        
        if food == "1":
            self.hunger -= 1
        elif food == "2":
            self.hunger -= 2
        elif food == "3":
            self.hunger -= 3
        elif food == "4":
            self.hunger -= 4
        elif food == "5":
            self.hunger -= 5
        else:
            print("Wrong value")
        self.__time_pass()

    def play(self, fun):
        if fun == "1":
            self.boredom -= 1
        elif fun == "2":
            self.boredom -= 2
        elif fun == "3":
            self.boredom -= 3
        elif fun == "4":
            self.boredom -= 4
        elif fun == "5":
            self.boredom -= 5
        else:
            print("Wrong value")
        self.__time_pass()

def main():
    print("Hello, please tell me what are the names of you new 5 pets")
    first_pet_name = input("First pet name is: ")
    ran_hunger = randrange(1,11)
    ran_boredom = randrange(1,11)
    pet_one = Critter(first_pet_name, ran_hunger, ran_boredom)
    second_pet_name = input("Second pet name is: ")
    ran_hunger = randrange(1,11)
    ran_boredom = randrange(1,11)
    pet_two = Critter(second_pet_name, ran_hunger, ran_boredom)
    third_pet_name = input("Third pet name is: ")
    ran_hunger = randrange(1,11)
    ran_boredom = randrange(1,11)
    pet_three = Critter(third_pet_name, ran_hunger, ran_boredom)
    fourth_pet_name = input("Fourth pet name is: ")
    ran_hunger = randrange(1,11)
    ran_boredom = randrange(1,11)
    pet_four = Critter(fourth_pet_name, ran_hunger, ran_boredom)
    fifth_pet_name = input("Fifth pet name is: ")
    ran_hunger = randrange(1,11)
    ran_boredom = randrange(1,11)
    pet_five = Critter(fifth_pet_name, ran_hunger, ran_boredom)

    choice = None
    
    while choice != "5":
        print("\n\nWhat would you like to do? \
          \n\n1. Type 1 to check the mood of your pets. \
          \n2. Type 2 to feed your pet. \
          \n3. Type 3 to play with you pets. \
          \n4. Type 4 to check the attributes of your pets. \
          \n5. Type 5 to Exit")

        choice = input("\nWybierasz: ")
        if choice == "1":
            pet_one.mood()
            pet_two.mood()
            pet_three.mood()
            pet_four.mood()
            pet_five.mood()
        elif choice == "2":
            print("How many snack would you like to give to your pets?")
            food = input("1. Type 1 for 1 snack for each pet. \
                         \n2. Type 2 for 2 snack for each pet. \
                         \n3. Type 3 for 3 snack for each pet. \
                         \n4. Type 4 for 4 snack for each pet. \
                         \n5. Type 5 for 5 snack for each pet.")
            pet_one.feed(food)
            pet_two.feed(food)
            pet_three.feed(food)
            pet_four.feed(food)
            pet_five.feed(food)
        elif choice == "3":
            print("How do you want to play with your pet.")
            fun = input("1. Type 1 for 1 min of fun with each pet. \
                         \n2. Type 2 for 2 mins of fun with each pet. \
                         \n3. Type 3 for 3 mins of fun with each pet. \
                         \n4. Type 4 for 4 mins of fun with each pet. \
                         \n5. Type 5 for 5 mins of fun with each pet.")
            pet_one.play(fun)
            pet_two.play(fun)
            pet_three.play(fun)
            pet_four.play(fun)
            pet_five.play(fun)
        elif choice == "4":
            all_together = (pet_one, pet_two, pet_three, pet_four, pet_five)
            print(all_together)
            print(pet_one)
            print(pet_two)
            print(pet_three)
            print(pet_four)
            print(pet_five)
        else:
            print("Thanks!")
            sys.exit()

main()

    
            
            
                     
                     
                  
        
    
