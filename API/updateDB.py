from time import localtime, strftime
from configobj import ConfigObj
import MySQLdb, sys

"""
@param status: 		The status of the API
@param category: 	API's category
@param class_name: 	API's name

"""
def setupDB(status, category, class_name):

	# Get DB info from configuration 
	config = ConfigObj('db_user.cfg.sample')
	user = config['user_name']
	passwd = config['pwd']
	host = config['host']
	db = config['db']

	# Open DB connection
	db = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)

	# Get the local system time for time stamp
	stamp = strftime("%Y %b %d %H:%M:%S", localtime())
	
	# If doing API test -> update API DB
	# else if doing IT test -> update IT DB
	env = sys.argv[1]
	if env.find("api") != -1:
		updateAPIdb(db, status, category, class_name, stamp)
	elif env.find("seleniumIT") != -1:
		updateITdb(db, status, class_name, stamp)

"""
UPdate API DB
"""
def updateAPIdb(db, status, category, class_name, stamp):
	
	action = db.cursor()
	action.execute("""CREATE TABLE IF NOT EXISTS API( 
                                category VARCHAR(50),
                                api VARCHAR(50) PRIMARY KEY,
                                status   VARCHAR(10),
                                timeStamp VARCHAR(50)
                                )
  	      		""")

	if status:
		print "sending status OK to DB..."
                # Create a SQL query to the DB
                query = "INSERT INTO API(category, api, status, timeStamp) \
                        	VALUES ('%s', '%s', 'OK', '%s')" %( category, class_name, stamp)
		try:
                	action.execute(query)
                except:
                        query = "UPDATE API SET status = 'OK', timeStamp='%s' \
                           	WHERE api = '%s'" %(stamp, class_name)
                        action.execute(query)

                db.commit()
	else:
		print "sending failure to DB"

                query = "INSERT INTO API(category, api, status, timeStamp) \
                         	VALUES ('%s', '%s', 'FAILURE', '%s')" %(category, class_name, stamp)
                try:
                	action.execute(query)
                except:
                	query = "UPDATE API SET status = 'FAILURE', timeStamp='%s' \
                            	WHERE api = '%s'" %(stamp, class_name)
                        action.execute(query)

                db.commit()

"""
Update IT DB
"""
def updateITdb(db, status, class_name, stamp):

	action = db.cursor()
	action.execute("""CREATE TABLE IF NOT EXISTS IT(
                                function VARCHAR(50) PRIMARY KEY,
                                status VARCHAR(10),
                                timeStamp VARCHAR(50)
                                )
                        """) 
	if status:
		print "sending status OK to DB..."
		# Create a SQL query to the DB
		query = "INSERT INTO IT(function, status, timeStamp) \
                                VALUES('%s', 'OK', '%s')" %(class_name, stamp)
		try:
			action.execute(query)
		except:
			query = "UPDATE IT SET status = 'OK', timeStamp='%s' \
				WHERE function = '%s'" %(stamp, class_name)
			action.execute(query)

		db.commit()
	else:
		print "sending failure to DB..."
		# Create a SQL query to the DB
                query = "INSERT INTO IT(function, status, timeStamp) \
                                VALUES('%s', 'FAILURE', '%s')" %(class_name, stamp)
                try:
                        action.execute(query)
                except:
                        query = "UPDATE IT SET status = 'FAILURE', timeStamp='%s' \
                                WHERE function = '%s'" %(stamp, class_name)
                        action.execute(query)

                db.commit()




