#!/usr/bin/env python3
import re
import sys

def check_terraform_naming(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []

    # Check resource/data blocks (have two quoted strings)
    resource_pattern = r'(resource|data)\s+"[^"]+"\s+"([a-zA-Z0-9_-]+)"'
    for match in re.finditer(resource_pattern, content):
        block_type = match.group(1)
        name = match.group(2)
        line_num = content[:match.start()].count('\n') + 1
        if '-' in name:
            errors.append(f"{file_path}:{line_num}: {block_type} '{name}' uses kebab-case. Use snake_case instead.")
        if any(c.isupper() for c in name):
            errors.append(f"{file_path}:{line_num}: {block_type} '{name}' contains uppercase letters. Use snake_case instead.")

    # Check output/variable blocks
    single_name_pattern = r'(output|variable)\s+"([a-zA-Z0-9_-]+)"'
    for match in re.finditer(single_name_pattern, content):
        block_type = match.group(1)
        name = match.group(2)
        line_num = content[:match.start()].count('\n') + 1
        if '-' in name:
            errors.append(f"{file_path}:{line_num}: {block_type} '{name}' uses kebab-case. Use snake_case instead.")
        if any(c.isupper() for c in name):
            errors.append(f"{file_path}:{line_num}: {block_type} '{name}' contains uppercase letters. Use snake_case instead.")

    # Check locals block for variable names
    locals_pattern = r'locals\s*\{([^}]+)\}'
    for match in re.finditer(locals_pattern, content, re.DOTALL):
        locals_content = match.group(1)
        var_pattern = r'^\s*([a-zA-Z0-9_-]+)\s*='
        for var_match in re.finditer(var_pattern, locals_content, re.MULTILINE):
            var_name = var_match.group(1)
            line_num = content[:match.start() + var_match.start()].count('\n') + 1
            if '-' in var_name:
                errors.append(f"{file_path}:{line_num}: local '{var_name}' uses kebab-case. Use snake_case instead.")
            if any(c.isupper() for c in var_name):
                errors.append(f"{file_path}:{line_num}: local '{var_name}' contains uppercase letters. Use snake_case instead.")

    # Check module blocks (have one quoted string)
    module_pattern = r'module\s+"([a-zA-Z0-9_-]+)"'
    for match in re.finditer(module_pattern, content):
        name = match.group(1)
        line_num = content[:match.start()].count('\n') + 1
        if '-' in name:
            errors.append(f"{file_path}:{line_num}: module '{name}' uses kebab-case. Use snake_case instead.")
        if any(c.isupper() for c in name):
            errors.append(f"{file_path}:{line_num}: module '{name}' contains uppercase letters. Use snake_case instead.")

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
