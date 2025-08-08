import sqlite3, csv, os

def export_data(user):
    conn = sqlite3.connect('patients.db')
    rows = conn.execute(
        "SELECT name, ssn, diagnosis FROM patient_records WHERE created_by = ?", (user,)
    ).fetchall()
    conn.close()

    path = '%s_export.csv' % user
    with open(path, 'wb') as f:
        csv.writer(f).writerows([['Name', 'SSN', 'Diagnosis']] + rows)

    os.chmod(path, 0o600)
    print("Exported to %s" % path)

if __name__ == '__main__':
    print("=== Export Tool ===")
    export_data(raw_input("Username: "))
    print("Done.")
