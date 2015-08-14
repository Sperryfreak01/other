import csv
import psycopg2

SQL = "COPY %s FROM STDIN WITH DELIMITER ',' CSV HEADER"

my_file = open('C:/Users/pfriedhoff/Desktop/Arena Extracts/Changes_Summary.csv')

# with open('C:/Users/pfriedhoff/Desktop/Arena Extracts/Changes_Summary.csv', newline = '') as csvfile:
# 	data = csv.reader(csvfile, delimiter = ',')

def import_file(conn, table_name, file_object):
	cursor = conn.cursor()
	cursor.copy_expert(sql = SQL % table_name, file = file_object)
	conn.commit()
	cursor.close()

try:
	conn = psycopg2.connect(database = 'try_imports', host = 'localhost', user = 'postgres', password = '123')
except:
	print ('Cannot connect to db')

try:
	import_file(conn, 'changes_summary', my_file)
except:
	print ('Something wrong with import')
finally:
	conn.close()