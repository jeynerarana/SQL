# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as ttk
from mysql import connector
from collections import deque
# from PIL import Image, ImageTk
IMAGE_PATH = '/home/supercoolhackker/PycharmProjects/420Lab10/venv/SQL/guiSQL/7ihdbEc.jpg'
WIDTH, HEIGTH = 900, 1700
# Variables for login
userName =""
password =""
host =""
database = ""


def DeleteSelection(root,tables):
    #destroy the previuos page
    root.destroy()
    query = ("DROP TABLE "+str(tables)[2:-3])
    cursor.execute(query)
    homePage()
def CancelCreate(root):
    backToHome(root)
def ConfirmCreate(root, dbTable,attrName,attrType,attrCollation):
    table = dbTable.get(1.0,"end-1c")
    name = attrName.get(1.0,"end-1c")
    type = attrType.get(1.0, "end-1c")
    collation = attrCollation.get(1.0, "end-1c")

    row1 = ("CREATE TABLE "+table+" ("+name+" "+type+");")
    cursor.execute(row1)
    backToHome(root)

def CreateTable(prevroot):
    prevroot.destroy()
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
    label = ttk.Label(frame, text="Selected Database :"+database, bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.2, rely=0.2, relwidth=0.18, relheight=0.07)

    # add Text/Label for table name
    tableNameText = ttk.Text(root, height=1, width=30)
    tableNameText.pack()
    tableNameText.place(relx=0.35, rely=0.28)

    #Name
    attrName = ttk.Text(root, height=1, width=20)
    attrName.pack()
    attrName.place(relx=0.25, rely=0.40)

    attrNamelabel= ttk.Label(frame, text="Name: ", bg='grey')
    attrNamelabel.pack(side='left', fill='both')
    attrNamelabel.grid(row=0, column=1)
    attrNamelabel.place(relx=0.25, rely=0.35, relwidth=0.08, relheight=0.03)

    #Type
    attrType = ttk.Text(root, height=1, width=20)
    attrType.pack()
    attrType.place(relx=0.40, rely=0.40)

    attrTypelabel= ttk.Label(frame, text="Type: ", bg='grey')
    attrTypelabel.pack(side='left', fill='both')
    attrTypelabel.grid(row=0, column=1)
    attrTypelabel.place(relx=0.40, rely=0.35, relwidth=0.08, relheight=0.03)
    #Collation
    attrCollation = ttk.Text(root, height=1, width=20)
    attrCollation.pack()
    attrCollation.place(relx=0.55, rely=0.40)

    attrCollationlabel= ttk.Label(frame, text="Collation: ", bg='grey')
    attrCollationlabel.pack(side='left', fill='both')
    attrCollationlabel.grid(row=0, column=1)
    attrCollationlabel.place(relx=0.55, rely=0.35, relwidth=0.08, relheight=0.03)

    # This label will match the table name text
    tableNamelabel= ttk.Label(frame, text="Table name: ", bg='white')
    tableNamelabel.pack(side='left', fill='both')
    tableNamelabel.grid(row=0, column=1)
    tableNamelabel.place(relx=0.23, rely=0.28, relwidth=0.09, relheight=0.03)
    #counts the loop
    count = 0
    # allocButton(queue)
    #These last Texts will be control the tabel attributes

    #Add dropr or cancel buttons
    cancelBtn =ttk.Button(frame, text="Cancel", bg='red',command=lambda:CancelCreate(root))
    cancelBtn.pack(side='left', fill='both')
    cancelBtn.grid(row=0, column=0)
    cancelBtn.place(relx=0.355, rely=0.8, relwidth=0.07, relheight=0.07)
    dropBtn = ttk.Button(frame, text="ADD", bg='green', command = lambda:ConfirmCreate(root,tableNameText,attrName,attrType,attrCollation))
    dropBtn.pack(side='left', fill='both')
    dropBtn.grid(row=0, column=0)
    dropBtn.place(relx=0.55, rely=0.8, relwidth=0.07, relheight=0.07)

