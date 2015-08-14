"""
Script to load csv files into PostgreSQL database
Work towards:
	a. Autmatically clearing each table
	b. Bulk import of multiple csv files
	c. Alter tables to enfore relationships after load
"""
import psycopg2

# Create the SQL copy statement to pass into copy_expert()
SQL = "COPY %s FROM STDIN WITH DELIMITER ',' CSV HEADER"

# Create file object to pass into copy_expert()
my_file = open('C:/Users/pfriedhoff/Desktop/Arena Extracts/Changes_Summary.csv')

# Refer to: http://initd.org/psycopg/docs/cursor.html?highlight=copy%20expert#cursor.copy_expert
def import_file(conn, table_name, file_object):
	cursor = conn.cursor()
	cursor.copy_expert(sql = SQL % table_name, file = file_object)
	conn.commit()
	cursor.close()

# Setup database connection
try:
	conn = psycopg2.connect(database = 'try_imports', host = 'localhost', user = 'postgres', password = '123')
except:
	print ('Cannot connect to db')

# Execute copy_expert()
try:
	import_file(conn, 'changes_summary', my_file)
except:
	print ('Something wrong with import')
else:
	print ('File copied!')
finally:
	conn.close()