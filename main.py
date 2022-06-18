# main window for repair tool

import csv
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from subprocess import call
from PIL import ImageTk, Image
from bit2 import *
from search import *


main = Tk()
main.title("Repair Quick Reference Tool")



app_width = 280
app_height = 150

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

main.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

main.config(bg='#66b2ff')
main.iconbitmap('spec4.ico')

# search button
search_btn = Button(main, text="Search", command = search, fg="white", bg="blue")
search_btn.pack(padx=10, pady=10, ipadx=30)

admin_btn = Button(main, text="Admin",command = admin, bg="grey")
admin_btn.pack(pady=10, padx=10, ipadx=30)


button_quit = Button(main, text="EXIT", command=main.quit, fg="white", bg="red")
button_quit.pack()

main.mainloop()