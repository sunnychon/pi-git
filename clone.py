import sys
import os
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()

repo_url = simpledialog.askstring(title="clone",
                                  prompt="type the repository url")
os.system("git clone "+repo_url)