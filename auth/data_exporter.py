import sqlite3
import csv
import os

DB_FILE = 'patients.db'

def export_data(username):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    query = "SELECT name, ssn, diagnosis FROM patient_records WHERE created_by = '%s'" % username
    cursor.execute(query)

    rows = cursor.fetchall()
    conn.close()

    csv_file = '%s_export.csv' % username
    with open(csv_file, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'SSN', 'Diagnosis'])
        writer.writerows(rows)

    print("Data exported to %s" % csv_file)

def main():
    print("=== Export Tool ===")
    username = raw_input("Enter your username: ")
    export_data(username)
    print("Done.")

if __name__ == '__main__':
    main()
