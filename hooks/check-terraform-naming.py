#!/usr/bin/env python3
import re
import sys

def check_terraform_naming(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(resource|data|module|output|variable|locals)\s+"?([a-zA-Z0-9_-]+)"?\s+"?([a-zA-Z0-9_-]+)"?'
    errors = []

    for match in re.finditer(pattern, content):
        block_type = match.group(1)
        name = match.group(3) if match.group(3) else match.group(2)

        if block_type in ['resource', 'data', 'module'] and match.group(3):
            name = match.group(3)

        if '-' in name:
            line_num = content[:match.start()].count('\n') + 1
            errors.append(f"{file_path}:{line_num}: {block_type} '{name}' uses kebab-case. Use snake_case instead.")

    return errors

def main():
    all_errors = []
    for file_path in sys.argv[1:]:
        if file_path.endswith('.tf'):
            all_errors.extend(check_terraform_naming(file_path))

    if all_errors:
        for error in all_errors:
            print(error)
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
