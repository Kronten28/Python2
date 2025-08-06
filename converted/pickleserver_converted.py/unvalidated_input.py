import sqlite3

def login() -> None:
    db_path: str = 'users.db'
    conn: sqlite3.Connection = sqlite3.connect(db_path)
    cursor: sqlite3.Cursor = conn.cursor()

    username: str = input("Enter username: ")
    password: str = input("Enter password: ")

    query: str = "SELECT 1 FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    result: tuple | None = cursor.fetchone()

    if result is not None:
        print("Login successful")
    else:
        print("Invalid credentials")

    conn.close()

if __name__ == '__main__':
    login()
