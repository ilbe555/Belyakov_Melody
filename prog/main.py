from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pygame
import time
import melodyapp
import tutorial

## The Main class inherits from Tk
class Main(Tk):
    ## Constructor of the Main class
    def __init__(self):
        super().__init__()
        self.title("menu")
        self.geometry("453x633")
        self.resizable(width=False, height=False)

        # Loading and displaying an image
        img = PhotoImage(file="gitarra.png")
        label = Label(self, image=img)
        label.image = img
        label.place(x=-1,y=-1)

        # The 'start' button
        self.start_button = ttk.Button(text="start", command=self.start)
        self.start_button.place(x=20, y=30)

        # The 'tutorial' button
        self.tutorial_button=ttk.Button(text="tutorial",command=self.tutor)
        self.tutorial_button.place(x=20,y=60)

    ## The method to start the application
    def start(self):
        self.destroy()
        app = melodyapp.MelodyApp()

    ## A method to start learning
    def tutor(self):
        self.destroy()
        app=tutorial.Tutorial()

# The entry point to the program
if __name__ == "__main__":
    Main().mainloop()