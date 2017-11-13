# TV set application
# User can choose a channel and volume in the indicated ranges

class TV(object):

    def __init__(self, chan = 1, vol = 10):
        self.chan = chan
        self.vol = vol
        

    def channel(self):
        
        print("What channel from 1-20, would you like to watch? ")
        self.chan = int(input("Wybierasz: "))
        
        while self.chan > 20 or self.chan < 1:
            self.chan = int(input("You have chosen nonexistent channel, choose different from 1-20: "))
            print("You chose channel: ", self.chan)


    def volume(self):
        
        print("The volume is set to: ", self.vol, "zn You can choose the volume between 1-20")
        up_or_down = input("Would you like to volume up or down? ")
        up_or_down.lower()
        
        if up_or_down == "up":
            up = int(input("How much would you like to increase the volume? "))
            
            while self.vol + up > 20:
                up = int(input("Too much, the maximum is 20! \nHow much would you like to increase the volume? "))
                
            self.vol += up
            print("You set the volume to: ", self.vol)

        elif up_or_down == "down":

            up = int(input("How much would you like to decrease the volume? "))
            
            while self.vol - up < 1:
                up = int(input("Too low, the manimum is 1! \nHow much would you like to decrease the volume? "))
                
            self.vol -= up
            print("You set the volume to: ", self.vol)
            

def main():

    tv = TV()

    user_choice = None
    while user_choice != "0":
        print("What would you like to do with your TV set? \
          \n 1. Type 1 to change the channel \
          \n 2. Type 2 to change the volume \
          \n 3. Type 0 to exit")
        user_choice = input("Wybierasz: ")
        if user_choice == "1":
            tv.channel()
        elif user_choice == "2":
            tv.volume()
        elif user_choice == "0":
            print("Bye")
        else:
            print("Wrong choice!")
    print(tv.vol, tv.chan)


main()
    
    
            
                
        
            
        
