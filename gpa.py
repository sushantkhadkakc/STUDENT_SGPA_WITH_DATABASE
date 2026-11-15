totalcredit=0
totalgrade=0
totalpoint=0
import sqlite3
conn=sqlite3.connect("markshettt.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS user(rollno INTEGER PRIMARY KEY,name TEXT,sem INTEGER,subject TEXT,credit INTEGER,letter_grade TEXT)""")
class info:
    def fg(self):
        global totalcredit
        global totalgrade
        global totalpoint
        name=input("ENTER YOUR NAME\n")
        sem=int(input("ENTER YOUR SEM\n"))
        for i in range(1,6):
               subject=input("ENTER YOUR SUBJECT\n")
               credit=int(input('ENTER YOUR SUBJECT CREDIT HOUR\n'))
               totalcredit+=credit
               grade_point=float(input("ENTER YOUR LETTER GRADE\n"))
               totalgrade+=grade_point
               totalpoint+=credit*grade_point
               self.spga=totalpoint/totalcredit
               cursor.execute("INSERT INTO user(name,sem,subject,credit,letter_grade) VALUES(?,?,?,?,?)",(name,sem,subject,credit,grade_point))
               conn.commit()
        print(f"spga:{self.spga}")
a=info()
a.fg()               
        

         