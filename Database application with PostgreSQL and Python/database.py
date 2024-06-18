import psycopg2

def create_table():
    conn = psycopg2.connect(dbname="studentdb",user ="postgres",password="root",host="localhost",port=5432) 
    cur = conn.cursor()
    cur.execute("create table students(id serial primary key, name text, address text, age int, number text);")
    print("table created")
    conn.commit()
    conn.close()

def insert_data():
    name = input("Enter a name: ")
    address = input("Enter a address: ")
    age = input("Enter a age: ")
    number = input("Enter a number: ")
    conn = psycopg2.connect(dbname="studentdb",user ="postgres",password="root",host="localhost",port=5432) 
    cur = conn.cursor()
    cur.execute("insert into students(name,address,age,number) values(%s,%s,%s,%s);",(name,address,age,number))
    print("data inserted")
    conn.commit()
    conn.close()

def update_data():

    conn = psycopg2.connect(dbname="studentdb",user ="postgres",password="root",host="localhost",port=5432) 
    cur = conn.cursor()

    id = input("Enter id you want to update: ")
    fields = { "1":("name","Enter the new Name: "),"2":("address","Enter the new Address: "),
               "3":("age","Enter the new Age: "),"4":("number","Enter the new Number: ") }
    print("Which field you will like to update?")
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    input_value = input("Enter the number of field you want to update: ")

    if input_value in fields:
        field_name, prompt = fields[input_value]
        new_value = input(prompt)
        qry = f"update students set {field_name} = %s where id = %s;"
        cur.execute(qry,(new_value,id))
        print(f"{field_name} updated")
    else:
        print("Invalid choice")
    
    conn.commit()
    conn.close()

def del_data():
    id = input("Enter id you want to delete: ")
    conn = psycopg2.connect(dbname="studentdb",user ="postgres",password="root",host="localhost",port=5432) 
    cur = conn.cursor()
    cur.execute("select * from students where id = %s",(id,))
    student = cur.fetchone()
    if student:
        print(f"Student will be deleted {student[0]} Name = {student[1]}, Address = {student[2]}, Age = {student[3]}, Number = {student[4]}")
    sure = input("Are you sure you want to delete data (Y/N): ")
    if sure =="Y":
        cur.execute("delete from students where id = %s",(id,))
        print("data deleted")
    elif sure =="N" :
        print("Data not deleted")
    
    conn.commit()
    conn.close()

def read_data():
    conn = psycopg2.connect(dbname="studentdb",user ="postgres",password="root",host="localhost",port=5432) 
    cur = conn.cursor()
    cur.execute("select * from students;")
    students = cur.fetchall()
    for student in students:
        print(f"Student id = {student[0]} Name = {student[1]}, Address = {student[2]}, Age = {student[3]}, Number = {student[4]}")
    conn.commit()
    conn.close()


while True:
    print("\n welcome to the students database")
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")
    choice = input("Enter you choice: ")

    if choice == "1":
        create_table()
    elif choice == "2":
        insert_data()
    elif choice == "3":
        read_data()
    elif choice == "4":
        update_data()
    elif choice == "5":
        del_data()
    elif choice == "6":
        break
    else:
        print("Enter a number between 1 to 6")