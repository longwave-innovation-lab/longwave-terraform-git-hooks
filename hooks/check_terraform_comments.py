#!/usr/bin/env python3
import re
import sys

def check_terraform_comments(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    errors = []

    for i, line in enumerate(lines, 1):
        # Check for // comments
        if re.search(r'^\s*//', line):
            errors.append(f"{file_path}:{i}: Use '#' for comments, not '//'")

        # Check for /* */ comments
        if re.search(r'/\*', line):
            errors.append(f"{file_path}:{i}: Use '#' for comments, not '/* */'")

    return errors

def main():
    all_errors = []
    for file_path in sys.argv[1:]:
        if file_path.endswith('.tf'):
            all_errors.extend(check_terraform_comments(file_path))

    if all_errors:
        for error in all_errors:
            print(error)
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
