import psycopg2
def create_table():
    con = psycopg2.connect(dbname = 'studentdb', user = 'postgres',password = 'admin123', host = 'localhost', port = '5432')
    cur = con.cursor()
    cur.execute('Create table if not exists students(student_id serial primary key, name text, age int, address text, number text);')
    print('Student table created')
    con.commit()
    con.close()

def insert_data():
    name = input('Enter Name:...')
    age = int(input('Enter Age:...'))
    address = input('Enter Address:...')
    number = input('Enter Number:...')
    con = psycopg2.connect(dbname = 'studentdb', user = 'postgres',password = 'admin123', host = 'localhost', port = '5432')
    cur = con.cursor()
    cur.execute("insert into students(name,age, address, number) values (%s,%s,%s,%s)",(name,age,address,number))
    print('Data added in students table')
    con.commit()
    con.close()

def read_data():
    con = psycopg2.connect(dbname = 'studentdb', user = 'postgres',password = 'admin123', host = 'localhost', port = '5432')
    cur = con.cursor()
    cur.execute('select * from students;')
    students = cur.fetchall()
    for student in students:
        print(f'ID: {student[0]}, Name:{student[1]}, Age:{student[2]}, Address: {student[3]}, Number:{student[4]}')
    con.close()


def update_data():
    student_id = input('Enter id of the student that needs to be updated')
    con = psycopg2.connect(dbname = 'studentdb', user = 'postgres',password = 'admin123', host = 'localhost', port = '5432')
    cur = con.cursor()
    fields = {
        "1":("name","Enter the new name: "),
        "2":("age","Enter the new Age: "),
        "3":("address","Enter the new address: "),
        "4":("number","Enter the new number: ")

    }
    print('Which field would you like to update')
    for key in fields:
        print(f'{key}:{fields[key][0]}')
    fields_choice = input('Enter the number of the fields you want to update: ')

    if fields_choice in fields:
        field_name, prompt = fields[fields_choice]
        new_value = input(prompt)
        sql = (f"update students set {field_name}=%s where student_id=%s")
        cur.execute(sql, (new_value, student_id))
        print(f"{field_name} updated successfully")

    else:
        print("Invalid choice")

    con.commit()
    con.close()


def delete_data():
    student_id = input('Enter id of the student that needs to be deleted')
    con = psycopg2.connect(dbname = 'studentdb', user = 'postgres',password = 'admin123', host = 'localhost', port = '5432')
    cur = con.cursor()

    cur.execute("select * from students where student_id = %s", (student_id,))
    student = cur.fetchone()

    if student:
        print(f'Student to be deleted: ID {student[0]}, Name: {student[1]}, Age: {student[2]}, Address: {student[3]}, Number:{student[4]} ')
        choice = input("Are you sure you want to delete the student (yes/no)")
        if choice.lower() == 'yes':
            cur.execute("delete from students where student_id = %s", (student_id,))
            print("Student record deleted")
        else:
            print("Deletion cancelled")
    
    else:
        print("Student not found")
    
    con.commit()
    con.close()



while True:
    print('\nWelcome to the student database managment system')
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")
    choice  = input("Please enter the number (1-6)")
    if choice == '1':
        create_table()
    elif choice =='2':
        insert_data()
    elif choice =='3':
        read_data()
    elif choice =='4':
        update_data()
    elif choice =='5':
        delete_data()
    elif choice =='6':
        break
    else:
        print('Invalid choice')
        





