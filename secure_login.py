import sqlite3

username = input("Username: ")
password = input("Password: ")

try:
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username=? AND password=?"

    cursor.execute(query, (username, password))

    result = cursor.fetchone()

    if result:
        print("Login Successful")
    else:
        print("Login Failed")

except Exception:
    print("Database Error")

finally:
    conn.close()