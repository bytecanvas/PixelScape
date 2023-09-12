
### Wallpaper Automation with Python

This Python script allows you to automate wallpaper changes at regular intervals. It randomly selects an image from a specified directory and sets it as your wallpaper.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/bytecanvas/PixelScape.git
   cd PixelScape
   ```

2. **Create a Virtual Environment (Optional):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   Activating the virtual environment is optional but recommended to isolate dependencies.

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Configure the Script:**

   - Open the `script.py` file in a text editor.
   - Modify the following variables to match your setup:

     - `wallpaper_directory`: Set this to the path where your wallpaper images are located.
     - `screen_width` and `screen_height`: Adjust these to match your screen resolution.

2. **Run the Script:**

   - Execute the script using Python:

     ```bash
     python script.py
     ```

   - The script will start changing your wallpaper at the specified intervals.

3. **Logs:**

   - The script logs its actions to a file specified in the `logfile.log` variable.
   - You can view the log file to check for any issues or to see which wallpapers were set.

### Customization

- You can customize the script further by modifying the image directory, resolution, or scheduling intervals as needed.

### Troubleshooting

If you encounter any issues, please refer to the troubleshooting section in the script. Common issues and their solutions are mentioned there.

### Contributing

If you would like to contribute to this project or have any suggestions, feel free to open an issue or submit a pull request on the GitHub repository: [PixelScape Repository](https://github.com/bytecanvas/PixelScape).

That's it! You now have a wallpaper automation script up and running, changing your wallpaper at regular intervals.

* * *

Feel free to replace `/path/to/your/script.py`, `/path/to/your/logfile.log`, and `/path/to/your/wallpaper_directory` with the actual paths you're using.
