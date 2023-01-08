import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("PI GIT INFO")
        #setting window size
        width=500
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_525=tk.Button(root)
        GButton_525["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_525["font"] = ft
        GButton_525["fg"] = "#000000"
        GButton_525["justify"] = "center"
        GButton_525["text"] = "back"
        GButton_525.place(x=10,y=340,width=480,height=30)
        GButton_525["command"] = self.GButton_525_command

        GMessage_588=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_588["font"] = ft
        GMessage_588["fg"] = "#333333"
        GMessage_588["justify"] = "center"
        GMessage_588["text"] = "PI GIT 0.1"
        GMessage_588.place(x=0,y=0,width=499,height=34)

        GMessage_266=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_266["font"] = ft
        GMessage_266["fg"] = "#333333"
        GMessage_266["justify"] = "center"
        GMessage_266["text"] = "a simple git gui"
        GMessage_266.place(x=0,y=50,width=499,height=31)

    def GButton_525_command(self):
        exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
