import os
import time
import pygame
from get_musics import music_choice


#funktion um musik abzuspielen mit pygame
def play(music_path):
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()

    while True:
        stop_playback = input("Press 2 to stop the music and go back to the menu: ")

        # Start taking user input and doing something with it
        if stop_playback == "2":
            pygame.mixer.music.stop()
            return
        else:
            continue

while True:
    # clear the screen
    os.system("cls")
    # Show the menu
    MENU = "MyPOD Music Player\n\nPress 1 to Play a song of your choice\nPress 2 to Exit\n"
    # take user's input
    choice = input(MENU)

    # check whether you should call the play() subroutine depending on user's input
    if choice == "1":
        play(music_choice())
    elif choice == "2":
        os.system("cls")
        print("See you next time")
        time.sleep(1)
        exit()
    else:
        continue
