# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as ttk
from mysql import connector
cnx = connector.connect(user='root', password='comp420', host='54.174.186.225',
database='PROJECTDB')
cursor = cnx.cursor()
query = ("SELECT PROJECT_MANAGER FROM PROJECT LIMIT 2")
cursor.execute(query)
projectManager1 = ''
for pm in cursor:
    projectManager1=pm
    print("{}\n", pm)
cnx.close()
HEIGHT = 300
WIDTH = 500
root = ttk.Tk()
canvas = ttk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
frame = ttk.Frame(root, bg='#80c1ff')
frame.place(relwidth=1, relheight=1)
button = ttk.Button(frame, text="Test button")
#button.pack(side='left', fill='both', expand=True)
# ttk.Button(root, text="Hello World").grid()
#button.grid(row=0, column=0)
button.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)
label = ttk.Label(frame, text=pm, bg='yellow')
#label.pack(side='left', fill='both')
#label.grid(row=0, column=1)
label.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)
entry = ttk.Entry(frame, bg='green')
#entry.pack()
#entry.grid(row=1, column=2)
entry.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.25)
root.mainloop()
