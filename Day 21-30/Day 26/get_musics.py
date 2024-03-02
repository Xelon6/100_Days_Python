import os


#listet alle inhalten von dem order auf und lässt dich einen song selecten 

def music_choice():
    target_dir= "D:\\Music\\Musik\\Rock"
    music_list = os.listdir(target_dir)
    music_shortcut = {}

    for i, music_file in enumerate(music_list):
        music_shortcut[i + 1] = music_file
        print(f"{i + 1}) {music_file}")

    choice = int(input("Please type the number of the music you want to play: "))
    
    if choice in music_shortcut:
        print(f"You selected: {music_shortcut[choice]}")
        return f"{target_dir}\\{music_shortcut[choice]}"
    else:
        print("Invalid choice. Please choose a valid number.")