def ReadTable(root,table,rx,ry,rwidth,rheight,count):
    for pm in table:
            print(range(len(pm)))
            for c in range(len(pm)):
                dropText = ttk.Text(root, height=2, width=30)
                dropText.pack(side='left', fill='x')
                dropText.insert(ttk.END, pm[c])
                dropText.place(relx=rx, rely=ry, relwidth=rwidth/len(pm), relheight=rheight)

                rx += 0.2
            rx = 0.1
            ry += 0.1
    count += 5
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
    label = ttk.Label(frame, text="Selected Table :"+str(tables)[2:-3], bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.2, rely=0.2, relwidth=0.18, relheight=0.07)
    #Add dropr or cancel buttons
    cancelBtn =ttk.Button(frame, text="Cancel", bg='green', command=lambda: allocButton(tables, root, frame, canvas,5))
    cancelBtn.pack(side='left', fill='both')
    cancelBtn.grid(row=0, column=0)
    cancelBtn.place(relx=0.355, rely=0.5, relwidth=0.07, relheight=0.07)
    dropBtn = ttk.Button(frame, text="Drop", bg='red', command=lambda: DeleteSelection(root,tables))
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
def allocButton(tables, prevroot,frame,canvas,prevcount):
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
    #Label fro chosen database
    labeldb = ttk.Label(frame, text="Selected Database :"+database, bg='purple')
    labeldb.pack(side='left', fill='both')
    labeldb.grid(row=0, column=1)
    labeldb.place(relx=0.1, rely=0.20, relwidth=0.2, relheight=0.05)
    # label for table
    label = ttk.Label(frame, text="Selected Table :"+str(tables)[2:-3], bg='yellow')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.1, rely=0.25, relwidth=0.2, relheight=0.03)
    #counts the loop
    count = prevcount
    # buttons for browse
    queuestr = "Browse"
    # allocButton(queue)
    #adding scrollbar

    ## execute query
    query = ("SELECT * FROM "+str(tables)[2:-3])
    cursor.execute(query)
    records = cursor.fetchmany(count)
    #ReadTable(root, records,rx,ry, rwidth,rheight,count)
    records = records[count-5:count]
    for pm in records:
            print(range(len(pm)))
            for c in range(len(pm)):
                dropText = ttk.Text(root, height=2, width=30)
                dropText.pack(side='left', fill='x')
                dropText.insert(ttk.END, pm[c])
                dropText.place(relx=rx, rely=ry, relwidth=rwidth/len(pm), relheight=rheight)

                rx += 0.2
            rx = 0.1
            ry += 0.1
    print(records[count-5:count])
    # count += 5
    #Make the back button
    backBtn =ttk.Button(frame, text="Back", bg='grey', command=lambda: backToHome(root))
    backBtn.pack(side='left', fill='both')
    backBtn.grid(row=0, column=0)
    backBtn.place(relx=0.1, rely=0.1, relwidth=0.07, relheight=0.07)
    # Make the Next Button
    nextBtn = ttk.Button(frame, text =">>", bg="grey", command=lambda c=count+5 :allocButton(tables, root,frame,canvas,c))
    nextBtn.pack(side='left', fill='both')
    nextBtn.grid(row=0, column=0)
    nextBtn.place(relx=0.875, rely=0.1, relwidth=0.07, relheight=0.07)
    # Make the Next Button
    # TODO
    nextBtn = ttk.Button(frame, text ="<<", bg="grey", command=lambda:backToHome(root))
    nextBtn.pack(side='left', fill='both')
    nextBtn.grid(row=0, column=0)
    nextBtn.place(relx=0.805, rely=0.1, relwidth=0.07, relheight=0.07)

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
    # Fixe the static variable 'imdb'
    label = ttk.Label(frame, text="Selected Database :"+database, bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.2, rely=0.2, relwidth=0.3, relheight=0.07)
    #counts the loop
    count = 0
    # execute quey
    query = ("SHOW TABLES;")
    cursor.execute(query)
    # making a button for creating new Table
    createTableBttn = ttk.Button(frame, text="Create New Table",bg='cyan', command=lambda:CreateTable(root))
    createTableBttn.pack(side='left', fill='both')
    createTableBttn.grid(row=0, column=0)
    createTableBttn.place(relx=0.9, rely=0.1, relwidth=0.1, relheight=0.08)
    for pm in cursor:
        label = ttk.Label(frame, text=pm, bg='white')
        label.pack(side='left', fill='both')
        label.grid(row=0, column=1)
        label.place(relx=rx, rely=ry, relwidth=rwidth, relheight=rheight)
        # Declaring deque
        # for browsing button
        queue = deque([ttk.Button(frame, text="Browse", bg='green', command=lambda j =pm: allocButton(j,root,frame,canvas,5))])
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
    #Make the back button
    backBtn =ttk.Button(frame, text="Back", bg='grey', command=lambda: goToDB(root))
    backBtn.pack(side='left', fill='both')
    backBtn.grid(row=0, column=0)
    backBtn.place(relx=0.1, rely=0.1, relwidth=0.07, relheight=0.07)
    root.mainloop()
