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

def current_song(sp_oauth):
    current_track = sp.current_playback()
    if current_track and current_track['is_playing']:
        track_name = current_track['item']['name']
        artist_name = current_track['item']['artists'][0]['name']
        return f"{track_name} by {artist_name}"
    return "no song playing"

def update_overlay(sp, label):
    def refresh():
        text = current_song(sp)
        label.config(text=text)
        label.after(1000, refresh)  # Refresh every 1 second
    refresh()

def overlay(sp_oauth):
    root = tk.Tk()

    root.title("Spotify Overlay")
    root.geometry("400x100") #window size

    label = tk.Label(root, text = current_song(sp_oauth), font = ("Arial", 10, "bold"))
    label.pack()

    root.mainloop()

