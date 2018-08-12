import psycopg2

class dataBase:

    def connect(self):
        self.conn=psycopg2.connect("dbname='pythontest' user='postgres' password='postgres' host='192.168.200.10' port='5432'")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS house (id INTEGER PRIMARY KEY, color TEXT, price REAL)")
        self.conn.commit()
        print ('Database Opened')

    def insert(self,id,color,price):
        self.cur.execute("INSERT INTO house VALUES (%s,%s,%s)",(id,color,price))
        self.conn.commit()
        print ('Inserted Items')

    def view(self):
        self.cur.execute("SELECT * FROM house")
        recv=self.cur.fetchall()
        return recv

    def add_column(self):
        self.cur.execute("ALTER TABLE house ADD COLUMN size TEXT")
        self.conn.commit()

    def insert_data(self,size):
        self.cur.execute("UPDATE house SET size=%s WHERE id=2",(size,))
        self.conn.commit()

    def close(self):
        self.conn.close()
        print ('Database Closed')



db=dataBase()
db.connect()
#db.add_column()
#db.insert(3,'red',50000)
db.insert_data('Medium')
print(db.view())

db.close()
