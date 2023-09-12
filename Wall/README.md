# Wallpaper Automation with Python 🖼️

## Installation ⚙️

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

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage 🚀

1. **Configure the Script:**
   - Open the `script.py` file in a text editor.
   - Modify these variables:
     - `wallpaper_directory`: Set to the path of your wallpaper images.
     - `screen_width` and `screen_height`: Adjust to match your screen resolution.

2. **Run the Script:**
   ```bash
   python script.py
   ```

3. **Logs:**
   - Actions are logged to `logfile.log`.
   - View the log file to check for issues or see which wallpapers were set.

## Customization 🎨

- Customize the script further by modifying the image directory, resolution, or scheduling intervals.

## Troubleshooting ❓

If you encounter any issues, please refer to the troubleshooting section in the script. Common issues and their solutions are mentioned there.

## Scheduling with `cron` ⏰

1. **Edit the `crontab` File:**
   ```bash
   crontab -e
   ```

2. **Add a `cron` Job:**
   Add this line to run the script every minute:
   ```bash
   * * * * * /usr/bin/python3 /path/to/your/script.py >> /path/to/your/logfile.log 2>&1
   ```
   - Replace `/usr/bin/python3` with your Python interpreter path.
   - Replace `/path/to/your/script.py` with your script's path.
   - Replace `/path/to/your/logfile.log` with your log file's path.

3. **Save and Exit.**

Now, your Python script will change the wallpaper every minute.

## Contributing 🤝

If you'd like to contribute, open an issue or submit a pull request on the [PixelScape Repository](https://github.com/bytecanvas/PixelScape).

That's it! You now have a wallpaper automation script, changing your wallpaper at regular intervals. 🎉
```
