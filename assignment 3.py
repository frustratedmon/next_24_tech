import tkinter as tk
from tkinter import messagebox
import requests

def fetch_lyrics():
    artist = artist_entry.get().strip()
    song = song_entry.get().strip()
    if not artist or not song:
        messagebox.showerror("Input Error", "Enter both artist and song name:")
        return
    
    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        lyrics = data.get("lyrics", "Lyrics not found.")
        lyrics_text.delete(1.0, tk.END)
        lyrics_text.insert(tk.END, lyrics)
    else:
        messagebox.showerror("API Error", "Could not findlyrics.")


root = tk.Tk()
root.title("Lyrics Fetcher")


tk.Label(root, text="Artist:").grid(row=0, column=0, padx=10, pady=10)
artist_entry = tk.Entry(root, width=30)
artist_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Song:").grid(row=1, column=0, padx=10, pady=10)
song_entry = tk.Entry(root, width=30)
song_entry.grid(row=1, column=1, padx=10, pady=10)

fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=2, column=0, columnspan=2, pady=20)

lyrics_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