def setDB(db,root):
    root.destroy()
    global database
    if database =="":
        database =str(db)[2:-3]
    if database =="NA":
        database = str(db)[2:-3]
        cnx = connector.connect(user=userName, password=password, host=host,database=str(db)[2:-3])
        cursor = cnx.cursor(buffered=True)
        # query to show databeases
        query = ("SHOW TABLES;")
        # query =("show databases;")
        cursor.execute(query)
        homePage()
        print(database)
def goToDB(root):
    global database
    root.destroy()
    database = "NA"
    chooseDB()
# This page display the available databases if you don;t type a database
def chooseDB():
    try:
        # execute quey
        HEIGHT = 900
        WIDTH = 1700
        # local vars
        rx = 0.35
        ry = 0.3
        rwidth = 0.4
        rheight = 0.07
        root = ttk.Tk()
        canvas = ttk.Canvas(root, height=HEIGHT, width=WIDTH)
        canvas.pack()
        frame = ttk.Frame(root, bg='#80c1ff')
        frame.place(relwidth=1, relheight=1)
        cnx = connector.connect(user=userName, password=password, host=host)
        cursor = cnx.cursor(buffered=True)
        query = ("SHOW DATABASES;")
        cursor.execute(query)
        for pm in cursor:
            # # Declaring deque
            # # for browsing button
            # queue = deque([ttk.Button(frame, text=pm, bg='green', command=lambda i =pm:setDB(i,root))])
            # queue[0].pack(side='left', fill='both')
            # queue[0].grid(row=0, column=0)
            # queue[0].place(relx=rx + 0.45, rely=ry, relwidth=(rwidth / 3), relheight=rheight)
            # queue.append(queue[0])
            # ry += 0.1

            for c in range(len(pm)):
                # Declaring deque
                # for browsing button
                queue = deque([ttk.Button(frame, text=pm, bg='green', command=lambda i=pm: setDB(i, root))])
                queue[0].pack(side='left', fill='both')
                queue[0].grid(row=0, column=0)
                queue[0].place(relx=rx, rely=ry, relwidth=(rwidth /len(pm)), relheight=rheight)
                queue.append(queue[0])
                rx += 0.2
            rx = 0.35
            ry += 0.1
    except(connector.errors.InterfaceError, connector.Warning) as e:
        print("Error signing in")
        return

def signInfo(usrText,passText,hostText,databaseText,root):
    global userName, password,host,database
    userName = usrText.get(1.0, "end-1c")
    password = passText.get(1.0,"end-1c")
    host = hostText.get(1.0,"end-1c")
    if (databaseText.get(1.0,"end-1c")==""):
        chooseDB()
    else:database = databaseText.get(1.0,"end-1c")
    root.destroy()
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
    label.place(relx=0.2, rely=0.2, relwidth=0.20, relheight=0.07)

    # User Text
    usrText = ttk.Text(root, height=1, width=30)
    usrText.pack()
    usrText.place(relx=0.5, rely=0.28)
    label = ttk.Label(frame, text="UserName: ", bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.40, rely=0.28, relwidth=0.09, relheight=0.025)
    # Password Text
    passText = ttk.Text(root, height=1, width=30)
    passText.pack()
    passText.place(relx=0.5, rely=0.34)
    label = ttk.Label(frame, text="Password: ", bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.40, rely=0.34, relwidth=0.09, relheight=0.025)
    # Host Text
    hostText = ttk.Text(root, height=1, width=30)
    hostText.pack()
    hostText.place(relx=0.5, rely=0.38)
    label = ttk.Label(frame, text="Host: ", bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.40, rely=0.38, relwidth=0.09, relheight=0.025)
    # database Text
    databaseText = ttk.Text(root, height=1, width=30)
    databaseText.pack()
    databaseText.place(relx=0.5, rely=0.42)
    label = ttk.Label(frame, text="Database: ", bg='purple')
    label.pack(side='left', fill='both')
    label.grid(row=0, column=1)
    label.place(relx=0.40, rely=0.42, relwidth=0.09, relheight=0.025)
    #print what the user typed

    #Add sign in btn
    signInBtn =ttk.Button(frame, text="Sign In", bg='green', command=lambda:signInfo(usrText,passText,hostText,databaseText,root))
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
    # Checking if there are errors while connecting with given credentials
    try:
        cnx = connector.connect(user=userName, password=password, host=host,
        database=database)
    except(connector.errors.DatabaseError, connector.Warning) as e:
        print("Sorry looks like you have invalid credentials: Please make sure there are no spaces")
    # cnx = connector.connect(user='root', password='comp420', host='54.174.186.225',database='imdb')
    cursor = cnx.cursor(buffered=True)
    #query to show databeases
    query = ("SHOW TABLES;")
    #query =("show databases;")
    cursor.execute(query)
    # for (databases) in cursor:
    #     print(databases[0])
    homePage()
    #cnx.close()

