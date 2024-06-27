from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pygame
import time


class MelodyEditor:
    def __init__(self):
        self.melodylist = []
        self.r_pattern = []

        self.chords = ["C", "Cm", "D", "Dm", "E", "Em", "F", "Fm", "G", "Gm", "A", "Am", "B", "Bm"]

        self.verse = []
        self.versepattern = []
        self.mp3verse = []
        self.versecounter = 0
        self.versemultiplier = 1

        self.chorus = []
        self.choruspattern = []
        self.mp3chorus = []
        self.choruscounter = 0
        self.chorusmultiplier = 1

        self.chan = 0

    # speed block
    def melody_time(self, mvalue):
        melody_speed = ttk.Label(width=10)
        melody_speed.place(x=715, y=65)
        melody_speed["text"] = round(float(mvalue), 2)
        self.melody_time = float(mvalue)

    def verse_time(self, vvalue):
        verse_speed = ttk.Label(width=10)
        verse_speed.place(x=715, y=170)
        verse_speed["text"] = round(float(vvalue), 2)
        self.verse_time = float(vvalue)

    def chorus_time(self, cvalue):
        chorus_speed = ttk.Label(width=10)
        chorus_speed.place(x=715, y=260)
        chorus_speed["text"] = round(float(cvalue), 2)
        self.chorus_time = float(cvalue)

    # melody block
    def add_chord(self, event):
        if entry.get() in self.chords:
            if self.melodylist == []:
                self.label = ttk.Label()
                self.label.place(x=310, y=10)
            self.melodylist.append(entry.get())
            self.label["text"] = self.melodylist
            print(self.melodylist)
        entry.delete(0, END)

    def delete_chords(self):
        self.label.destroy()
        self.melodylist.clear()
        print(self.melodylist)

    def add_pattern(self, char):
        if self.r_pattern == []:
            self.pattern_label = ttk.Label()
            self.pattern_label.place(x=310, y=42)
        self.r_pattern.append(char)
        self.pattern_label["text"] = self.r_pattern

    def delete_pattern(self):
        self.pattern_label.destroy()
        self.r_pattern.clear()
        print(self.r_pattern)

    def play_melody(self):
        print(self.melody_time)
        melody_mp3_list = []

        for chord in range(len(self.melodylist)):
            for pattern in range(len(self.r_pattern)):
                if self.r_pattern[pattern] == "*":
                    melody_mp3_list.append("mute.mp3")
                elif self.r_pattern[pattern] == " ":
                    melody_mp3_list.append("pause")
                else:
                    melody_mp3_list.append(self.melodylist[chord] + self.r_pattern[pattern] + ".mp3")
        for chord in melody_mp3_list:
            if chord == "pause":
                time.sleep(float(self.melody_time))
            else:
                if self.chan == 0:
                    self.chan = 1
                else:
                    self.chan = 0
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(chord)
                pygame.mixer.Channel(self.chan).play(pygame.mixer.Sound(chord))
                time.sleep(float(self.melody_time))  # 2

    # add block
    def add_to_verse(self):
        if self.verse == []:
            self.versepatternlabel = ttk.Label()
            self.versepatternlabel.place(x=10, y=140)
            self.verselabel = ttk.Label()
            self.verselabel.place(x=10, y=115)

        self.verse, self.verselabel, self.versepattern, self.versepatternlabel, self.versecounter = self.add_to_song(
            "verse", self.verse, self.verselabel,
            self.versepattern, self.versepatternlabel,
            self.versecounter)
        self.delete_chords()
        self.delete_pattern()

    def add_to_chorus(self):
        if self.chorus == []:
            self.choruspatternlabel = ttk.Label()
            self.choruspatternlabel.place(x=10, y=215)
            self.choruslabel = ttk.Label()
            self.choruslabel.place(x=10, y=190)

        self.chorus, self.choruslabel, self.choruspattern, self.choruspatternlabel, self.choruscounter = self.add_to_song(
            "chorus", self.chorus, self.choruslabel,
            self.choruspattern, self.choruspatternlabel,
            self.choruscounter)
        self.delete_chords()
        self.delete_pattern()

    def add_to_song(self, place, song, songlabel, songpattern, songpatternlabel, songcounter):
        mp3song = []
        if self.melodylist != [] and self.r_pattern != []:
            for chord in range(len(self.melodylist)):
                for pattern in range(len(self.r_pattern)):
                    if self.r_pattern[pattern] == "*":
                        mp3song.append("mute.mp3")
                    elif self.r_pattern[pattern] == " ":
                        mp3song.append("pause")
                    else:
                        mp3song.append(self.melodylist[chord] + self.r_pattern[pattern] + ".mp3")

            if place == "verse":
                self.mp3verse = self.mp3verse + mp3song
            else:
                self.mp3chorus = self.mp3chorus + mp3song
            songcounter = songcounter + 1

            song = song + self.melodylist
            song.append("(" + str(songcounter) + ")" + "/")
            songlabel["text"] = song

            songpattern = songpattern + self.r_pattern
            songpattern.append("(" + str(songcounter) + ")" + "/")
            songpatternlabel["text"] = songpattern

            return song, songlabel, songpattern, songpatternlabel, songcounter

    # delete block
    def delete_verse(self):
        self.verselabel, self.versepatternlabel, self.verse, self.versepattern, self.versecounter, self.mp3verse = self.delete_song(
            self.verselabel,self.versepatternlabel, self.verse,self.versepattern, self.versecounter, self.mp3verse)

    def delete_chorus(self):
        self.choruslabel, self.choruspatternlabel, self.chorus, self.choruspattern, self.choruscounter, self.mp3chorus = self.delete_song(
            self.choruslabel,self.choruspatternlabel,self.chorus,self.choruspattern,self.choruscounter,self.mp3chorus)

    def delete_song(self, songlabel, songpatternlabel, song, songpattern, songcounter, mp3song):
        songlabel.destroy()
        songpatternlabel.destroy()
        song.clear()
        songpattern.clear()
        songcounter = 0
        mp3song.clear()
        return songlabel, songpatternlabel, song, songpattern, songcounter, mp3song

    # multiply block
    def verse_multiply(self):
        self.versemultiplier = self.song_multiply(self.versemultiplier)
        versemultiplier_label = ttk.Label()
        versemultiplier_label.place(x=690, y=113)
        versemultiplier_label["text"] = "x" + str(self.versemultiplier)

    def chorus_multiply(self):
        self.chorusmultiplier = self.song_multiply(self.chorusmultiplier)
        chorusmultiplier_label = ttk.Label()
        chorusmultiplier_label.place(x=686, y=203)
        chorusmultiplier_label["text"] = "x" + str(self.chorusmultiplier)

    def song_multiply(self, songmultiplier):
        songmultiplier = songmultiplier + 1
        if songmultiplier == 5: songmultiplier = 1
        return songmultiplier

    # play block
    def play_verse(self):
        self.play_songpart(self.versemultiplier, self.mp3verse, self.verse_time)
        print(self.verse_time)

    def play_chorus(self):
        self.play_songpart(self.chorusmultiplier, self.mp3chorus, self.chorus_time)
        print(self.verse_time)

    def play_songpart(self, songmultiplier, mp3song, song_time):
        for i in range(songmultiplier):
            for chord in mp3song:
                if chord == "pause":
                    time.sleep(song_time)
                else:
                    if self.chan == 0:
                        self.chan = 1
                    else:
                        self.chan = 0
                    pygame.init()
                    pygame.mixer.init()
                    pygame.mixer.music.load(chord)
                    pygame.mixer.Channel(self.chan).play(pygame.mixer.Sound(chord))
                    time.sleep(song_time) # 1

    def play_song(self):
        self.play_verse()
        self.play_chorus()

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