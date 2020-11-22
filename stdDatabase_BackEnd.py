import sqlite3
#backend

def studentData():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTERGER PRIMARY KEY, StdID text, Firstname text, Surname text, Classroom text, \
        Gender text, Mobile text, School_fees text, Paid_fees text, Remaining_fees text, Status text, Phase text, Date_paid text)")  
    con.commit()
    con.close()

def addStdRec(StdID, Firstname, Surname, Classroom, Gender, Mobile, School_fees, Paid_fees, Remaining_fees, Status ,Phase, Date_paid):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?)", \
                (StdID, Firstname, Surname, Classroom, Gender, Mobile, School_fees, Paid_fees, Remaining_fees, Status ,Phase, Date_paid))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(StdID="", Firstname="", Surname="", Classroom="", Gender="", Mobile="", School_fees="", Paid_fees="", Remaining_fees="", Status="" ,Phase="", Date_paid=""):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE (StdID=? OR Firstname=? OR Surname=?, Classroom=? OR Gender=?, Mobile=? OR School_fees=? OR Paid_fees=? OR Remaining_fees=? OR Status=? OR Phase=? OR Date_paid=? ",(StdID, Firstname, Surname, Classroom, Gender, Mobile, School_fees, Paid_fees, Remaining_fees, Status ,Phase, Date_paid))
    rows=cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,StdID="", Firstname="", Surname="", Classroom="", Gender="", Mobile="", School_fees="", Paid_fees="", Remaining_fees="", Status="" ,Phase="", Date_paid=""):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=?, Firstname=?, Surname=?, Classroom=?, Gender=?, Mobile=?, School_fees=?, Paid_fees=?, Remaining_fees=?, Status=? ,Phase=?, Date_paid=? ",\
              (StdID, Firstname, Surname, Classroom, Gender, Mobile, School_fees, Paid_fees, Remaining_fees, Status ,Phase, Date_paid, id))
    con.commit()
    con.close()
    
studentData()
    
