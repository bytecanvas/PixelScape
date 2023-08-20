import os
import random
import subprocess
from pathlib import Path

def change_wallpaper(directory):
    wallpapers = list(directory.glob('*.jpg')) + list(directory.glob('*.png'))
    if wallpapers:
        selected_wallpaper = random.choice(wallpapers)
        subprocess.run(['feh', '--bg-fill', str(selected_wallpaper)])
    else:
        print("No wallpapers found in the specified directory.")

if __name__ == '__main__':
    wallpaper_directory = Path('/path/to/PixelScape')  # Replace with the actual path
    change_wallpaper(wallpaper_directory)
