# www.tkdocs.com/tutorial/firstexample.html

#tells python that we need the modlues tkinter and ttk
# tkinter is the standard binding to Tk (what is a binding?)
# ttk is Python's binding to the newer themed widgets that were added to 8.5
from tkinter import *
from tkinter import ttk
#calculate procedure
def calculate(*args):
	try: 
		#feet is the text variables
		value = float(feet.get())
		meters.set ((0.3048 * value * 10000.0 + 0.5)/10000.0)
	except ValueError:
		pass

root = Tk()
root.title("Feet to Meters") # gives window title feet to meters

#creates frame widget
mainframe = ttk.Frame(root, padding= "3 3 12 12")
mainframe.grid (column= 0, row = 0, sticky = (N, W, E, S))
# tells tkinker that if the main window is resized, the frame should expand to take up the extra space
mainframe.columnconfigure (0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

#create three widgets in program: entry to feet, a label, and the button
#do two things for a widget:
	#1. create widget 2. put it on the screen
#all 3 widgets are children of content window
# the .grid parts places them in the screen
#sticky option says how to line up in cell

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe,width = 7, textvariable = feet)
feet_entry.grid (column = 2, row =1, sticky = (W, E))

ttk.Label(mainframe, textvariable = meters).grid (column = 2, row=2, stick = (W, E))
ttk.Button(mainframe, text = "Calculate", command = calculate).grid(column=3, row = 3, sticky = W)

ttk.Label(mainframe, text = 'feet').grid (column = 3, row =1, sticky = W)
ttk.Label(mainframe, text = "is equivalent to").grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = "meters"). grid(column = 3, row = 2, sticky = W)


#finishing touches
#this line walks through all of the widgets that are children and add a bit of padding
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# cursor starts in feet intry
feet_entry.focus()

#when enter button is presed, it calls calculate
root.bind("<Return>", calculate)
#tells tk to enter event loop which makes everthing run
root.mainloop()