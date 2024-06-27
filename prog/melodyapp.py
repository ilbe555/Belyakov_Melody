# -*- coding: utf-8 -*-
## @## @ package MelodyApp
# This module contains classes for working with melodies and the application interface.
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pygame
import time
import main

## MelodyEditor class
# A class for editing melodies.
class MelodyEditor:
    ## Constructor of the MelodyEditor class.
    def __init__(self):
        ## A list of melody chords.
        self.melodylist = []
        ## Rhythm pattern.
        self.r_pattern = []

        ## Available chords.
        self.chords = ["C", "Cm", "D", "Dm", "E", "Em", "F", "Fm", "G", "Gm", "A", "Am", "B", "Bm"]

        ## A list of chords for the verse.
        self.verse = []
        ## Rhythm template for the verse.
        self.versepattern = []
        ## List of mp3 files for the verse.
        self.mp3verse = []
        ## Verse counter.
        self.versecounter = 0
        ## The verse multiplier.
        self.versemultiplier = 1

        ## A list of chords for the chorus.
        self.chorus = []
        ## Rhythm template for the chorus.
        self.choruspattern = []
        ## List of mp3 files for the chorus.
        self.mp3chorus = []
        ## Chorus counter.
        self.choruscounter = 0
        ## The chorus multiplier.
        self.chorusmultiplier = 1

        ## The current playback channel.
        self.chan = 0

    ## Setting the melody time.
    #  @param mvalue The time value of the melody.
    def melody_time(self, mvalue):
        melody_speed = ttk.Label(width=10)
        melody_speed.place(x=715, y=65)
        melody_speed["text"] = round(float(mvalue), 2)
        ## Melody time
        self.melody_time = float(mvalue)

    ## Setting the verse time.
    #  @param vvalue The time value of the verse.
    def verse_time(self, vvalue):
        verse_speed = ttk.Label(width=10)
        verse_speed.place(x=715, y=170)
        verse_speed["text"] = round(float(vvalue), 2)
        ## Verse time
        self.verse_time = float(vvalue)

    ## Setting the chorus time.
    #  @param cvalue The time value of the chorus.
    def chorus_time(self, cvalue):
        chorus_speed = ttk.Label(width=10)
        chorus_speed.place(x=715, y=260)
        chorus_speed["text"] = round(float(cvalue), 2)
        ## Chorus time
        self.chorus_time = float(cvalue)

    ## Adding a chord to a melody.
    #  @param event The chord addition event.
    def add_chord(self, event):
        if entry.get() in self.chords:
            if self.melodylist == []:
                self.label = ttk.Label()
                self.label.place(x=310, y=10)
            self.melodylist.append(entry.get())
            self.label["text"] = self.melodylist
            print(self.melodylist)
        entry.delete(0, END)

    ## Removing all chords from the melody.
    def delete_chords(self):
        self.label.destroy()
        self.melodylist.clear()
        print(self.melodylist)

    ## Adding a symbol to the rhythm template.
    #  @param char Symbol to add to the template.
    def add_pattern(self, char):
        if self.r_pattern == []:
            self.pattern_label = ttk.Label()
            self.pattern_label.place(x=310, y=42)
        self.r_pattern.append(char)
        self.pattern_label["text"] = self.r_pattern

    ## Removing the rhythm pattern.
    def delete_pattern(self):
        self.pattern_label.destroy()
        self.r_pattern.clear()
        print(self.r_pattern)

    ## Play the melody.
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
                time.sleep(float(self.melody_time))

    ## Adding a melody to a verse.
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

    ## Adding a melody to the chorus.
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

    ## A common method for adding a melody to a song.
    #  @param place The place of addition (verse or chorus).
    #  @param song is a list of the chords of the song.
    #  @param songlabel is a label for displaying chords.
    #  @param song pattern is the rhythm pattern of a song.
    #  @param songpatternlabel is a label for displaying the rhythm pattern.
    #  @param songcounter Song parts counter.
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

    ## Removing a verse from a song.
    #  @param songlabel The label of the verse.
    #  @param songpatternlabel is the label of the verse rhythm pattern.
    #  @param song is a list of chords of the verse.
    #  @param song pattern is a verse rhythm pattern.
    #  @param songcounter Verse counter.
    #  @param mp3song is a list of mp3 files of the verse.
    def delete_verse(self):
        self.verselabel, self.versepatternlabel, self.verse, self.versepattern, self.versecounter, self.mp3verse = self.delete_song(
            self.verselabel,self.versepatternlabel, self.verse,self.versepattern, self.versecounter, self.mp3verse)

    ## Removing the chorus from the song.
    #  @param songlabel is the label of the chorus.
    #  @param songpatternlabel is the label of the chorus rhythm pattern.
    #  @param song Chorus chord list.
    #  @param song pattern is the rhythm pattern of the chorus.
    #  @param songcounter Chorus counter.
    #  @param mp3song is a list of mp3 files of the chorus.
    def delete_chorus(self):
        self.choruslabel, self.choruspatternlabel, self.chorus, self.choruspattern, self.choruscounter, self.mp3chorus = self.delete_song(
            self.choruslabel,self.choruspatternlabel,self.chorus,self.choruspattern,self.choruscounter,self.mp3chorus)

    ## A common method for deleting a part of a song.
    #  @param songlabel is the label of a part of the song.
    #  @param songpatternlabel is the label of the rhythm pattern of a part of the song.
    #  @param song is a list of chords of a part of the song.
    #  @param song pattern is the rhythm pattern of a part of a song.
    #  @param songcounter Song parts counter.
    #  @param mp3song is a list of mp3 files of a part of the song.
    def delete_song(self, songlabel, songpatternlabel, song, songpattern, songcounter, mp3song):
        songlabel.destroy()
        songpatternlabel.destroy()
        song.clear()
        songpattern.clear()
        songcounter = 0
        mp3song.clear()
        return songlabel, songpatternlabel, song, songpattern, songcounter, mp3song

    ## Multiplication of the verse.
    #  Increases the number of repetitions of the verse.
    def verse_multiply(self):
        self.versemultiplier = self.song_multiply(self.versemultiplier)
        versemultiplier_label = ttk.Label()
        versemultiplier_label.place(x=690, y=113)
        versemultiplier_label["text"] = "x" + str(self.versemultiplier)

    ## Multiplication of the chorus.
    #  Increases the number of repetitions of the chorus.
    def chorus_multiply(self):
        self.chorusmultiplier = self.song_multiply(self.chorusmultiplier)
        chorusmultiplier_label = ttk.Label()
        chorusmultiplier_label.place(x=686, y=203)
        chorusmultiplier_label["text"] = "x" + str(self.chorusmultiplier)

    ## A common method for multiplying parts of a song.
    #  @param song multiplier is a multiplier of parts of a song.
    def song_multiply(self, songmultiplier):
        songmultiplier = songmultiplier + 1
        if songmultiplier == 5: songmultiplier = 1
        return songmultiplier

    ## Playing a verse.
    #  Reproduces the verse taking into account the multiplier.
    def play_verse(self):
        self.play_songpart(self.versemultiplier, self.mp3verse, self.verse_time)
        print(self.verse_time)

    ## Playing the chorus.
    #  Reproduces the chorus taking into account the multiplier.
    def play_chorus(self):
        self.play_songpart(self.chorusmultiplier, self.mp3chorus, self.chorus_time)
        print(self.verse_time)

    ## A common method for playing parts of a song.
    #  @param song multiplier is a multiplier of parts of a song.
    #  @param mp3song is a list of mp3 files of a part of the song.
    #  @param song_time The playback time of a part of the song.
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
                    time.sleep(song_time)

    ## Play the whole song.
    #  Plays the verses first, then the choruses.
    def play_song(self):
        self.play_verse()
        self.play_chorus()

## MelodyApp Class
#  A class for managing the user interface of the application.
class MelodyApp(Tk):
    ## Constructor of the MelodyApp class
    #  Configuring the interface.
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

        ## Melody editor.
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

    ## Button creation function.
    #  This function is responsible for creating a button in the user interface.
    def create_button(self, text, command, x, y, width=None):
        button = Button(text=text, command=command, width=width)
        button.place(x=x, y=y)

    ## The function returns to the previous screen.
    #  This function allows the user to return to the previous interface screen.
    def back(self):
        self.destroy()
        app=main.Main()
