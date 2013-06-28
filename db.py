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

def connect():

    try:
        connectdb = mysql.connect(host,user,password,db)
        var = connectdb.cursor()
        var.execute("SELECT VERSION()")
        var.fetchone()
        print "Database Version : %s " %var.fetchone()

    except mysql.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

    finally:
            if connectdb:
                connectdb.close()

homeurl = "select option_value from wp_options where option_name = home"

dbpassreset = "update wp_users  set user_pass = MD5('password2') where ID = '1' "
siteurl = "update wp_options  set option_value = 'http://localhost' where option_id = 1 ; "
