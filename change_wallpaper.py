import subprocess
import time
import random
import os
import os
os.environ['DISPLAY'] = ':0.0'  # This assumes your X server is running on display :0.0


def change_wallpaper(wallpaper_folder):
    wallpaper_files = [f for f in os.listdir(wallpaper_folder) if f.endswith(('.jpg', '.png', '.bmp'))]

    if wallpaper_files:
        random_wallpaper = os.path.join(wallpaper_folder, random.choice(wallpaper_files))
        subprocess.run(["feh", "--bg-fill", random_wallpaper])

def main():
    wallpaper_folder = "/home/kernelslinger/Pictures/"  # Change this to your wallpaper folder path
    interval_minutes = 30  # Change this to the desired interval in minutes

    while True:
        change_wallpaper(wallpaper_folder)
        time.sleep(interval_minutes * 60)  # Convert minutes to seconds

if __name__ == "__main__":
    main()
