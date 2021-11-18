#import the mysql
import csv
from mysql import connector
def scanInput():
    print("Please Choose what table to insert values: \n")
    scanner =input("(1)Crew (2)AKAS (3)Episodes (4)People   (5)Ratings  (6)Titles\n")
    return scanner
def tableChosen(inputNum):
    switcher = {
        1: "crew",
        2: "akas",
        3: "episodes",
        4: "people",
        5: "ratings",
        6: "titles",
            }
    return switcher.get(inputNum,"error")
def connectToDatabase():
    cnx = connector.connect(user= 'root', password = 'comp420', host= '54.174.186.225',database = 'imdb')
    cursor =cnx.cursor()
    #ask user what table they want to choose to insert csv
    usrInput = tableChosen(int(scanInput()))
    usr_file = input("Please type name of csv file")
    #open the csv file
    print(usr_file)
    with open(usr_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            query = ("INSERT INTO "+usrInput+" VALUES("+str(row)[1:-1]+")")
            try:
                cursor.execute(query)
            except (connector.errors.DataError, connector.Warning) as e:
                print("Error inserting Line ")
            print(query)
    #closing session
    cnx.close()
connectToDatabase()
