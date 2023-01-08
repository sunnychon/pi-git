import sys
import os
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()

usr_nam = simpledialog.askstring(title="login",
                                  prompt="type your username of github")
os.system("git config --global user.name "+usr_nam)

from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()

usr_email = simpledialog.askstring(title="login",
                                  prompt="type your email of github")
os.system("git config --global user.email "+usr_email)

from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()

usr_paswd = simpledialog.askstring(title="Test",
                                  prompt="type your password of github(or access)")
os.system("git config --global user.password "+usr_paswd)

