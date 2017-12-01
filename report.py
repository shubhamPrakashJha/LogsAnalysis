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









