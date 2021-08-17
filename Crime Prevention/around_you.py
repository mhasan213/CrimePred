import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM chicago_crime_data")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def find_id(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    r=input()
    #l= input()
    cur.execute("""
                SELECT * FROM chicago_crime_data WHERE chicago_crime_data.District=?
                ;""", (r,))

    rows = cur.fetchall()
    return rows
    print(rows)
    for row in rows:
        print(row)

# def select_task_by_priority(conn, priority):
#     """
#     Query tasks by priority
#     :param conn: the Connection object
#     :param priority:
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
#
#     rows = cur.fetchall()
#
#     for row in rows:
#         print(row)


def main():
    database = "crime_data.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
       # select_task_by_priority(conn, 1)

        print("2. Query all tasks")
        #select_all_tasks(conn)
        find_id(conn)


if __name__ == '__main__':
    main()