import db

import re
import MySQLdb as mysql

import os

host = "localhost"
wpcfg = open("wp-config.php")
userRE = re.compile("(.*)DB_USER\'\,.\'(.*)\'")
dbpassRE = re.compile("(.*)DB_PASSWORD\'\,.\'(.*)\'")


def dbname():
    for x in wpcfg.readlines():
        search = re.search(".DB_NAME.*", x)
        if search:
            result = search
            return result


def dbuser():
    for x in wpcfg.readlines():
        match = userRE.search(x)
        if match:
            result = match.group(2)
            return result


def dbpass():
    with open("wp-config.php") as f:
        for lines in f:
            match = re.search("DB_PASSWORD\'\,.\'(.*)\'", lines)
            if match:
                return match.group(1)


def DBNAME():
    with open("wp-config.php") as y:
        for x in y.readlines():
            match = re.search("DB_NAME\'\,.\'(.*)\'", x)
            if match:
                return match.group(1)


password = dbpass()
user = dbuser()
db1 = DBNAME()


def wordpressmysql(query):
    connectdb = mysql.connect(host, user, password, db)
    var = connectdb.cursor()
    x = var.execute(query)
    result = var.fetchall()
    connectdb.commit()
    connectdb.close()



# Queries
homeurl = """select option_value from wp_options where option_name = home"""
dbpassreset = "update wp_users  set user_pass = MD5('password2') where ID = '1' "
siteurl = "update wp_options  set option_value = 'http://localhost' where option_id = 1 ; "
plugs = "select option_value from wp_options where option_name = 'active_plugins'"
backupquery = "update wp_options set option_value = '' where option_name = 'active_plugins'"
resetplugs = "update wp_options set option_value = '' where option_name = 'active_plugins'"
def backupplugs():
    a = wordpressmysql(plugs)
    y = str(a[0])
    pickle.dump(y,open("plugins.pkl", "wb"))


import pickle
def unpickle():
    x = pickle.load(open("plugins.pkl"))
    return x

unpickled = unpickle()
def backuprestore():
    x ="update wp_options set option_value = '%s' where option_name = 'active_plugins'" %y
    z = str(x)
    result = wordpressmysql(str(x))
    return x
y = unpickled

test = mysql.connect(host, user, password, "test")
cursor = test.cursor()
query = ("update wp_options set option_value = ''" "where option_name = 'active_plugins'")


restore_plugins = """
update wp_options
set option_value= '%s'
where option_name='active_plugins'
""" %y


disable_plugins = """
update wp_options
set option_value=''
where option_name='active_plugins'
"""

class dbConnect(object):
    def __init__(self,host="localhost",
    user="user",
    passwd="password",
    **other_db_arguments):
        self.host = host
        self.user = user
        self.passwd = passwd


        def Connection_Create(self):
            self.connection = mysql.connect(self.host,self.user,self.passwd)

        def KillConnection(self):
            self.connection.close()

        def Execute(self,sql):
            cursor = self.connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result



a = dbConnect("hi")




