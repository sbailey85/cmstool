__author__ = 'sean'
import MySQLdb as mysql
import sys
import os
import string
cwd = os.path.realpath(".")
host = "localhost"
password = "password"
db = "test"
user = "test"
cms = ["wordpress","joomla","magento"]

def connect(host,user,password,database):

    try:
        connectdb = mysql.connect(host,user,password,db)
        var = connectdb.cursor()
        var.execute("select * from wp_options")
        print(var.fetchall())


    except mysql.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)




