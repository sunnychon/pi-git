import sys
import os
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()

cmt_mes = simpledialog.askstring(title="commit",
                                  prompt="type the commit message")
os.system("git commit -m "+cmt_mes)