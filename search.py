# search function

import csv
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from subprocess import call
from PIL import ImageTk, Image

def search():
	global search

	search_records = Tk()
	search_records.title("Search")
	search_records.geometry("350x250")
	search_records.config(bg='#66b2ff')
	search_records.iconbitmap('spec4.ico')
# entry box search records

	search_box = Entry(search_records, bg="light grey")
	search_box.grid(row=0, column=2, pady=10, padx=10)

	search_box_label = Label(search_records, value=["SELECT problem FROM repairs WHERE unit = %s"], bg='#66b2ff')
	search_box_label.grid(row=0, column=0, pady=10, padx=10)

	drop = ttk.Combobox(search_records, value=["Search by...", "Unit", "Fault"])
	drop.current(0)
	drop.grid(row=0, column=1)

	def search_now():
		global search_now


		sql = ""
		selected = drop.get()
		if selected == "Search by...":
			error = Label(search_records, text="Choose From List.")
			error.grid(row=1, column=2)

		if selected == "Unit":
			sql = "SELECT problem FROM repairs WHERE unit = %s"

		if selected == "Fault":
			sql = "SELECT repair_pro FROM repairs WHERE problem = %s"

		search_now = Toplevel()
		search_now.title("Search Results")
		search_now.geometry("700x500")
		search_now.config(bg='#66b2ff')
		search_now.iconbitmap('spec4.ico')

		con = sqlite3.connect("repair.db")

		c = con.cursor()

		searched = search_box.get()
		sql = "SELECT repair_pro FROM repairs WHERE problem = ?"
		name = (searched, )
		result = c.execute(sql, name)
		result = c.fetchall()
		

		if not result:
			result = "Record Not Found"

			main_frame = Frame(search_now)
			main_frame.pack(fill=BOTH, expand=1)

			my_canvas = Canvas(main_frame)
			my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

			my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
			my_scrollbar.pack(side=RIGHT, fill=Y)

			my_canvas.configure(yscrollcommand=my_scrollbar.set)
			my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion = my_canvas.bbox("all")))

			second_frame = Frame(my_canvas)

			my_canvas.create_window((0,0), window=second_frame, anchor="nw")




			button_quit = Button(second_frame, text="EXIT", command=search_now.destroy, fg="white", bg="blue")
			button_quit.grid(row=0, column=1)

			searched_label = Label(second_frame, text=result)
			searched_label.grid(row=1, column=1)

		else:
			for index, x in enumerate(result):
				num = 0
				index += 2
				
				for y in x:


					main_frame = Frame(search_now)
					main_frame.grid(row=1, rowspan=5, column=0, columnspan=5, pady=(5, 0), sticky='nw')
					my_canvas = Canvas(main_frame)
					my_canvas.grid(row=2, rowspan=5, column=2, columnspan=5, sticky="news")

					my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
					my_scrollbar.grid(row=0, rowspan=5, column=10,  sticky='we')
					
					my_canvas.configure(yscrollcommand=my_scrollbar.set)
					my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion = my_canvas.bbox("all")))

					second_frame = Frame(my_canvas)

					my_canvas.create_window((0,0), window=second_frame, anchor="nw")




					button_quit = Button(second_frame, text="EXIT", command=search_now.destroy, fg="white", bg="blue")
					button_quit.grid(row=0, column=1)

					searched_label = Label(second_frame, text=result)
					searched_label.grid(row=1, column=1)

					num +=1
			
			con.commit()
			con.close()

	# search buttons

	global search_btn
	global button_quit

	search_btn = Button(search_records, text="Search", command=search_now, bg="blue")
	search_btn.grid(row=1, column=1, padx=10, pady=10)

	button_quit = Button(search_records, text="EXIT", command=search_records.destroy, fg="white", bg="red")
	button_quit.grid(row=99, column=1)

