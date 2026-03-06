# Longwave Git Hooks <!-- omit in toc -->

Centralized repository for reusable git hooks in Longwave projects.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Intro](#intro)
- [Available Hooks](#available-hooks)
  - [Terraform Naming Check](#terraform-naming-check)
  - [Terraform Comments Check](#terraform-comments-check)
  - [Terraform Locals Position Check](#terraform-locals-position-check)
- [Usage](#usage)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Development](#development)
  - [Adding New Hooks](#adding-new-hooks)
  - [Testing](#testing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Intro

This repository contains custom git hooks to ensure code quality and consistency across Longwave projects.

Hooks are implemented as Python scripts and use the [pre-commit](https://pre-commit.com/) framework for repository integration.

## Available Hooks

### Terraform Naming Check

**File:** `hooks/check-terraform-naming.py`

Validates that all Terraform resources follow `snake_case` naming convention instead of `kebab-case`.

**Checks:**

- `resource`
- `data`
- `module`
- `output`
- `variable`
- `locals`

**Error example:**

```text
main.tf:10: resource 'my-bucket' uses kebab-case. Use snake_case instead.
```

### Terraform Comments Check

**File:** `hooks/check-terraform-comments.py`

Validates that Terraform comments use only `#` syntax and not `//` or `/* */`.

**Error example:**

```text
main.tf:5: Use '#' for comments, not '//'
```

### Terraform Locals Position Check

**File:** `hooks/check-terraform-comments.py`

Validates that `locals` blocks are placed as the first block in files and that there is only one per file.

**Error example:**

```text
main.tf:5: : multiple locals blocks found, only one is allowed
main.tf:5: : locals block must be the first block in the file
```

## Usage

### Prerequisites

- Python >= 3.10
- Git

### Installation

1. Install pre-commit:

   ```bash
   pip install pre-commit
   ```

2. In your project, create or update `.pre-commit-config.yaml`:

   ```yaml
   repos:
     - repo: https://github.com/longwave-innovation-lab/longwave-terraform-git-hooks
       rev: v0.2.0  # Use the latest available version
       hooks:
         - id: terraform-naming
         - id: terraform-comments
         - id: terraform-locals-position
   ```

3. Install the hooks:

   ```bash
   pre-commit install
   ```

### Configuration

Hooks automatically run on every commit for `.tf` files.

To run manually on all files:

```bash
pre-commit run --all-files
```

To run a specific hook:

```bash
pre-commit run terraform-naming --all-files
```

## Development

### Adding New Hooks

1. Create the Python script in `hooks/`:

   ```python
   #!/usr/bin/env python3
   import sys

   def main():
       # Your logic here
       return 0

   if __name__ == '__main__':
       sys.exit(main())
   ```

2. Add the hook to `.pre-commit-hooks.yaml`:

   ```yaml
   - id: my-new-hook
     name: My New Hook
     entry: hooks/my-new-hook.py
     language: python
     files: \\.tf$
   ```

3. Test locally before committing

### Testing

To test hooks locally:

```bash
# Install in development mode
pre-commit install

# Test on specific files
python hooks/check-terraform-naming.py path/to/file.tf

# Test with pre-commit
pre-commit run --all-files
```
