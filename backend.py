import sqlite3

def connect():
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, section TEXT, roll INTEGER, branch TEXT)")
    con.commit()
    con.close()

def insert(name,section,roll,branch):
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute("INSERT INTO students values (NULL,?,?,?,?)",(name,section,roll,branch))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    con.close()
    return rows

def search(name="",section="",roll="",branch=""):
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute("SELECT * from students WHERE name=? or section=? or roll=? or branch=?",(name,section,roll,branch))
    rows = cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE id=?",(id,))
    con.commit()
    con.close()

def update(id,name,section,roll,branch):
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute("UPDATE students SET name=?, section=?, roll=?, branch=? WHERE id=?",(name,section,roll,branch,id))
    con.commit()
    con.close()

connect()
#insert("Uday Vikram Singh","8C",2001220100120,"IT")
#delete(3)
#update(2,"Uday Vikram Singh","7C",120,"CSE")
#print(view())
