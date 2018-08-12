import psycopg2

#######@!!!!#####POSTGRES NEEDS THE QUOTES REVERSED FROM NORMAL.  DOUBLE QUOTE ON OUTSIDE, SINGLE QUOTE INSIDE

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))   #numbers are quantity and price

    conn.commit()
    conn.close()



def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='password' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='password' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='password' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

update(11,6,"Apple")

delete('Orange')

#insert("Coffee Glass",10,5)


create_table()
insert('Orange',10,15)
print(view())

