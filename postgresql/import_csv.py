"""
Script to load csv files into PostgreSQL database

Ideally trying for this workflow
	For each table in database:
		a. clear contents
		b. import correct csv file
		c. apply appropriate field relationships
"""
import os
import psycopg2

# Create the SQL copy statement to pass into copy_expert()
SQL = "COPY %s FROM STDIN WITH DELIMITER ',' CSV HEADER"

# Get list of all files
file_list = os.listdir('C:/Users/pfriedhoff/Desktop/Arena Extracts')

# Create file object to pass into copy_expert()
my_file = open('C:/Users/pfriedhoff/Desktop/Arena Extracts/Changes_Summary.csv')

# Refer to: http://initd.org/psycopg/docs/cursor.html?highlight=copy%20expert#cursor.copy_expert
def import_file(conn, table_name, file_object):
	cursor = conn.cursor()
	cursor.copy_expert(sql = SQL % table_name, file = file_object)
	conn.commit()
	cursor.close()

# Setup database connection: http://initd.org/psycopg/docs/module.html
try:
	conn = psycopg2.connect(database = 'try_imports', host = 'localhost', user = 'postgres', password = '123')
except psycopg2.Error as e:
	print ('Cannot connect to db: %s, %s' % (e.pgcode, e.pgerror))

# Get all tables
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM information_schema.tables WHERE table_schema ='public'")
# for i in cursor:
# 	print (i)

# Execute copy_expert()
try:
	import_file(conn, 'changes_summary', my_file)
except:
	print ('Something wrong with import')
else:
	print ('File copied!')
finally:
	conn.close()