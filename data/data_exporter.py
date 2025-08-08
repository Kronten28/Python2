import sqlite3
import csv

DB_FILE = 'patients.db'

def export_data(user):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT name, ssn, diagnosis FROM patient_records WHERE created_by = ?", (user,))
    rows = cursor.fetchall()
    conn.close()

    filename = '%s_export.csv' % user
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'SSN', 'Diagnosis'])
        writer.writerows(rows)

    print("Export complete: %s" % filename)

def main():
    print("=== Export Tool ===")
    user = raw_input("Username: ")
    export_data(user)
    print("Done.")

if __name__ == '__main__':
    main()
