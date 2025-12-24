# Longwave Git Hooks <!-- omit in toc -->

Repository centralizzata per git hooks riutilizzabili nei progetti Longwave.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Intro](#intro)
- [Hooks Disponibili](#hooks-disponibili)
  - [Terraform Naming Check](#terraform-naming-check)
  - [Terraform Comments Check](#terraform-comments-check)
  - [Terraform Locals Position Check](#terraform-locals-position-check)
- [Utilizzo](#utilizzo)
  - [Prerequisiti](#prerequisiti)
  - [Installazione](#installazione)
  - [Configurazione](#configurazione)
- [Sviluppo](#sviluppo)
  - [Aggiungere Nuovi Hooks](#aggiungere-nuovi-hooks)
  - [Testing](#testing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Intro

Questa repository contiene git hooks personalizzati per garantire qualità e coerenza del codice nei progetti Longwave.

Gli hooks sono implementati come script Python e utilizzano il framework [pre-commit](https://pre-commit.com/) per l'integrazione nei repository.

## Hooks Disponibili

### Terraform Naming Check

**File:** `hooks/check-terraform-naming.py`

Verifica che tutte le risorse Terraform seguano la convenzione `snake_case` invece di `kebab-case`.

**Controlla:**

- `resource`
- `data`
- `module`
- `output`
- `variable`
- `locals`

**Esempio errore:**

```text
main.tf:10: resource 'my-bucket' uses kebab-case. Use snake_case instead.
```

### Terraform Comments Check

**File:** `hooks/check-terraform-comments.py`

Verifica che i commenti Terraform utilizzino solo la sintassi `#` e non `//` o `/* */`.

**Esempio errore:**

```text
main.tf:5: Use '#' for comments, not '//'
```

### Terraform Locals Position Check

**File:** `hooks/check-terraform-comments.py`

Verifica che i blocchi `locals` siano posti come primi blocchi nei file e che ve ne sia massimo 1.

**Esempio errore:**

```text
main.tf:5: : multiple locals blocks found, only one is allowed
main.tf:5: : locals block must be the first block in the file
```

## Utilizzo

### Prerequisiti

- Python >= 3.10
- Git

### Installazione

1. Installa pre-commit:

   ```bash
   pip install pre-commit
   ```

2. Nel tuo progetto, crea o aggiorna `.pre-commit-config.yaml`:

   ```yaml
   repos:
     - repo: https://github.com/llw-RnD/longwave-terraform-git-hooks
       rev: v1.0.0  # Usa l'ultima versione disponibile
       hooks:
         - id: terraform-naming
         - id: terraform-comments
         - id: terraform-locals-position
   ```

3. Installa gli hooks:

   ```bash
   pre-commit install
   ```

### Configurazione

Gli hooks si attivano automaticamente ad ogni commit sui file `.tf`.

Per eseguire manualmente su tutti i file:

```bash
pre-commit run --all-files
```

Per eseguire un hook specifico:

```bash
pre-commit run terraform-naming --all-files
```

## Sviluppo

### Aggiungere Nuovi Hooks

1. Crea lo script Python in `hooks/`:

   ```python
   #!/usr/bin/env python3
   import sys

   def main():
       # La tua logica qui
       return 0

   if __name__ == '__main__':
       sys.exit(main())
   ```

2. Aggiungi l'hook in `.pre-commit-hooks.yaml`:

   ```yaml
   - id: my-new-hook
     name: My New Hook
     entry: hooks/my-new-hook.py
     language: python
     files: \\.tf$
   ```

3. Testa localmente prima di committare

### Testing

Per testare gli hooks localmente:

```bash
# Installa in modalità development
pre-commit install

# Testa su file specifici
python hooks/check-terraform-naming.py path/to/file.tf

# Testa con pre-commit
pre-commit run --all-files
```
