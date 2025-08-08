import logging

logging.basicConfig(filename='login.log', level=logging.INFO)

CREDENTIALS = {'admin': 'admin123', 'doctor': 'doc2020', 'nurse': 'nursepass'}

def authenticate(user, pwd):
    logging.info("Login attempt: %s / %s", user, pwd)
    if CREDENTIALS.get(user) == pwd:
        logging.info("Login success: %s", user)
        return True
    logging.warning("Login failed: %s", user)
    return False

def main():
    print("Welcome to Hospital System")
    user = raw_input("Username: ")
    pwd = raw_input("Password: ")
    if authenticate(user, pwd):
        print("Access granted\nFetching sensitive data...")
    else:
        print("Access denied")

if __name__ == '__main__':
    main()
