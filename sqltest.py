import pyodbc
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Line, String
import time

canvas_test = canvas.Canvas('databasetest1.pdf', pagesize=letter)
width, height = letter


default_horizontal = 50
default_height = 750
transformed_height = 725


server = 'testseating.database.windows.net'
database = 'Test SQL Seating '
username = 'nstern'
password = 'Nat30119!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def test():
    global transformed_height
    global default_horizontal
    global default_height

    canvas_test.drawString(default_horizontal, default_height, "All Entries:")
    canvas_test.line(default_horizontal, default_height - 2, default_horizontal + 57, default_height - 2)

    cursor.execute("SELECT name_first, name_last, house_sitting, grade_sitting FROM test1 WHERE house LIKE '%Harper%';")
    row = cursor.fetchone()
    while row:
    #print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]) + " "+ str(row[6]))
        #print(str(row))
        canvas_test.drawString(default_horizontal, transformed_height, str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
        row = cursor.fetchone()
        transformed_height -=25

    canvas_test.save()

test()