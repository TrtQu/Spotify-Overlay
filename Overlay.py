import os
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = "http://localhost:8888/callback"
scope = "streaming,user-read-playback-state,user-modify-playback-state,user-read-currently-playing,user-read-private"

sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
    )
sp = Spotify(auth_manager=sp_oauth)

class OverlayGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Spotify Overlay")
        self.geometry("800x500") #window size

        label = ttk.Label(self, text = "Welcome to Spotify Overlay", font = ("Arial", 30, "bold"))
        label.pack()

        button = ttk.Button(self, text = "Get Started", command = self.new_window)
        button.pack()
        self.mainloop()
        
    def new_window(self):
        new_window = tk.Toplevel(self)
        new_window.title("New Window")

OverlayGUI()
