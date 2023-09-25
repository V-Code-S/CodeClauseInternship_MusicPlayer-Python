import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame
import os
from PIL import Image, ImageTk

# Initialize Pygame
pygame.init()

# Create the main window
root = tk.Tk()
root.title("Music Player - VIRUPAKSHI ")
root.configure(bg="black")  # Set the background color to black

# Create a variable to store the selected music file
selected_music = tk.StringVar()

# Create a list of music files in a directory 
music_folder = "C:/Users/viruk/OneDrive/Desktop/mp3"
music_list = [os.path.join(music_folder, file) for file in os.listdir(music_folder) if file.endswith(".mp3")]

# Create variables to keep track of the current index and playback position
current_index = 0
current_position = 0

# Function to play the selected music
def play_music():
    pygame.mixer.music.load(selected_music.get())
    pygame.mixer.music.play(start=current_position)

# Function to pause the music
def pause_music():
    global current_position
    current_position = pygame.mixer.music.get_pos() // 1000  # Get current position in seconds
    pygame.mixer.music.pause()

# Function to stop the music
def stop_music():
    global current_position
    current_position = 0
    pygame.mixer.music.stop()

# Function to play the next music
def next_music():
    global current_index
    current_index = (current_index + 1) % len(music_list)
    selected_music.set(music_list[current_index])
    play_music()

# Function to play the previous music
def prev_music():
    global current_index
    current_index = (current_index - 1) % len(music_list)
    selected_music.set(music_list[current_index])
    play_music()

# Function to rewind the music by 10 seconds
def rewind_music():
    global current_position
    current_position = max(0, current_position - 10)
    play_music()

# Function to fast forward the music by 10 seconds
def fast_forward_music():
    global current_position
    current_position += 10
    play_music()

# Function to choose a music file
def choose_music_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        music_list.append(file_path)
        current_index = len(music_list) - 1
        selected_music.set(file_path)
        play_music()

# Create and configure styles for themed widgets
style = ttk.Style()

# Configure the background color of buttons to red
style.configure("TButton", padding=10, relief="flat", background="red")

# Create and pack widgets
frame = ttk.Frame(root)
frame.pack(pady=10, padx=10)

label = ttk.Label(frame, text="Select a music file:")
label.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

browse_button = ttk.Button(frame, text="Browse", command=choose_music_file)
browse_button.grid(row=1, column=0, columnspan=2, pady=5, padx=5)

play_button = ttk.Button(frame, text="Play", command=play_music)
play_button.grid(row=2, column=0, pady=5, padx=5)

pause_button = ttk.Button(frame, text="Pause", command=pause_music)
pause_button.grid(row=2, column=1, pady=5, padx=5)

stop_button = ttk.Button(frame, text="Stop", command=stop_music)
stop_button.grid(row=2, column=2, pady=5, padx=5)

prev_button = ttk.Button(frame, text="Previous", command=prev_music)
prev_button.grid(row=3, column=0, pady=5, padx=5)

# Load the rewind button image and create a PhotoImage object
rewind_image = Image.open("rewind.png")
rewind_image = rewind_image.resize((30, 30))
rewind_photo = ImageTk.PhotoImage(rewind_image)

# Create the Rewind button with the image
rewind_button = ttk.Button(frame, image=rewind_photo, command=rewind_music)
rewind_button.grid(row=3, column=1, pady=5, padx=5)

# Load the fast forward button image and create a PhotoImage object
fast_forward_image = Image.open("fast_forward.png")
fast_forward_image = fast_forward_image.resize((30, 30))
fast_forward_photo = ImageTk.PhotoImage(fast_forward_image)

# Create the Fast Forward button with the image
fast_forward_button = ttk.Button(frame, image=fast_forward_photo, command=fast_forward_music)
fast_forward_button.grid(row=3, column=2, pady=5, padx=5)

next_button = ttk.Button(frame, text="Next", command=next_music)
next_button.grid(row=4, column=0, pady=5, padx=5)

# Run the main loop
root.mainloop()
