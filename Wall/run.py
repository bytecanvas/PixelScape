import os
import time
import random
import schedule
import logging
from PIL import Image

# Configure logging to write to a log file
log_file = '/path/to/your/logfile.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Directory where your wallpaper images are located
wallpaper_directory = 'path_to_your_wallpaper_directory'

# Get a list of image files in the directory
image_files = [f for f in os.listdir(wallpaper_directory) if f.endswith(('jpg', 'jpeg', 'png'))]

def change_wallpaper():
    try:
        # Choose a random image from the directory
        random_image = random.choice(image_files)

        # Full path to the selected image
        image_path = os.path.join(wallpaper_directory, random_image)

        # Load the image
        image = Image.open(image_path)

        # Get the screen resolution (you may need to adjust this)
        screen_width, screen_height = 1920, 1080  # Example resolution

        # Resize the image to fit the screen
        image = image.resize((screen_width, screen_height))

        # Set the wallpaper (Linux-specific using feh)
        os.system(f'feh --bg-scale {image_path}')

        # Log a success message
        logging.info(f"Wallpaper changed successfully to {random_image}")

    except Exception as e:
        # Log an error message
        logging.error(f"An error occurred: {str(e)}")

# Schedule wallpaper change every minute
schedule.every(1).minutes.do(change_wallpaper)

while True:
    schedule.run_pending()
    time.sleep(1)
