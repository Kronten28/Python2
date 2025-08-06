import sqlite3

def login():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    username = raw_input("Enter username: ")
    password = raw_input("Enter password: ")

    query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)

    cursor.execute(query)
    result = cursor.fetchone()
    
    if result:
        print "Login successful"
    else:
        print "Invalid credentials"

    conn.close()

if __name__ == '__main__':
    login()
