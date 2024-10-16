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

def curr_song(sp_oauth):
    curr_track = sp.current_playback()
    if curr_track and curr_track ['is_playing']: #accessing a value from a dictionary
        track_title = curr_track ['item']['name']#accessing nested values in dictionaries
        artist_name = curr_track ['item']['artists'][0]['name']#accessing an item from a list, the first artist
        song_info = f"{track_title} by {artist_name}" #f string makes the variables literal strings
    


root = tk.Tk()

root.title("Spotify Overlay")
root.geometry("800x500") #window size


label = ttk.Label(root, text = curr_song(sp_oauth), font = ("Arial", 30, "bold"))
root.after(1000, curr_song)
label.pack()

root.mainloop()