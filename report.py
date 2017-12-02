#!/usr/bin/env python3

# import psycopg2 to use postgres sql
import psycopg2

# database name
DBNAME = "news"

# connect to database
connection = psycopg2.connect(database=DBNAME)

# create cursor
cursor = connection.cursor()

# decorator at the beginning of report
print("="*65)
print("\n" + " "*20 + "NEWS ANALYSIS REPORT\n")

# executing popular_articles query and storing the result table in result1
cursor.execute("select * from popular_articles")
results1 = cursor.fetchall()
print("\n1. The most popular three articles of all time are:\n")
for i in range(3):
    print('\t{}. "{}" -- {} views'.format(i+1, results1[i][0], results1[i][1]))

# executing popular_authors query and storing the result table in result2
cursor.execute("select * from popular_authors")
results2 = cursor.fetchall()
print("\n\n2. The most popular authors of all time are:\n")
for i in range(len(results2)):
    print('\t{}. {} -- {} views'.format(i+1, results2[i][0], results2[i][1]))

# executing most_error query and storing the result table in result3
cursor.execute("select * from most_errors")
results3 = cursor.fetchall()
print("\n\n3. Days on which more than 1% of the requests lead to error are:\n")
for i in range(len(results3)):
    print('\t{}. {} -- {})% error'.format(i+1, results3[i][0], results3[i][1]))

# decorator at the end of the report
print("\n"+"="*65)

# closing the connection from database
connection.close()
