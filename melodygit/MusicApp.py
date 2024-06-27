from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pygame
import time


class MelodyEditor:

class MelodyApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("melody app")
        self.geometry("800x400")
        self.resizable(width=False, height=False)
        self.configure(background="#f0f0f0")

        img = PhotoImage(file="noty5.png")
        label = Label(self, image=img)
        label.image = img
        label.place(x=120, y=0)

        self.editor = MelodyEditor()
        global entry
        entry = ttk.Entry(width=31)
        entry.place(x=10, y=10)

        entry.bind("<Return>", self.editor.add_chord)

        label_melody_speed = ttk.Label()
        label_melody_speed.place(x=715, y=65)
        label_melody_speed["text"] = "0"
        label_melody_time = ttk.Label()
        label_melody_time.place(x=605, y=42)
        label_melody_time["text"]="melody time"

        label_verse_speed = ttk.Label()
        label_verse_speed.place(x=715, y=170)
        label_verse_speed["text"] = "0"
        label_verse_time = ttk.Label()
        label_verse_time.place(x=617, y=147)
        label_verse_time["text"] = "verse time"

        label_chorus_speed = ttk.Label()
        label_chorus_speed.place(x=715, y=260)
        label_chorus_speed["text"] = "0"
        label_chorus_time = ttk.Label()
        label_chorus_time.place(x=610, y=237)
        label_chorus_time["text"] = "chorus time"

        self.create_button("delete chords", self.editor.delete_chords, 210, 8)

        melodyScale = ttk.Scale(orient=HORIZONTAL, length=100, from_=0.1, to=0.5, command=self.editor.melody_time)
        melodyScale.place(x=677,y=40)
        verseScale = ttk.Scale(orient=HORIZONTAL, length=100, from_=0.1, to=0.5, command=self.editor.verse_time)
        verseScale.place(x=677, y=145)
        chorusScale = ttk.Scale(orient=HORIZONTAL, length=100, from_=0.1, to=0.5, command=self.editor.chorus_time)
        chorusScale.place(x=677, y=235)

        self.create_button("add to verse", self.editor.add_to_verse, 80, 85)
        self.create_button("delete verse", self.editor.delete_verse, 160, 85)
        self.create_button("multiply verse", self.editor.verse_multiply, 705, 110)
        self.create_button("play verse", self.editor.play_verse, 10, 85)

        self.create_button("add to chorus", self.editor.add_to_chorus, 90, 160)
        self.create_button("delete chorus", self.editor.delete_chorus, 180, 160)
        self.create_button("multiply chorus", self.editor.chorus_multiply, 700, 200)
        self.create_button("play chorus", self.editor.play_chorus, 10, 160)

        self.create_button("play melody", self.editor.play_melody, 710, 8)
        self.create_button("play song", self.editor.play_song, 10, 235)

        self.create_button("up", lambda: self.editor.add_pattern("^"), 10, 40, 5)
        self.create_button("down", lambda: self.editor.add_pattern("v"), 60, 40, 5)
        self.create_button("mute", lambda: self.editor.add_pattern("*"), 110, 40, 5)
        self.create_button("pause", lambda: self.editor.add_pattern(" "), 160, 40, 5)
        self.create_button("delete pattern", self.editor.delete_pattern, 210, 40)

        self.label_maj = ttk.Label(text="C     D     E     F     G     A     B", font=(14))
        self.label_maj.place(x=270, y=330)
        self.label_min = ttk.Label(text="Cm     Dm     Em     Fm     Gm     Am     Bm", font=(14))
        self.label_min.place(x=225, y=360)

        self.create_button("<-back to menu", self.back, 5, 370)

    def create_button(self, text, command, x, y, width=None):
        button = Button(text=text, command=command, width=width)
        button.place(x=x, y=y)

    def back(self):
        self.destroy()
        app=Main()

class Tutorial(Tk):
    def __init__(self):
        super().__init__()
        self.title("tutorial")
        self.geometry("1100x600")
        self.resizable(width=False, height=False)
        self.configure(background="#f7f7f7")

        img = PhotoImage(file="headphones.png")
        label = Label(self, image=img)
        label.image = img
        label.place(x=510,y=170)

        self.back_button=ttk.Button(text="<-back to menu", command=self.back)
        self.back_button.place(x=5,y=570)

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

    def back(self):
        self.destroy()
        app=Main()

class Main(Tk):
    def __init__(self):
        super().__init__()
        self.title("menu")
        self.geometry("453x633")
        self.resizable(width=False, height=False)
        img = PhotoImage(file="gitarra.png")
        label = Label(self, image=img)
        label.image = img
        label.place(x=-1,y=-1)

        self.start_button = ttk.Button(text="start", command=self.start)
        self.start_button.place(x=20, y=30)

        self.tutorial_button=ttk.Button(text="tutorial",command=self.tutor)
        self.tutorial_button.place(x=20,y=60)

    def start(self):
        self.destroy()
        app = MelodyApp()

    def tutor(self):
        self.destroy()
        app=Tutorial()

if __name__ == "__main__":
    Main().mainloop()