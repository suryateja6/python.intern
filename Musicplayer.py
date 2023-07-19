import os
import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Colorful Music Player")
        self.geometry("600x400")
        self.playlist = []
        self.current_index = -1

        pygame.init()
        pygame.mixer.init()

       
        style = ttk.Style()
        style.theme_use("clam")

        self.create_widgets()

    def create_widgets(self):
        self.playlist_box = tk.Listbox(self, bg="#202020", fg="white", selectbackground="red", selectforeground="white")
        self.playlist_box.pack(fill=tk.BOTH, expand=True)

        self.open_button = ttk.Button(self, text="Open", command=self.add_to_playlist, style="Accent.TButton")
        self.open_button.pack()

        self.play_button = ttk.Button(self, text="Play", command=self.play_music, style="Accent.TButton")
        self.play_button.pack()

        self.pause_button = ttk.Button(self, text="Pause", command=self.pause_music, style="Accent.TButton")
        self.pause_button.pack()

        self.stop_button = ttk.Button(self, text="Stop", command=self.stop_music, style="Accent.TButton")
        self.stop_button.pack()

        self.next_button = ttk.Button(self, text="Next", command=self.next_song, style="Accent.TButton")
        self.next_button.pack()

        self.prev_button = ttk.Button(self, text="Previous", command=self.prev_song, style="Accent.TButton")
        self.prev_button.pack()

    def add_to_playlist(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            self.playlist_box.insert(tk.END, os.path.basename(file_path))

    def play_music(self):
        if not self.playlist:
            return

        if self.current_index == -1:
            self.current_index = 0

        current_song = self.playlist[self.current_index]
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_song(self):
        if not self.playlist:
            return

        self.stop_music()
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play_music()

    def prev_song(self):
        if not self.playlist:
            return

        self.stop_music()
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play_music()

if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()
