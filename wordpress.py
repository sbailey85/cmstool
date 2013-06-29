import db

import re
import MySQLdb as mysql
import sys
import os

if __name__ == '__main__':
	if not os.path.exists("wp-config.php"):
			print("wp-config.php does not exist in current directory")
			sys.exit(1)
	else:
		pass
#~ wpcfg = open("wp-config.php")
#~ dbpassRE = re.compile("(.*)DB_PASSWORD\'\,.\'(.*)\'")

#~ def dbuser():
	#~ with open("wp-config.php") as f:
		#~ for lines in f.readlines():
			#~ match = userRE.search(lines)
			#~ if match:
				#~ return match.group(2)
			#~ 

class WPparser():
	def __init__(self):
		def dbuser():
			userRE = re.compile("(.*)DB_USER\'\,.\'(.*)\'")
			with open("wp-config.php") as f:
				for lines in f.readlines():
					match = userRE.search(lines)
				if match:
					return match.group(2)
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

		
		self.host = "localhost"
		self.passwd = dbpass()
		self.db = DBNAME()
		self.usern = dbuser()

def wordpressmysql(query):
		host = "localhost"
		user = "test"
		password = "test"
		db = "test"
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


host = "localhost"
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


class connection:
    def __init__(self):
		x = WPparser()
		self.conn = mysql.connect(host = x.host ,user = x.usern,
                             passwd = x.passwd, db = x.db
                             )

    def TearDown(self):
        self.conn.close()
    def nume(self):
        return self.conn










