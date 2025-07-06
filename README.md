# MyPass: Password Manager App

A simple password manager built with Python's Tkinter GUI library.  
Features:
- Generate strong passwords  
- Save credentials securely in a JSON file  
- Search saved passwords by website  
- Copy password to clipboard automatically

## How to Run

1. Make sure you have Python installed (tested on 3.8+).  
2. Install `pyperclip` via `pip install pyperclip`.  
3. Run `password_manager.py` with `python password_manager.py`.  
4. The UI window will open, and you can use the app.

## Notes

- The app saves passwords in `data.json` locally.  
- Keep your `data.json` secure, as it stores passwords unencrypted.
- The project is for learning and personal use only.

## Used Modules & Dependencies

- tkinter — Built-in Python library for creating the GUI interface. No installation needed.

- random — Built-in Python module used for generating random characters in passwords.

- pyperclip — External module used to copy generated passwords automatically to the clipboard.
  Install it via running this command in your powershell "pip install pyperclip"

