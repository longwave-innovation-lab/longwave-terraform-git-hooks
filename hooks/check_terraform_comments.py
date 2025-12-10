#!/usr/bin/env python3
import re
import sys

def check_terraform_comments(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []
    lines = content.split('\n')

    for i, line in enumerate(lines, 1):
        # Remove strings to avoid false positives
        line_without_strings = re.sub(r'"[^"]*"', '', line)

        # Check for // comments (not in strings)
        if re.search(r'^\s*//', line_without_strings):
            errors.append(f"{file_path}:{i}: Use '#' for comments, not '//'")

        # Check for /* */ comments (not in strings)
        if re.search(r'/\*.*\*/', line_without_strings) or re.search(r'^\s*/\*', line_without_strings):
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
