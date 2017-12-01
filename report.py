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
print("\n" + " "*20 + " NEWS ANALYSIS REPORT\n")

# executing popular_articles query and storing the result table in result1
cursor.execute("select * from popular_articles")
results1 = cursor.fetchall()
print("\n1. The most popular three articles of all time are:\n")
for i in range(3):
    print("\t"+str(i+1)+". \""+results1[i][0]+"\" -- "+str(results1[i][1])+" views")







