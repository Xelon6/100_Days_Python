import os
import re
import csv
import time

FILE_NAME="100MostStreamedSongs.csv"

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

os.chdir(os.path.dirname(os.path.realpath(__file__)))


clear_console()
print("Sorting your songs :)")
time.sleep(1)

with open(FILE_NAME,"r",encoding="UTF-8") as f:
    file = csv.DictReader(f)
    
    folder = "Songs"
    if not os.path.exists(folder):
        os.mkdir(folder)

    try:
        for row in file:
            artist = row["Artist(s)"]
            song_raw = row["Song"]
            artist_folder = os.path.join(folder, artist)
            
            song = re.sub(r'[^\w\s]+', '', song_raw)
            
            
            # Create artist folder if it doesn't exist
            if not os.path.exists(artist_folder):
                os.mkdir(artist_folder)
            
            # Check if the song file already exists
            song_file_path = os.path.join(artist_folder, f"{song}.txt")
            if not os.path.exists(song_file_path):
                # Create text file for the song and write some content (e.g., artist and song name)
                with open(song_file_path, "w", encoding="UTF-8") as song_file:
                    song_file.write(f"Artist: {artist}\nSong: {song}\n")


        
    except Exception as e:#pylint: disable=broad-exception-caught
        print(f"Error saving data {e}")

print("Done")
