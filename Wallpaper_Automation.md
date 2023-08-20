Certainly! Here's the full set of instructions in Markdown format for easy copy and paste:

```markdown
# Automatic Wallpaper Changer for Linux

This guide will help you set up an automatic wallpaper changer for your Linux system using the `feh` command-line tool and a Python script.

## Step 1: Install `feh`

If you don't have `feh` installed, you can install it using your package manager. For example, on Ubuntu:

```bash
sudo apt-get install feh
```

## Step 2: Clone the Repository

Clone the wallpaper repository to your local machine:

```bash
git clone https://github.com/bytecanvas/PixelScape.git
```

## Step 3: Create the Python Script

Create a Python script named `change_wallpaper.py` with the following content:

```python
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
```

Replace `/path/to/PixelScape` with the actual path to the cloned repository directory.

## Step 4: Make the Script Executable

Open a terminal and navigate to the directory where you saved the Python script. Run the following command to make the script executable:

```bash
chmod +x change_wallpaper.py
```

## Step 5: Automate Wallpaper Changes with Cron

To automate wallpaper changes, use a cron job:

1. Open your crontab configuration:

```bash
crontab -e
```

2. Add a new line at the end of the file to run the script at a specific interval. For example, to run the script every 30 minutes:

```
*/30 * * * * /path/to/change_wallpaper.py
```

Replace `/path/to/change_wallpaper.py` with the actual path to your Python script.

3. Save the crontab configuration and exit the editor.

Now, the Python script will run at the specified interval and change the wallpaper using the `feh` command-line tool.
```

Just make sure to replace `/path/to/PixelScape` and `/path/to/change_wallpaper.py` with the actual paths on your system.
