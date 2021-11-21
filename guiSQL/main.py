# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as ttk
from mysql import connector
from collections import deque
from PIL import Image, ImageTk
IMAGE_PATH = '/home/supercoolhackker/PycharmProjects/420Lab10/venv/SQL/guiSQL/7ihdbEc.jpg'
WIDTH, HEIGTH = 900, 1700
userName =""
password =""
host =""
database = ""


def DeleteSelection():
    print("BYE, BYE")
def CreateTable():
    return 0
def ReadTable(table):
    print(table)
def UpdateTable():
    return 0
def DeleteTable(tables, root,frame,canvas):
    root.destroy()
    HEIGHT = 900
    WIDTH = 1700
    #local vars
    rx = 0.2
    ry = 0.3
    rwidth = 0.4
    rheight = 0.07
    root = ttk.Tk()
    canvas = ttk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()
    frame = ttk.Frame(root, bg='#80c1ff')
    frame.place(relwidth=1, relheight=1)
    # label for databes in
    label = ttk.Label(frame, text="Selected Database :", bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.2, rely=0.2, relwidth=0.18, relheight=0.07)
    #Add dropr or cancel buttons
    cancelBtn =ttk.Button(frame, text="Cancel", bg='green', command=lambda: allocButton(tables, root, frame, canvas))
    cancelBtn.pack(side='left', fill='both')
    cancelBtn.grid(row=0, column=0)
    cancelBtn.place(relx=0.355, rely=0.5, relwidth=0.07, relheight=0.07)
    dropBtn = ttk.Button(frame, text="Drop", bg='red', command=lambda: backToHome(root))
    dropBtn.pack(side='left', fill='both')
    dropBtn.grid(row=0, column=0)
    dropBtn.place(relx=0.55, rely=0.5, relwidth=0.07, relheight=0.07)
    # add Text
    dropText = ttk.Text(root, height=2, width=30)
    dropText.pack()
    dropText.insert(ttk.END, "Are you sure you want to drop table: ")
    dropText.place(relx=0.35, rely=0.28)
    #counts the loop
    count = 0
    # allocButton(queue)
    ## execute query
def allocButton(tables, prevroot,frame,canvas):
    # destroys prevoius root
    prevroot.destroy()
    HEIGHT = 900
    WIDTH = 1700
    #local vars
    rx = 0.1
    ry = 0.3
    rwidth = 1
    rheight = 0.07
    root = ttk.Tk()
    canvas = ttk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()
    frame = ttk.Frame(root, bg='#80c1ff')
    frame.place(relwidth=1, relheight=1)
    # label for databes in
    label = ttk.Label(frame, text="Selected Table :"+str(tables)[2:-3], bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.1, rely=0.2, relwidth=0.4, relheight=0.07)
    #counts the loop
    count = 0
    # buttons for browse
    queuestr = "Browse"
    # allocButton(queue)
    #adding scrollbar

    ## execute query
    query = ("SELECT * FROM "+str(tables)[2:-3])
    cursor.execute(query)
    records = cursor.fetchmany(5)
    for pm in records:
            print(range(len(pm)))
            for c in range(len(pm)):
                # label = ttk.Label(frame, text=pm[c], bg='white')
                # label.pack(side='left', fill='x')
                # label.grid(row=0, column=1)
                # label.place(relx=rx, rely=ry, relwidth=rwidth/len(pm), relheight=rheight)
                dropText = ttk.Text(root, height=2, width=30)
                dropText.pack(side='left', fill='x')
                dropText.insert(ttk.END, pm[c])
                dropText.place(relx=rx, rely=ry, relwidth=rwidth/len(pm), relheight=rheight)

                rx += 0.2
            rx = 0.1
            ry += 0.1
            count +=1
        # if count == 5:
        #     break
    #Make the back button
    backBtn =ttk.Button(frame, text="Back", bg='grey', command=lambda: backToHome(root))
    backBtn.pack(side='left', fill='both')
    backBtn.grid(row=0, column=0)
    backBtn.place(relx=0.1, rely=0.1, relwidth=0.07, relheight=0.07)

    # labels for first buttons
#    root.mainloop()
#    cnx.close()
def backToHome(root):
    root.destroy()
    homePage()

