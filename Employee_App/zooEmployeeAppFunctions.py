#import zooEmployeeApp
import sqlite3 # Used for SQL database  connection
import hashlib # Used for password hashing
import os # Used to generate a salt



def check_password(entered_password, employee_id):
    global logged_in_employee_id

    # Connect to database
    conn = sqlite3.connect('zooEmployeeData.db')
    # Create a cursor
    c = conn.cursor()

    # Grab the salt from the database for this employee ID
    result = c.execute("SELECT salt FROM zooEmployeeData WHERE employee_id = ?", (employee_id,))
    row = c.fetchone()
    conn.commit()
  
    if not row:
        return False

    # Grab the salt from  the database for this employee ID
    existing_salt = c.execute("SELECT salt FROM zooEmployeeData WHERE employee_id = ?", (employee_id,))
    conn.commit()
    existing_salt = c.fetchone()[0]

    # Grab the key from the database for this employee ID 
    existing_key = c.execute("SELECT key FROM zooEmployeeData WHERE employee_id = ?", (employee_id,))
    conn.commit()
    existing_key = c.fetchone()[0]

    # Generate hash using the newly entered password and the existing salt from DB
    new_key = hashlib.pbkdf2_hmac('sha256', entered_password.encode('utf-8'), existing_salt, 100000)
            
    # Check to see if password hashes match
    if existing_key == new_key:
        print("password is valid")
        return True
    else:
        print("password is not valid")
        return False

# Generate and  store a password hash
def create_password_hash(entered_new_pass, employee_id):
    global logged_in_employee_id

    # Create a random salt for use with hashing
    salt = os.urandom(32)

    # Password Hashing
    key = hashlib.pbkdf2_hmac('sha256', entered_new_pass.encode('utf-8'), salt, 100000)


    # Connect to database
    conn = sqlite3.connect('zooEmployeeData.db')
    # Create a cursor
    c = conn.cursor()

    # Update the DB
    c.execute("UPDATE zooEmployeeData SET password_unhashed = ?, salt = ?, key = ? WHERE employee_id = ?", (entered_new_pass, salt, key, employee_id,))
    
    conn.commit()
    conn.close()


# Get employees username
def get_permission_level(employee_id):

    conn = sqlite3.connect('zooEmployeeData.db')
    # Create a cursor
    c = conn.cursor()

    permission_level = c.execute("SELECT permission_level FROM zooEmployeeData WHERE employee_id = ?", (employee_id,))
    conn.commit()

    permission_level = c.fetchone()[0]

    conn.close()

    return permission_level


