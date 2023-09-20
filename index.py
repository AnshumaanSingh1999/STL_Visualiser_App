from visualiser import adder
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os

root = Tk()

root.title("Learning Tkinter")
root.geometry('350x200')

num1=StringVar()
num2=StringVar()

lbl = Label(root, text = "STL File:")
lbl.grid()
# txt1 = Entry(root, width=10,textvariable=num1)
# txt1.grid(column =1, row =0)
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
	print("button pressed")
	x=filepath
	print("values accessed")
	print(x)
	r=adder(x)
	# res.config(text=r)
	





root.mainloop()