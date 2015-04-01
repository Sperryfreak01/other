# To export (dump) a local database
'''
1. cd to the bin folder in the postgreSQL path: cd C:\Program Files (x86)\PostgreSQL\9.4\bin
2. pg_dump -Fc --no-acl --no-owner -h localhost -U postgres third_db > prop_data.dump