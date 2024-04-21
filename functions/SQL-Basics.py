import os
import sqlite3

os.chdir(os.path.dirname(os.path.realpath(__file__)))


class Employee():
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def __repr__(self):
        return f"Employee({self.first},{self.last},{self.pay})"



#erstellt eine db
#conn = sqlite3.connect('employee.db')

#erstellt eine db im ram die sich automatisch löscht
conn = sqlite3.connect(':memory:')


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{"first":emp.first,"last":emp.last,"pay":emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=?",(lastname,))
    return c.fetchall()

def update_pay(emp,pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay 
                    WHERE first = :first AND last = :last""",
                    {"first":emp.first,"last":emp.last,"pay":pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first= :first AND last = :last",{"first":emp.first,"last":emp.last})


#erstellt cursor
c = conn.cursor()
#table employees erstellen
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
        )""")


empl_1=Employee("john","Doe",8000)
empl_2=Employee("Adam","Doe",9000)
empl_3=Employee("Adam","Shfer",15000)

c.execute(f"INSERT INTO employees VALUES ('{empl_1.first}','{empl_1.last}',{empl_1.pay})")

conn.commit()


#hier wird eine dict benutzt anstelle eines f strings
c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{"first":empl_2.first,"last":empl_2.last,"pay":empl_2.pay})
conn.commit()

#benutze hier ein tuple mit ? als placeholder
c.execute("SELECT * FROM employees WHERE last=?",('Doe',))
print(c.fetchone())




insert_emp(empl_3)

emps = get_emps_by_name("Shfer")
print(emps)


conn.commit()

conn.close()