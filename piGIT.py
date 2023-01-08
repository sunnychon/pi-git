import sys
import os
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("PIGIT - A simple git gui")
        #setting window size
        width=510
        height=390
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_705=tk.Button(root)
        GButton_705["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_705["font"] = ft
        GButton_705["fg"] = "#000000"
        GButton_705["justify"] = "center"
        GButton_705["text"] = "clone"
        GButton_705.place(x=10,y=90,width=382,height=30)
        GButton_705["command"] = self.GButton_705_command

        GButton_671=tk.Button(root)
        GButton_671["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_671["font"] = ft
        GButton_671["fg"] = "#000000"
        GButton_671["justify"] = "center"
        GButton_671["text"] = "commit"
        GButton_671.place(x=10,y=130,width=382,height=30)
        GButton_671["command"] = self.GButton_671_command

        GButton_699=tk.Button(root)
        GButton_699["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_699["font"] = ft
        GButton_699["fg"] = "#000000"
        GButton_699["justify"] = "center"
        GButton_699["text"] = "push"
        GButton_699.place(x=10,y=170,width=382,height=30)
        GButton_699["command"] = self.GButton_699_command

        GButton_786=tk.Button(root)
        GButton_786["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_786["font"] = ft
        GButton_786["fg"] = "#000000"
        GButton_786["justify"] = "center"
        GButton_786["text"] = "login"
        GButton_786.place(x=10,y=10,width=381,height=67)
        GButton_786["command"] = self.GButton_786_command

        GButton_739=tk.Button(root)
        GButton_739["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_739["font"] = ft
        GButton_739["fg"] = "#000000"
        GButton_739["justify"] = "center"
        GButton_739["text"] = "exit"
        GButton_739.place(x=10,y=210,width=382,height=30)
        GButton_739["command"] = self.GButton_739_command

        GButton_921=tk.Button(root)
        GButton_921["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_921["font"] = ft
        GButton_921["fg"] = "#dd1717"
        GButton_921["justify"] = "center"
        GButton_921["text"] = "PI GIT v0.1.0"
        GButton_921.place(x=400,y=10,width=99,height=71)
        GButton_921["command"] = self.GButton_921_command

    def GButton_705_command(self):
        os.system("python clone.py")


    def GButton_671_command(self):
        os.system("python commit.py")


    def GButton_699_command(self):
        os.system("git push")


    def GButton_786_command(self):
        os.system("python log.py")


    def GButton_739_command(self):
        exit()


    def GButton_921_command(self):
        os.system("python info.py")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
