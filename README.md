# Longwave Terraform Template <!-- omit in toc -->

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Intro](#intro)
- [Using this as Git Template](#using-this-as-git-template)
- [Development Setup](#development-setup)
  - [Pre-commit Hooks](#pre-commit-hooks)
- [Actions](#actions)
  - [On Pull Requests](#on-pull-requests)
  - [On Push](#on-push)
- [Requirements](#requirements)
- [Providers](#providers)
- [Modules](#modules)
- [Resources](#resources)
- [Inputs](#inputs)
- [Outputs](#outputs)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Intro

Questo progetto è da usare come punto di partenza per creare un progetto o modulo terraform da zero.

Usando questo template verrà configurato un progetto con:

- Github Action per la generazione della documentazione Terraform automatica
- Github Action per la generazione di versioni tramite taggin secondo gli standard [SEMVER](https://semver.org/lang/it/) partendo da [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- Github Action per la creazione/aggiornamento automatico dell'indice `table-of-content`
- Github hooks che controllano la conformità del codice prima del commit:
  - Rimozione degli spazi inutili al termine delle righe
  - [Aggiunge esattamente una linea vuota al termine di ogni file](https://stackoverflow.com/questions/729692/why-should-text-files-end-with-a-newline)
  - Check se dei file di grandi dimensioni sono stati aggiunti alla repository
  - Check sulla sintassi dei commit secondo lo standard [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
  - Formattazione sintassi Terraform tramite `terraform fmt -recursive`
  - Validazione del codice tramite `terraform validate`
  - Check sui nomi delle risorse in modo che seguano lo standard terraform `snake_case`
  - Check sulla presenza solo di commenti single-line `#` invece dei deprecati multi-line`/* */`

## Using this as Git Template

**IMPORTANT!!!**

IF you are using this repo as a template to create a new one, for a Terraform module, there are some changes to apply before proceeding to commit on the new Repo:

1. Delete completely the `CHANGELOG.md` file, to avoid wrong versions or description.
2. Update the file `package.json` with the correct info about the starting version, or author or anything else.

## Development Setup

### Pre-commit Hooks

This repository uses pre-commit hooks to ensure code quality and consistency.

**Prerequisites:**

- Python >= 3.10 ([Download here](https://www.python.org/downloads/))

**Setup (one-time per developer):**

```bash
# Install pre-commit (if not already installed)
pip install pre-commit

# Install the git hooks
pre-commit install
```

**What it does:**

- Automatically formats Terraform code with `terraform fmt`
- Validates Terraform syntax with `terraform validate`

**Manual run (optional):**

```bash
pre-commit run --all-files
```

## Actions

### On Pull Requests

When a `Pull Request` is opened or updated, an action to create or update the module's README is triggered.

Upon termination the action pushes the updated code the the same `Pull Request`, with a commed that doesn't trigger a new one.

After the git push is done the code markdown linting is checked to check the syntax correctness.

### On Push

When a `Push` is made to the `main` branch, an action to create a `tag`, a `release` and a `changelog` udpate is triggered.

<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.5.7 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_random"></a> [random](#provider\_random) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [random_id.example](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/id) | resource |
| [random_string.example_snake_case](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/string) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_aws_profile"></a> [aws\_profile](#input\_aws\_profile) | n/a | `string` | `"my-profile"` | no |
| <a name="input_aws_region"></a> [aws\_region](#input\_aws\_region) | n/a | `string` | `"eu-south-1"` | no |

## Outputs

No outputs.
<!-- END_TF_DOCS -->
