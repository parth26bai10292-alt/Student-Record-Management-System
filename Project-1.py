import mysql .connector as sql
con=sql.connect(host="localhost", user="root", password="123456")

    
def create_database() :
    while True:
        try :
            cursor=con.cursor()
            dname=input("Enter your database name:")
            query1="create database {}".format(dname)
            cursor.execute(query1)
            print("Your database has created")
            break
        except :
            print("Database Already Exits.....Try using another name")
            continue


def table() :
    cursor=con.cursor()
    d=input("Enter your database name to be used for creating table:")
    q="use {}".format(d)
    cursor.execute(q)
    print("Now you are using", d, "database")
    F1= "F1:-  Registration_ID, Student_Name, Field_of_Student, Overall_Grade, CGPA"
    F2= "F2:- Registration_ID, Student_Name, Total_Marks, Scored_Marks"
    print("Given below are some formate of table please provide a formate to create the student record table")
    print(F1)
    print(F2)
    ch=input("Enter your formate choice (F1 & F2):")
    if ch == "F1" :
        while True :
            try :
                tname1=input("Enter your table name:")
                query1="create table {} (Registration_ID varchar(50), Student_Name varchar(50), Field_Of_Student varchar(50), Overall_Grade varchar(50), CGPA varchar(50))".format(tname1)
                cursor.execute(query1)
                print("Your table of chossen formate is created successfully")
                break
            except :
                print("Table name is already exists....try using another name")
                continue
        print("For adding records into table, user must enter the values as per the formate choosen")
        ans='y'
        while ans == 'y' :
            r_id=input("Enter student's registration number:")
            s_name=input("Enter student's name:")
            field=input("Enter student's field:")
            grade=input("Overall grade student obtained:")
            cgpa=input("CGPA obtained by the student:")
            q1="insert into {} values (%s, %s, %s, %s, %s)".format(tname1)
            cursor.execute(q1, (r_id, s_name, field, grade, cgpa))
            con.commit()
            print("Your record has added to the table")
            ans=input("Want to enter more data? (y/n) :")
    elif ch == "F2" :
        while True :
            try:
                tname2=input("Enter your table name:")
                query2="create table {} (Registration_ID varchar(50), Student_Name varchar(50), Total_Marks int, Scored_Marks int)".format(tname2)
                cursor.execute(query2)
                print("Your table of choosen formate is created successfully")
                break
            except :
                print("Table name is already exists....try using another name")
                continue
        print("For adding records into table, user must enter the values as per the formate choosen")
        ans='y'
        while ans == 'y':
            rid=input("Enter student's registration number:")
            name=input("Enter student's name:")
            tmarks=int(input("Enter total marks:"))
            omarks=int(input("Enter student's pbtained marks:"))
            q2="insert into {} values (%s, %s, %s, %s)".format(tname2)
            cursor.execute(q2, (rid, name, tmarks, omarks))
            print("Record added successfully into your selected table")
            con.commit()
            ans=input("Want to enter more record? (y/n) :")
    else :
        print("Invalid Choice!!!")


def display() :
    cursor=con.cursor()
    d=input("Enter your database name to be used for displaying record:")
    q="use {}".format(d)
    cursor.execute(q)
    print("Now you are using", d, "database")
    tname=input("Enter your table name from which you want to see data:")
    query="select * from {}".format(tname)
    cursor.execute(query)
    data=cursor.fetchall()
    for rec in data :
        print(rec)

def search() :
    cursor=con.cursor()
    d=input("Enter your database name to be used for displaying record:")
    q="use {}".format(d)
    cursor.execute(q)
    print("Now you are using", d, "database")
    tname=input("Enter your table name from which you want to search record:")
    query="select * from {}".format(tname)
    cursor.execute(query)
    data=cursor.fetchall()
    rid=input("Enter student's registration number to be searched:")
    found=False
    try :
        while True :
            for rec in data :
                if rec[0] == rid :
                    print(rec)
                    found=True
            break
    except :
        if found == False :
            print("No such record found")
        else :
            print("Search Successful")


    
while True :
    print("------Student Records------")
    print("1. Create Database")
    print("2. Creating Record Table")
    print("3. Display Record")
    print("4. Search Record")
    print("5. Exit")
    ch=int(input("Enter your choice:"))
    if ch == 1 :
        create_database()
    elif ch == 2 :
        table()
    elif ch == 3 :
        display()
    elif ch == 4 :
        search()
    elif ch == 5 :
        break
    else :
        print("Invalid choice......try again among 1-5")
        continue
    

 

