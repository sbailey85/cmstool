import re
import sys
import os

import MySQLdb as mysql

import db

if __name__ == '__main__':
	if not os.path.exists("wp-config.php"):
		print("wp-config.php does not exist in current directory")
		sys.exit(1)
	else:
		pass


def dbuser():
    with open("wp-config.php") as s:
        for lines in s:
            match = re.search("DB_USER\'\,.\'(.*)\'", lines)
            if match:
                result = match.group(1)
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

class WPparser:
    def __init__(self):
        self.host = "localhost"
        self.passwd = dbpass()
        self.db = DBNAME()
        self.usern = dbuser()
class Connection:
	def __init__(self):
		x = WPparser()
		self.conn = mysql.connect(host=x.host, user=x.usern, passwd=x.passwd, db=x.db)


	def TearDown(self):
		self.conn.close()

	def nume(self):
		return self.conn



def executor(query):
        c = Connection()
        d = c.nume()
        e = d.cursor()

        e.execute(query)

        return e.fetchall()

print(executor("select * from wp_users"))
def DBNAME():
	with open("wp-config.php") as y:
		for x in y.readlines():
			match = re.search("DB_NAME\'\,.\'(.*)\'", x)
			if match:
				return match.group(1)
# Queries
homeurl = """select option_value from wp_options where option_name = home"""
dbpassreset = "update wp_users  set user_pass = MD5('password2') where ID = '1' "
siteurl = "update wp_options  set option_value = 'http://localhost' where option_id = 1 ; "
plugs = "select option_value from wp_options where option_name = 'active_plugins'"
backupquery = "update wp_options set option_value = '' where option_name = 'active_plugins'"
resetplugs = "update wp_options set option_value = '' where option_name = 'active_plugins'"


def backupplugs():
	y = str(a[0])
	pickle.dump(y, open("plugins.pkl", "wb"))


import pickle


def unpickle():
	x = pickle.load(open("plugins.pkl"))
	return x


unpickled = unpickle()


def backuprestore():
	x = "update wp_options set option_value = '%s' where option_name = 'active_plugins'" % y
	z = str(x)
	result = wordpressmysql(str(x))
	return x


y = unpickled

host = "localhost"
query = ("update wp_options set option_value = ''" "where option_name = 'active_plugins'")

restore_plugins = """
update wp_options
set option_value= '%s'
where option_name='active_plugins'
""" % y

disable_plugins = """
update wp_options
set option_value=''
where option_name='active_plugins'
"""

