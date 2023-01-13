# importing libraries
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import time
from mutagen.mp3 import MP3


# add many songs to the playlist
def addsongs():
    # a list of songs is returned
    temp_song = filedialog.askopenfilenames(
        initialdir="Music/",
        title="Choose a song",
        filetypes=(("mp3 Files", "*.mp3"),)
    )
    # loop through everyitem in the list
    for s in temp_song:
        s = s.replace("C:/Users/bhakt/OneDrive/Desktop/Musicplayerr/", "")
        songs_list.insert(END, s)


def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])


def Play():
    song = songs_list.get(ACTIVE)
    song = f'C:/Users/bhakt/OneDrive/Desktop/Musicplayerr/{song}'
    mixer.music.load(song)
    mixer.music.set_volume(0.5)
    mixer.music.play()
    play_time()


def play_time():
    # grab current song elapsed time
    current_time = mixer.music.get_pos() / 1000
    # convert to time format
    cur_time = time.strftime('%M:%S', time.gmtime(current_time))
    # to get the next song
    song = songs_list.get(ACTIVE)
    song = f'C:/Users/bhakt/OneDrive/Desktop/Musicplayerr/{song}'

    # load song with mutagen
    song_mut = MP3(song)
    # get song length(mutagen)
    song_length = song_mut.info.length
    # convert to time format
    cur_songlen = time.strftime('%M:%S', time.gmtime(song_length))

    # output time to status bar
    status_bar1.config(text=f' Time Elapsed : ')
    status_bar2.config(text=f' {cur_time}  of  {cur_songlen}  ')
    # update time
    status_bar2.after(1000, play_time)


# to pause the song
def Pause():
    mixer.music.pause()


# to stop the  song
def Rewind():
    mixer.music.rewind()


# to resume the song
def Resume():
    mixer.music.unpause()


# Function to navigate from the current song
def Previous():
    # to get the selected song index
    previous_one = songs_list.curselection()
    # to get the previous song index
    previous_one = previous_one[0] - 1
    # to get the previous song
    temp2 = songs_list.get(previous_one)
    temp2 = f'C:/Users/bhakt/OneDrive/Desktop/Musicplayerr/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    # activate new song
    songs_list.activate(previous_one)
    # set the next song
    songs_list.selection_set(previous_one)


def Next():
    # to get the selected song index
    next_one = songs_list.curselection()
    # to get the next song index
    next_one = next_one[0] + 1
    # to get the next song
    temp = songs_list.get(next_one)
    temp = f'C:/Users/bhakt/OneDrive/Desktop/Musicplayerr/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    # activate newsong
    songs_list.activate(next_one)
    # set the next song
    songs_list.selection_set(next_one)


# creating the root window
root = Tk()
root.title('Music Player')
# initialize mixer
mixer.init()

# create the listbox to contain songs
songs_list = Listbox(
    root,
    selectmode=SINGLE,
    bg="black",
    fg="white",
    font=('Times new roman', 15),
    height=12,
    width=56,
    selectbackground="light pink",
    selectforeground="black"
)
songs_list.grid(pady=4, columnspan=8)

# font is defined which is to be used for the button font
defined_font = font.Font(family='Times new roman')

# play button
play_button = Button(
    root,
    text="Play",
    width=12,
    activeforeground="white",
    activebackground="dark orange",
    command=Play
)
play_button['font'] = defined_font
play_button.grid(row=2, column=2)

# status of song playing
status_bar1 = Label(
    root,
    text='',
    width=20,
    bd=1,
    relief=SUNKEN,
    anchor=CENTER,
    height=2
)
status_bar1.grid(row=1, column=2)
status_bar2 = Label(
    root,
    text='',
    width=20,
    bd=1,
    relief=SUNKEN,
    anchor=CENTER,
    height=2
)
status_bar2.grid(row=1, column=3)

# pause button
pause_button = Button(
    root,
    text="Pause",
    width=12,
    activeforeground="white",
    activebackground="dark orange",
    command=Pause
)
pause_button['font'] = defined_font
pause_button.grid(row=2, column=3)

# rewind button
rewind_button = Button(
    root,
    text="Rewind",
    width=12,
    activeforeground="white",
    activebackground="dark orange",
    command=Rewind
)
rewind_button['font'] = defined_font
rewind_button.grid(row=2, column=1)

# resume button
Resume_button = Button(
    root,
    text="Resume",
    width=12,
    activeforeground="white",
    activebackground="dark orange",
    command=Resume
)
Resume_button['font'] = defined_font
Resume_button.grid(row=2, column=4)

# previous button
previous_button = Button(
    root,
    text="Prev",
    width=12,
    activeforeground="white",
    activebackground="dark orange",
    command=Previous
)
previous_button['font'] = defined_font
previous_button.grid(row=1, column=1)

# nextbutton
next_button = Button(
    root,
    text="Next",
    width=12,
    activeforeground="white",
    activebackground="dark orange",
    command=Next
)
next_button['font'] = defined_font
next_button.grid(row=1, column=4)

# menu
my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)
add_song_menu.add_command(label="Delete song", command=deletesong)

mainloop()



