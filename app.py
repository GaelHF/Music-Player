from tkinter import filedialog
from tkinter import *
import customtkinter as ctk
import pygame
import os

app = ctk.CTk()
app.title("Music Player")
app.geometry("650x350")


pygame.mixer.init()

menubar = Menu(app)
app.config(menu=menubar)

songs = []
current_song = ""
paused = False

def load_music():
    global current_song
    app.directory = filedialog.askdirectory()
    
    for song in os.listdir(app.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)
            
    for song in songs:
        songlist.insert("end", song)
    
    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

def play_music():
    global current_song, paused
    
    if not paused:
        pygame.mixer.music.load(os.path.join(app.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.unpause()
        paused = False
    
def pause_music():
    global pause
    pygame.mixer.music.pause()
    paused = True
def next_music():
    global current_song, paused
    
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
def prev_music():
    global current_song, paused
    
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
    
organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label="Select Folder", command=load_music)
menubar.add_cascade(label="Music", menu=organise_menu)

songlist = Listbox(app, bg="black", fg="white", width=100, height=15)
songlist.pack()

play_btn_image = PhotoImage(file="./assets/play.png")
pause_btn_image = PhotoImage(file ="./assets/pause.png")
next_btn_image = PhotoImage(file = "./assets/next.png")
previous_btn_image = PhotoImage(file ="./assets/previous.png")

control_frame = ctk.CTkFrame(app)
control_frame.pack()

play_btn = ctk.CTkButton(control_frame, image=play_btn_image, border_width=0, command=play_music, text="")
pause_btn = ctk.CTkButton(control_frame, image=pause_btn_image, border_width=0, command=pause_music, text="")
next_btn = ctk.CTkButton(control_frame, image=next_btn_image, border_width=0, command=next_music, text="")
previous_btn = ctk.CTkButton(control_frame, image=previous_btn_image, border_width=0, command=prev_music, text="")

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
previous_btn.grid(row=0, column=0, padx=7, pady=10)

app.mainloop()
