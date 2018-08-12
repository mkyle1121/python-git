import pymysql


class db():
    connection = pymysql.connect(host='localhost', user='root', password='root', db='zebra')
    cursor = connection.cursor()

    @staticmethod
    def insert(name):
        sql = "INSERT INTO users VALUES (NULL,%s,NULL,NULL)"
        db.cursor.execute(sql, (name))
        db.connection.commit()
#db.insert('george','g@g.com','secret')



