#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import Tkinter as Tk
import tkMessageBox

# root.mainloop()
# root.withdraw()


def show_info(title, message):
    # root = Tk()
    # var = StringVar()
    # msg_w = Message(root, textvariable=var, relief=RAISED)
    # var.set(message)
    # msg_w.pack()

    # tkinter.messagebox.showinfo("FishC Demo", "2017新年快乐")
    tkMessageBox.showinfo(title=title, message=message)

    # root.mainloop()
    # root.withdraw()


def show_info_middle(title, message):
    root = Tk.Tk()

    width = 200
    height = 180
    # screen width and height
    width_screen = root.winfo_screenwidth()  # width of the screen
    height_screen = root.winfo_screenheight()  # height of the screen

    print width_screen, height_screen

    # calculate shift pixes
    x = (width_screen - width) // 2
    y = (height_screen - height) // 2

    print x, y
    # width, height of screen, the location of the left corner of the window
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    var = Tk.StringVar()

    msg_w = Tk.Message(root, textvariable=var, relief=Tk.RAISED)
    msg_w.pack(expand=True, fill="x")
    msg_w.bind("<Configure>", lambda e: msg_w.configure(width=e.width - 10))
    msg_w.config(font=("Courier", 10))

    var.set(message)

    root.mainloop()
    # root.withdraw()


def show_info_middle_2(title, message):
    root = Tk.Tk()

    width = 200
    height = 180
    # screen width and height
    width_screen = root.winfo_screenwidth()  # width of the screen
    height_screen = root.winfo_screenheight()  # height of the screen

    # calculate shift pixes
    x = (width_screen - width) // 2
    y = (height_screen - height) // 2

    # width, height of screen, the location of the left corner of the window
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    msg_w = Tk.Message(text=message)
    # 2 lines below modify the format
    msg_w.pack(expand=True, fill="x")
    msg_w.bind("<Configure>", lambda e: msg_w.configure(width=e.width - 10))
    msg_w.config(font=("Courier", 10))

    root.mainloop()
    # root.withdraw()


if __name__ == "__main__":
    # show_info("alert", "This is a test")
    # show_info_middle("alert", "This is a test")
    show_info_middle_2("alert", "This is a test")
