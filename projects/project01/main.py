# Bren Rodriguez, DEV128, November 10, 2026 Project 1 - main.py
# AI assisted: I used Claude to explain ____concepts and to debug____
# Reconstructed from "Beginning Python - Working with SQLite - Part 1"
# This represents the expanded version shown near the end of the video.

# import the sqlite3 database module
import sqlite3

print("SQLite Practice - Example User Table\n")

# create a connection to the database file
conn = sqlite3.connect("users.db")

# create a cursor that we will use to move through the database
cursor = conn.cursor()


# create the table if it doesn't already exist
# note that primary keys are automatically created in sqlite3 and referenced as rowid
cursor.execute("CREATE TABLE IF NOT EXISTS user (first_name TEXT, last_name TEXT, email TEXT, phone TEXT, street_address TEXT, city TEXT, state TEXT, zip_code TEXT)")

# create some records of data
cursor.execute("INSERT INTO user VALUES (\"Sophia\", \"Huerta\", \"sophia@reignfc.com\", \"555-111-2222\", \"12345 Main Street\", \"Tacoma\", \"WA\", \"98581\")")
cursor.execute("INSERT INTO user VALUES (\"Laura\", \"Harvey\", \"laura@reignfc.com\", \"984-553-2424\", \"1233 3rd Ave.\", \"Bothel\", \"WA\", \"91248\")")
cursor.execute("INSERT INTO user VALUES (\"Lynn\", \"Byendolo\", \"lynn@reignfc.com\", \"123-443-2424\", \"1233 Michigan Ave.\", \"Seattle\", \"WA\", \"90248\")")
cursor.execute("INSERT INTO user VALUES (\"Mia\", \"Fishel\", \"mia@reignfc.com\", \"555-045-2424\", \"1233 Eastern Ave.\", \"Bellevue\", \"WA\", \"97001\")")
cursor.execute("INSERT INTO user VALUES (\"Maddie\", \"Mercado\", \"maddie@reignfc.com\", \"641-321-6424\", \"1233 53rd Ave.\", \"Seattle\", \"WA\", \"91248\")")


# query the table including the rowid primary key value
cursor.execute("SELECT rowid, first_name, last_name, email FROM user")

# store the results of the query to a list called users
users = cursor.fetchall()

# now we can loop through the results of the query
for this_user in users:
    print(this_user[0], this_user[1], this_user[2], this_user[3], this_user[4], this_user[5])

# save the updates to the database - if you don't commit any updates/inserts to the database will not be saved
conn.commit()

# close the connection
conn.close()