def homePage():
    HEIGHT = 900
    WIDTH = 1700
    #local vars
    rx = 0.2
    ry = 0.3
    rwidth = 0.4
    rheight = 0.07
    root = ttk.Tk()
    canvas = ttk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()
    # TODO
    # img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
    # canvas.background = img  # Keep a reference in case this code is put in a function.
    # bg = canvas.create_image(0, 0, anchor=ttk.NW, image=img)
    frame = ttk.Frame(root, bg='#80c1ff')
    frame.place(relwidth=1, relheight=1)
    # label for databes in
    label = ttk.Label(frame, text="Selected Database : imdb", bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.2, rely=0.2, relwidth=0.3, relheight=0.07)
    #counts the loop
    count = 0
    # execute quey
    query = ("SHOW TABLES;")
    cursor.execute(query)
    for pm in cursor:
        label = ttk.Label(frame, text=pm, bg='white')
        label.pack(side='left', fill='both')
        label.grid(row=0, column=1)
        label.place(relx=rx, rely=ry, relwidth=rwidth, relheight=rheight)
        # Declaring deque
        # queue.append(ttk.Button(frame, text=queuestr, bg='red', command= lambda j=pm:allocButton(j)))
        # for browsing button
        queue = deque([ttk.Button(frame, text="Browse", bg='green', command=lambda j =pm: allocButton(j,root,frame,canvas))])
        queue[0].pack(side='left', fill='both')
        queue[0].grid(row=0, column=0)
        queue[0].place(relx=rx + 0.45, rely=ry, relwidth=(rwidth / 3), relheight=rheight)
        queue.append(queue[0])
        # for Drop button
        dropBtn = deque([ttk.Button(frame, text="Drop", bg='red', command=lambda j =pm: DeleteTable(j,root,frame,canvas))])
        dropBtn[0].pack(side='left', fill='both')
        dropBtn[0].grid(row=0, column=0)
        dropBtn[0].place(relx=rx + 0.6, rely=ry, relwidth=(rwidth / 3), relheight=rheight)
        dropBtn.append(queue[0])

        print(pm)
        ry += 0.1
        count += 1
    # allocButton(queue)
    root.mainloop()
def signInfo(usrText,passText,hostText,databaseText,root):
    global userName, password,host,database
    userName = usrText.get(1.0, "end-1c")
    password = passText.get(1.0,"end-1c")
    host = hostText.get(1.0,"end-1c")
    database = databaseText.get(1.0,"end-1c")
    root.destroy()
    #return usr,ppass,host,database
def loginPage(): #TODO
    HEIGHT = 900
    WIDTH = 1700
    #local vars
    rx = 0.2
    ry = 0.3
    rwidth = 0.4
    rheight = 0.07
    root = ttk.Tk()
    canvas = ttk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()
    frame = ttk.Frame(root, bg='#80c1ff')
    frame.place(relwidth=1, relheight=1)
    # label for databes in
    label = ttk.Label(frame, text="Please sign in to MySQL: ", bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.2, rely=0.2, relwidth=0.18, relheight=0.07)

    # User Text
    usrText = ttk.Text(root, height=1, width=30)
    usrText.pack()
    usrText.place(relx=0.5, rely=0.28)
    label = ttk.Label(frame, text="UserName: ", bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.45, rely=0.28, relwidth=0.05, relheight=0.02)
    # Password Text
    passText = ttk.Text(root, height=1, width=30)
    passText.pack()
    passText.place(relx=0.5, rely=0.34)
    label = ttk.Label(frame, text="Password: ", bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.45, rely=0.34, relwidth=0.05, relheight=0.02)
    # Host Text
    hostText = ttk.Text(root, height=1, width=30)
    hostText.pack()
    hostText.place(relx=0.5, rely=0.38)
    label = ttk.Label(frame, text="Host: ", bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.45, rely=0.38, relwidth=0.05, relheight=0.02)
    # database Text
    databaseText = ttk.Text(root, height=1, width=30)
    databaseText.pack()
    databaseText.place(relx=0.5, rely=0.42)
    label = ttk.Label(frame, text="Database: ", bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.45, rely=0.42, relwidth=0.05, relheight=0.02)
    #print what the user typed

    #Add dropr or cancel buttons
    signInBtn =ttk.Button(frame, text="Sign In", bg='green', command=lambda :signInfo(usrText,passText,hostText,databaseText,root))
    signInBtn.pack(side='left', fill='both')
    signInBtn.grid(row=0, column=0)
    signInBtn.place(relx=0.55, rely=0.5, relwidth=0.07, relheight=0.07)
    root.mainloop()

if __name__ == '__main__':
    HEIGHT = 700
    WIDTH = 700
    #the first login page
    loginPage()
    print(userName+password+host+database)
    cnx = connector.connect(user=userName, password=password, host=host,
    database=database)
    # cnx = connector.connect(user='root', password='comp420', host='54.174.186.225',
    # database='imdb')
    cursor = cnx.cursor(buffered=True)
    #query to show databeases
    query = ("SHOW TABLES;")
    cursor.execute(query)
    homePage()
    #cnx.close()

