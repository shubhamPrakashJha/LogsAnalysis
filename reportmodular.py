#!/usr/bin/env python3


# import psycopg2 to use postgres sql
import psycopg2


def db_connect():
    """ Creates and returns a connection to the database defined by DBNAME,
        as well as a cursor for the database.
    """
    global cursor
    # database name
    dbname = "news"
    # connect to database
    try:
        connection = psycopg2.connect(database=dbname)
    except psycopg2.Error:
        print("-"*29 + "warning" + "-"*29 +
              "\n can not find news database,"
              " database might not set up properly."
              "\n\n Please refer \'how to setup database\'"
              " in README file for help.\n")
        exit()
    # create cursor
    cursor = connection.cursor()


def execute_query(query):
    """
    execute_query takes an SQL query as a parameter.
    Executes the query and returns the results as a list of tuples.
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def print_top_articles():
    """Prints out the top 3 articles of all time."""
    query = "select * from popular_articles"
    results = execute_query(query)

    print("\n1. The most popular three articles of all time are:\n")
    for i in range(3):
        print('\t{}. "{}" -- {} views'
              .format(i + 1, results[i][0], results[i][1]))


def print_top_authors():
    """Prints a list of authors ranked by article views."""
    query = "select * from popular_authors"
    results = execute_query(query)

    print("\n\n2. The most popular authors of all time are:\n")
    for i in range(len(results)):
        print('\t{}. {} -- {} views'
              .format(i + 1, results[i][0], results[i][1]))


def print_errors_over_one():
    """
    Prints out the days,
    where more than 1% of logged access requests were errors.
    """
    query = "select * from most_errors"
    results = execute_query(query)

    print("\n\n3. Days on which more than 1% of "
          "the requests lead to error are:\n")
    for i in range(len(results)):
        print('\t{}. {} -- {}% error'
              .format(i + 1, results[i][0], results[i][1]))


if __name__ == '__main__':
    # decorator at the beginning of report
    print("=" * 65)
    print("\n" + " " * 20 + "NEWS ANALYSIS REPORT\n")

    db_connect()
    print_top_articles()
    print_top_authors()
    print_errors_over_one()

    # decorator at the end of the report
    print("\n" + "=" * 65)
