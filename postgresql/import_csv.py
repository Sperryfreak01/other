"""
Script to load csv files into PostgreSQL database

Overview:
1. Get list of files to import
2. Get list of tables
3. Clear each table
4. Import new csv data into each table
"""
import os
import psycopg2

# Get list of files to import
file_list = os.listdir('C:/Users/pfriedhoff/Desktop/Arena Extracts')
file_list.sort()

# Setup connection: http://initd.org/psycopg/docs/module.html
try:
	connection = psycopg2.connect(database = 'try_imports', host = 'localhost', user = 'postgres', password = '123')
except psycopg2.Error as e:
	print ('Cannot connect to db: %s, %s' % (e.pgcode, e.pgerror))

# Get list of tables from database
cursor = connection.cursor()
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
table_list = []
for i in cursor.fetchall():
	table_list.append(i)
table_list.sort()
cursor.close()

# Build {table: file} dictionary
tables_to_files = dict(zip(table_list, file_list))

# Create tables (look into how to cursor.execute(my_sql_file.sql))

# Drop (remove) existing tables
# cursor = connection.cursor()
# for i in table_list:
# 	try:
# 		cursor.execute("DROP TABLE IF EXISTS %s" % i)
# 	except:
# 		print ('Something went wrong dropping table: %s' % i)
# 		break
# 	else:
# 		print ('Dropped: %s' % i)
# connection.commit()
# cursor.close()

# Delete existing data from tables
cursor = connection.cursor()
for i in table_list:
	try:
		cursor.execute("DELETE FROM %s" % i)
	except:
		print ('Something went wrong deleting data from %s' % i)
		break
	else:
		print ('Deleted from: %s' % i)
connection.commit()
cursor.close()

# Import csv data using copy_expert()
cursor = connection.cursor()
for k, v in tables_to_files.items():
	try:		
		cursor.copy_expert(sql = "COPY %s FROM STDIN WITH DELIMITER ',' CSV HEADER" % k, file = open('C:/Users/pfriedhoff/Desktop/Arena Extracts/%s' % v, encoding = 'utf8'))
		connection.commit()
	except psycopg2.Error as e:
		print ('Import error: %s, %s' % (k, v))
		print ('%s, %s' % (e.pgcode, e.pgerror))
		break
	else:
		print ('File copied: %s' % v)
cursor.close()
connection.close()