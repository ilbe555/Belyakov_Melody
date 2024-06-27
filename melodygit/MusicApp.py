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

class Tutorial(Tk):

class Main(Tk):

if __name__ == "__main__":
    Main().mainloop()