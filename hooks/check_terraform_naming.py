#!/usr/bin/env python3
import hcl2
import sys

def check_terraform_naming(file_path):
    errors = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            parsed = hcl2.load(f)
    except Exception:
        return errors

    # Check resources: resource -> [{ resource_type: { resource_name: {...} } }]
    for resource_block in parsed.get('resource', []):
        for resource_type, resources in resource_block.items():
            for name in resources.keys():
                if '-' in name:
                    errors.append(f"{file_path}: resource '{name}' uses kebab-case. Use snake_case instead.")
                if any(c.isupper() for c in name):
                    errors.append(f"{file_path}: resource '{name}' contains uppercase letters. Use snake_case instead.")

    # Check data sources: data -> [{ data_type: { data_name: {...} } }]
    for data_block in parsed.get('data', []):
        for data_type, data_sources in data_block.items():
            for name in data_sources.keys():
                print(f"Data name {name}")
                if '-' in name:
                    errors.append(f"{file_path}: data '{name}' uses kebab-case. Use snake_case instead.")
                if any(c.isupper() for c in name):
                    errors.append(f"{file_path}: data '{name}' contains uppercase letters. Use snake_case instead.")

    # Check outputs: output -> [{ output_name: {...} }]
    for output in parsed.get('output', []):
        for name in output.keys():
            if '-' in name:
                errors.append(f"{file_path}: output '{name}' uses kebab-case. Use snake_case instead.")
            if any(c.isupper() for c in name):
                errors.append(f"{file_path}: output '{name}' contains uppercase letters. Use snake_case instead.")

    # Check variables: variable -> [{ variable_name: {...} }]
    for variable in parsed.get('variable', []):
        for name in variable.keys():
            if '-' in name:
                errors.append(f"{file_path}: variable '{name}' uses kebab-case. Use snake_case instead.")
            if any(c.isupper() for c in name):
                errors.append(f"{file_path}: variable '{name}' contains uppercase letters. Use snake_case instead.")

    # Check locals: locals -> [{ local_name: value }]
    for locals_block in parsed.get('locals', []):
        for name in locals_block.keys():
            if '-' in name:
                errors.append(f"{file_path}: local '{name}' uses kebab-case. Use snake_case instead.")
            if any(c.isupper() for c in name):
                errors.append(f"{file_path}: local '{name}' contains uppercase letters. Use snake_case instead.")

    # Check modules: module -> [{ module_name: {...} }]
    for module in parsed.get('module', []):
        for name in module.keys():
            if '-' in name:
                errors.append(f"{file_path}: module '{name}' uses kebab-case. Use snake_case instead.")
            if any(c.isupper() for c in name):
                errors.append(f"{file_path}: module '{name}' contains uppercase letters. Use snake_case instead.")

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
