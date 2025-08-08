import os

users = {
    'admin': 'admin123',
    'doctor': 'medic123',
    'nurse': 'nurse123'
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    clear()
    print("=== Insecure Login System ===")
    username = raw_input("Enter username: ")
    password = raw_input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful! Welcome, %s" % username)
        return username
    else:
        print("Invalid credentials.")
        return None

def view_patient_data(user):
    print("\n=== Patient Medical Records ===")
    print("WARNING: Displaying sensitive patient information")
    print("Patient: John Doe")
    print("DOB: 01/01/1970")
    print("Condition: Type 2 Diabetes")
    print("Prescriptions: Metformin")

def main():
    user = login()
    if user:
        view_patient_data(user)

if __name__ == '__main__':
    main()
