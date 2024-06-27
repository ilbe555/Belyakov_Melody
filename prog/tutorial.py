from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pygame
import time
import main

## The Tutorial class inherits from Tk and is a learning window of the application
class Tutorial(Tk):
    ## The constructor of the Tutorial class
    def __init__(self):
        super().__init__()
        self.title("tutorial")
        self.geometry("1100x600")
        self.resizable(width=False, height=False)
        self.configure(background="#f7f7f7")

        # Loading and displaying an image
        img = PhotoImage(file="headphones.png")
        label = Label(self, image=img)
        label.image = img
        label.place(x=510,y=170)

        # Return button to the menu
        self.back_button=ttk.Button(text="<-back to menu", command=self.back)
        self.back_button.place(x=5,y=570)

        # Label with instructions
        self.label_tutor = ttk.Label(text="Алгоритм работы с генератором мелодий:\n"
                                          "\n"
                                          "- Ввести в текстовое поле последовательность аккордов \n"
                                          "(список доступных аккордов находится внизу окна) \n"
                                          "и добавить их в текущую мелодию клавишей Enter\n"
                                          "\n"
                                          "- Добавить в текущую мелодию ритмический паттерн,\n"
                                          "используя кнопки ниже текстового поля\n"
                                          "\n"
                                          "- Время проигрывания получившейся мелодии можно изменить ползунком\n"
                                          "'melody time' и прослушать, нажав на кнопку 'play melody'\n"
                                          "\n"
                                          "- Когда мелодия будет готова, добавить её к куплету или припеву кнопками\n"
                                          "'add to verse' и 'add to chorus' соответственно\n"
                                          "\n"
                                          "- Настроить количество раз проигрывания куплета и припева кнопками\n"
                                          "'multiply verse' и 'multiply chorus'\n"
                                          "\n"
                                          "- Настроить время проигрывания куплета и припева ползунками \n"
                                          "'verse time' и 'chorus time'\n"
                                          "\n"
                                          "- Прослушать получившуюся песню, нажав на кнопку 'play song'\n"
                                          "\n"
                                          "Стандартные паттерны:\n"
                                          "- v {} v ^ {} ^ v ^ - 'шестёрка'\n"
                                          "- v {} {} {} v {} {} ^ {} ^ v {} v {} v ^ - 'восьмёрка'\n"
                                          "- v {} v ^ v {} v ^ v {} v ^ v {} v ^ - 'галоп'\n"
                                          "- v ^ * ^ - 'четвёрка'\n", font=(8), background="#f7f7f7")
        self.label_tutor.place(x=10, y=10)

    ## Method to return to the main menu
    def back(self):
        self.destroy()
        app=main.Main()