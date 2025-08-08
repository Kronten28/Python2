import os

def analyze_log(file_name):
    path = 'logs/' + file_name

    with open(path, 'r') as f:
        lines = f.readlines()

    errors = [l for l in lines if 'ERROR' in l]
    warnings = [l for l in lines if 'WARNING' in l]

    print("=== Report for %s ===" % file_name)
    print("Errors: %d | Warnings: %d" % (len(errors), len(warnings)))
    for e in errors:
        print("[!] %s" % e.strip())

def main():
    print("=== Insecure Log Analyzer ===")
    fname = raw_input("Enter log file name: ")
    analyze_log(fname)

if __name__ == '__main__':
    main()
