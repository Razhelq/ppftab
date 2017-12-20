# Different verion of the Mad Lib app provided with the book.
# The app shows the possibilities of widgets.

from tkinter import *

class New_Lib(Frame):
    def __init__(self, master):
        super(New_Lib, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Put require informations"
              ).grid(row = 0, column = 0, sticky = W)

        Label(self,
              text = "Person: "
              ).grid(row = 1, column = 0, sticky = W)
        self.person = Entry(self)
        self.person.grid(row = 1, column = 1, sticky = W)

        self.universe = StringVar()
        self.universe.set(None) 
        Label(self,
              text = "The best universe: "
              ).grid(row = 2, column = 0, columnspan = 1, sticky = W)
        column = 2
        universe = ["starcraft", "diablo", "warcraft"]
        for uni in universe:
            Radiobutton(self,
                        text = uni,
                        variable = self.universe,
                        value = uni
                        ).grid(row = 2, column = column, sticky = W)
            column += 1

        Label(self,
              text = "What is the best thing in selected universe: "
              ).grid(row = 3, column = 0, columnspan = 2, sticky = W)
        self.gameplay = BooleanVar()
        Checkbutton(self,
                    text = "gameplay",
                    variable = self.gameplay
                    ).grid(row = 3, column = 2 , sticky = W)

        self.immersion = BooleanVar()
        Checkbutton(self,
                    text = "immersion",
                    variable = self.immersion
                    ).grid(row = 3, column = 3, sticky = W)

        self.nolife = BooleanVar()
        Checkbutton(self,
                    text = "nolife",
                    variable = self.nolife
                    ).grid(row = 3, column = 4, sticky = W)

        Button(self,
               text = "Click to sum up.",
               command = self.story
               ).grid(row = 5, column = 0, sticky = W)

        self.story = Text(self, width = 75, height = 10, wrap = WORD)
        self.story.grid(row = 6, column = 0, columnspan = 5)

    def story(self):
        person = self.person.get()
        universe = self.universe.get()
        best_things = ""
        if self.gameplay.get():
            best_things += "gameplay, "
        elif self.immersion.get():
            best_things += "immersion, "
        elif self.nolife.get():
            best_things += "nolife, "
        

        story = "Hello "
        story += person
        story += ". Your favotite universe is "
        story += universe
        story += ".\nThe best thing in that game in your opinion is "
        story += best_things
        story += "\n\tGood choice!"

        self.story.delete(0.0, END)
        self.story.insert(0.0, story)

root = Tk()
root.title("Best game universe")
app = New_Lib(root)
root.mainloop()

        
            
        
               
        
    

        
