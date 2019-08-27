#!/usr/bin/pythonw

import pyodbc
from fpdf import FPDF

pdf = FPDF()
#pdf.add_page()
pdf.set_font('Arial', 'U', 16)
#pdf.cell(40, 10, 'Entries:', ln=1)
pdf.set_auto_page_break(True, 2.0)

server = 'testseating.database.windows.net'
database = 'Test SQL Seating '
username = 'nstern'
password = 'lccLions!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
#cursor.execute("SELECT name_first, name_last, house_sitting, grade_sitting FROM test1;")
#row = cursor.fetchone()

#pdf.set_font('Arial', 'UB', 14)
#pdf.cell(45, 10, 'First Name', border=1, ln=0)
#pdf.cell(45, 10, 'Last Name', border=1, ln=0)
#pdf.set_font('Arial', 'UB', 12)
#pdf.cell(45, 10, 'House Sitting With', border=1, ln=0)
#pdf.cell(45, 10, 'Grade Sitting With', border=1, ln=1)
#pdf.set_font('Arial', '', 12)

#while row:
#    pdf.cell(45, 10, str(row[0]), border=1, ln=0)
#    pdf.cell(45, 10, str(row[1]), border=1, ln=0)
#    pdf.cell(45, 10, str(row[2]), border=1, ln=0)
#    pdf.cell(45, 10, str(row[3]), border=1, ln=1)
#    row = cursor.fetchone()

def lookup(grade_sitting, house_sitting):
    query = "SELECT name_first, name_last, house, grade FROM test1 WHERE house_sitting LIKE '%" + house_sitting + "%' AND grade_sitting LIKE '%" + str(grade_sitting) + "%';"
    pdf.add_page()
    pdf.set_font('Arial', 'U', 16)
    pdf.cell(40, 10, str(house_sitting) + " " + str(grade_sitting) + ": ", ln=1)
    pdf.set_font('Arial', 'UB', 14)
    pdf.cell(45, 10, 'First Name', border=1, ln=0)
    pdf.cell(45, 10, 'Last Name', border=1, ln=0)
    pdf.cell(45, 10, 'House', border=1, ln=0)
    pdf.cell(45, 10, 'Grade', border=1, ln=1)
    pdf.set_font('Arial', '', 12)

    cursor.execute(query)
    row = cursor.fetchone()
    while row:
        pdf.cell(45, 10, str(row[0]), border=1, ln=0)
        pdf.cell(45, 10, str(row[1]), border=1, ln=0)
        pdf.cell(45, 10, str(row[2]), border=1, ln=0)
        pdf.cell(45, 10, str(row[3]), border=1, ln=1)
        row = cursor.fetchone()

lookup("9", "Beveridge")
lookup("9", "Claxton")
lookup("9", "Drummond")
lookup("9", "French")
lookup("9", "Harper")
lookup("9", "Heward")
lookup("9", "Russel")
lookup("9", "Woods")
lookup("10", "Beveridge")
lookup("10", "Claxton")
lookup("10", "Drummond")
lookup("10", "French")
lookup("10", "Harper")
lookup("10", "Heward")
lookup("10", "Russel")
lookup("10", "Woods")
lookup("11", "Beveridge")
lookup("11", "Claxton")
lookup("11", "Drummond")
lookup("11", "French")
lookup("11", "Harper")
lookup("11", "Heward")
lookup("11", "Russel")
lookup("11", "Woods")

pdf.output("seating.pdf")
