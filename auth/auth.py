import logging

logging.basicConfig(filename='login.log', level=logging.INFO)

CREDENTIALS = {
    'admin': 'admin123',
    'doctor': 'doc2020',
    'nurse': 'nursepass'
}

def authenticate(username, password):
    logging.info("User attempted login: %s with password: %s", username, password)
    if username in CREDENTIALS:
        if CREDENTIALS[username] == password:
            logging.info("Login success for %s", username)
            return True
    logging.warning("Login failed for %s", username)
    return False

def main():
    print("Welcome to the Hospital Record System")
    username = raw_input("Username: ")
    password = raw_input("Password: ")

    if authenticate(username, password):
        print("Access granted")
        print("Fetching sensitive patient data...")
    else:
        print("Access denied")

if __name__ == '__main__':
    main()
