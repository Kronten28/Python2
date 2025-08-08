import os
from typing import List

def analyze_log(file_name: str) -> None:
    path: str = os.path.join('logs', file_name)

    with open(path, 'r') as f:
        lines: List[str] = f.readlines()

    errors: List[str] = [l for l in lines if 'ERROR' in l]
    warnings: List[str] = [l for l in lines if 'WARNING' in l]

    print(f"=== Report for {file_name} ===")
    print(f"Errors: {len(errors)} | Warnings: {len(warnings)}")
    for e in errors:
        print(f"[!] {e.strip()}")

def main() -> None:
    print("=== Insecure Log Analyzer ===")
    fname: str = input("Enter log file name: ")
    analyze_log(fname)

if __name__ == '__main__':
    main()