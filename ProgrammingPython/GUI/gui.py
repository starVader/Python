#! /usr/bin/python3
from tkinter import *
from tkinter.messagebox import showerror
import tkinter.messagebox
import shelve
import json
shelvename = 'class-shelve'

bob = {'name':'Bob smith','age':42,'pay':30000,'job':'dev'}
sue = {'name':'Sue jones','age':45,'pay':40000,'job':'hdw'}
tom = {'name':'Tom','age':50,'pay':0000,'job':'None'}

db ={}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom


try:
	with open(shelvename,'w') as pick:
		json.dump(db,pick)
except IOError as ioerr:
	print("File read :" +str(ioerr))


fieldnames = ('name','age','job','pay')

def makeWidgets():
	global entries
	#Make a tikinter window
	window = Tk() 
	#IGve a title to the window
	window.title('Cannabis Types')
	#he Frame widget is very important for the process of grouping and organizing other widgets
	form = Frame(window)
	#This geometry manager organizes widgets in blocks before placing them in the parent widget.
	form.pack()
	entries = {}
	for (ix, label) in enumerate(('key',) +fieldnames):
		lab = Label(form, text=label)#This widget implements a display box where you can place text or images. The text displayed by this widget can be updated at any time you want.
		ent = Entry(form)#The Entry widget is used to accept single-line text strings from a user
		#This geometry manager organizes widgets in a table-like structure in the parent widget
		lab.grid(row =ix,column =0)
		ent.grid(row =ix,column =1)
		entries[label] = ent
	Button(window, text= "Fetch",command = fetchdata).pack(side = LEFT)
	Button(window, text = "Update",command = helloCallBack).pack(side = LEFT)
	Button(window, text ="Quit",command = exitfunc).pack(side = RIGHT)
	return (window)

def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", " :) ")
def exitfunc():
	exit()
def fetchdata():
	key = entries['key'].get()
	print (key)
	try:
		record = db[key]
	except:
		showerror("Key does not exist in Databse") 
	else:
		for field in fieldnames:
			print (field)
			entries[field].delete(0, END)
			entries[field].insert(0, repr(getattr(record,field)))



#db = shelve.open(shelvename, 'rb') as   ####BUGs in bugs.python.org
with open(shelvename,'r') as pick:
	db = json.load(pick)
window = makeWidgets()
window.mainloop()
db.close()


