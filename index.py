from visualiser import adder
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from tkinter import messagebox

import os

root = Tk()

filepath=""


root.title("STL Visualiser")
root.geometry('350x200')


lbl = Label(root, text = "STL File:")
lbl.grid()
res=Label(root)
res.grid(column=1,row=0)


btn1 = Button(root, text ='Select File', command = lambda:open_file())
btn1.grid(column=2, row=0)
btn = Button(root, text = "Visualise" , fg = "red", command=lambda:indexfunc())
btn.grid(column=3, row=0)



def open_file():
	print("file selected")
	file = filedialog.askopenfile(mode='r', filetypes=[('STL Files', '*.stl')])
	if file:
		global filepath
		filepath = os.path.abspath(file.name)
		res.config(text=filepath)
		
		
def indexfunc():
	if filepath=="":
		error()
	else:
		print("button pressed")
		x=filepath
		print("values accessed")
		print(x)
		adder(x)

def error():
	print("File not selected")
	messagebox.showerror('STL Visualiser Error', 'Error: Please select the file first!')
	
root.mainloop()