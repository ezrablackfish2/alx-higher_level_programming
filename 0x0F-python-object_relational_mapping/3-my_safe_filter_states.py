#!/usr/bin/python3

import MySQLdb;
import sys;

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS states ( id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id))")

    states = ["California", "Arizona", "Texas", "New York", "Nevada"]
    values = ", ".join(["('{}')".format(state) for state in states])
    insert_query = "INSERT INTO states (name) VALUES {};".format(values)
    cur.execute(insert_query)
    cur.execute("SELECT * FROM states where name LIKE '{}'".format(sys.argv[4]))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
