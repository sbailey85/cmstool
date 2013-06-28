__author__ = 'sean'
import MySQLdb as mysql

class connect:
    def __init__(self):
        self.conn = mysql.connect(host = "localhost",user = "test",
        passwd = "password", db = "test")
    def kill(self):
        self.conn.close()

    def nume(self):
        return self.conn

sql = "select * from wp_users"
conn = connect.nume()
cursor = conn.cursor()
cursor.execute(sql)
cursor.fetchone()