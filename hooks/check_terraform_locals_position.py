#!/usr/bin/env python3
import sys
import re

def check_terraform_locals_position(file_path):
    errors = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return errors

    print("TEEEEEESTTTTT")
    # Remove comments and empty lines for analysis
    lines = content.split('\n')
    non_comment_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#'):
            non_comment_lines.append(stripped)

    if not non_comment_lines:
        return errors

    # Check if there are any locals blocks
    locals_blocks = [line for line in non_comment_lines if 'locals' in line and '{' in line]
    print(f"locals blocks found: {locals_blocks}")
    has_locals = any(locals_blocks)

    if not has_locals:
        return errors

    if len(locals_blocks) > 1:
        errors.append(f"{file_path}: multiple locals blocks found, only one is allowed")
        return errors

    # Find first non-comment block
    first_block_line = non_comment_lines[0]

    # Check if first block is locals
    if not (first_block_line.startswith('locals') and '{' in first_block_line):
        errors.append(f"{file_path}: locals block must be the first block in the file")

    return errors

def main():
    all_errors = []
    for file_path in sys.argv[1:]:
        if file_path.endswith('.tf'):
            all_errors.extend(check_terraform_locals_position(file_path))

    if all_errors:
        for error in all_errors:
            print(error)
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
