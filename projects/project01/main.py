# Bren Rodriguez, DEV128, November 10, 2026 Project 1 - main.py
# AI assisted: I used Claude to seed data only once, ? placeholders, debug indentations, IndexError.
# Reconstructed from "Beginning Python - Working with SQLite - Part 1"
# This represents the expanded version shown near the end of the video.

# import the sqlite3 database module
import sqlite3

print("SQLite Practice - Seattle Reign FC Player Database\n")

# create a connection to the database file
conn = sqlite3.connect("users.db")

# create a cursor that we will use to move through the database
cursor = conn.cursor()


# create the table if it doesn't already exist
# note that primary keys are automatically created in sqlite3 and referenced as rowid
cursor.execute("CREATE TABLE IF NOT EXISTS user (first_name TEXT, last_name TEXT, email TEXT, phone TEXT, street_address TEXT, city TEXT, state TEXT, zip_code TEXT)")
# only add seed data if the table is empty
# create some records of data
cursor.execute("SELECT COUNT(*) FROM user")
count = cursor.fetchone()[0]
if count == 0:
  cursor.execute("INSERT INTO user VALUES (\"Sophia\", \"Huerta\", \"sophia@reignfc.com\", \"555-111-2222\", \"12345 Main Street\", \"Tacoma\", \"WA\", \"98581\")")
  cursor.execute("INSERT INTO user VALUES (\"Laura\", \"Harvey\", \"laura@reignfc.com\", \"984-553-2424\", \"1233 3rd Ave.\", \"Bothell\", \"WA\", \"91248\")")
  cursor.execute("INSERT INTO user VALUES (\"Lynn\", \"Byendolo\", \"lynn@reignfc.com\", \"123-443-2424\", \"1233 Michigan Ave.\", \"Seattle\", \"WA\", \"90248\")")
  cursor.execute("INSERT INTO user VALUES (\"Mia\", \"Fishel\", \"mia@reignfc.com\", \"555-045-2424\", \"1233 Eastern Ave.\", \"Bellevue\", \"WA\", \"97001\")")
  cursor.execute("INSERT INTO user VALUES (\"Maddie\", \"Mercado\", \"maddie@reignfc.com\", \"641-321-6424\", \"1233 53rd Ave.\", \"Seattle\", \"WA\", \"91248\")")


def full_roster_report():
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, email, phone, street_address, city, state, zip_code FROM user")

    # store the results of the query to a list called users
    users = cursor.fetchall()

    # now we can loop through the results of the query
    for this_user in users:  
            print(this_user[0], this_user[1], this_user[2], this_user[3], this_user[4], this_user[5], this_user[6], this_user[7], this_user[8])
def player_location_report():
    cursor.execute("SELECT rowid, first_name, last_name, city, state FROM user") 
    users = cursor.fetchall()
    for this_user in users:
            print(this_user[0], this_user[1], this_user[2], this_user[3],this_user[4])


def add_user(conn):

    cursor = conn.cursor()
    
    print()
    input_first_name = input("First Name: ")
    input_last_name = input("Last Name: ")
    input_email = input("Email: ")
    input_phone = input("Phone: ")
    input_street = input("Street Address: ")
    input_city = input("City: ")
    input_state = input("State: ")
    input_zip = input("Zipcode: ")

    sql = """
    INSERT INTO user (first_name, last_name, email, phone, street_address, city, state, zip_code)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?)"""
    
    cursor.execute(sql, (input_first_name, input_last_name, input_email, input_phone, input_street, input_city, input_state, input_zip))
   
    # save the updates to the database - if you don't commit any updates/inserts to the database will not be saved
    conn.commit()

    print(f"{input_first_name} {input_last_name} has been added.")

while True:
  print("\nSeattle Reign FC Player Database")
  print("* * * MENU * * *")
  print("1 - Full Roster Report")
  print("2 - Player Location Report")
  print("3 - Add User")
  print("4 - Exit")

  choice = input("Your choice: ")

  if choice == "1":
    full_roster_report()
  elif choice == "2":
    player_location_report()
  elif choice == "3":
    add_user(conn)
  elif choice == "4":
    print("Goodbye")
    break

  else:
    print("Invalid Choice")

conn.commit()
# close the connection
conn.close()
