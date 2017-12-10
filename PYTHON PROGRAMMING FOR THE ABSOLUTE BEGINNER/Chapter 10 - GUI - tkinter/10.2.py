# Computer choose random number in range(1,100)
# Player tries to guess the number and app informs him when the number is too small or too big.
# GUI based app


import random
from tkinter import *


class Whats_the_number(Frame):
    def __init__(self, master):
        super(Whats_the_number, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.the_number = random.randint(1, 100)
        
        Label(self,
              text = "What is the number?"
              ).grid(row = 0, column = 0, sticky = W)
        
        Label(self,
              text = "Your guess:"
              ).grid(row = 1, column = 0, sticky = W)

        self.number = Entry(self)
        self.number.grid(row = 1, column = 1, sticky = W)
        
        Button(self,
               text = "Click to check the number.",
               command = self.answer
               ).grid(row = 2, column = 0, sticky = W)

        self.answer = Text(self, width = 50, height = 5, wrap = WORD)
        self.answer.grid(row = 3, column = 0, columnspan = 2)

    def answer(self):
        number = self.number.get()
        number = int(number)
        the_number = self.the_number
        
        if number > the_number:
            answer = "Too big..."        
            self.answer.delete(0.0, END)
            self.answer.insert(0.0, answer)
        elif number < the_number:
            answer = "Too small..."
            self.answer.delete(0.0, END)
            self.answer.insert(0.0, answer)
        elif number == the_number:
            answer = "Congratulations, the number is: "
            answer += str(the_number)
            self.answer.delete(0.0, END)
            self.answer.insert(0.0, answer)
        

root = Tk()
root.title("What is the number")
app = Whats_the_number(root)
root.mainloop()
        
        
