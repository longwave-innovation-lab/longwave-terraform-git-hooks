#!/usr/bin/env python3
"""Unit tests for Terraform git hooks."""
import pytest
import os
from pathlib import Path
from hooks.check_terraform_naming import check_terraform_naming
from hooks.check_terraform_comments import check_terraform_comments

TESTS_DIR = Path(__file__).parent
TERRAFORM_FILES_DIR = os.path.join(TESTS_DIR, "terraform_files")


class TestTerraformNaming:
    """Test check_terraform_naming hook."""

    def test_snake_case_ok(self):
        """Valid snake_case should pass."""
        file_path = os.path.join(TERRAFORM_FILES_DIR, "snake_case_ok.tf")
        errors = check_terraform_naming(str(file_path))
        assert len(errors) == 0, f"Expected no errors, got: {errors}"

    def test_snake_case_nok(self):
        """Invalid kebab-case should fail."""
        file_path = os.path.join(TERRAFORM_FILES_DIR, "snake_case_nok.tf")
        errors = check_terraform_naming(str(file_path))
        assert len(errors) > 0, "Expected errors for kebab-case naming"
        assert "my-role" in errors[0], "Should detect 'my-role' as invalid"
        assert "my-data_role" in errors[1], "Should detect 'my-data_role' as invalid"
        assert "my-output" in errors[2], "Should detect 'my-output' as invalid"
        assert "my-variable" in errors[3], "Should detect 'my-variable' as invalid"
        assert "my-local" in errors[4], "Should detect 'my-local' as invalid"
        assert "my-module" in errors[5], "Should detect 'my-module' as invalid"
        assert "kebab-case" in errors[0], "Error message should mention kebab-case"

    def test_snake_case_uppercase_nok(self):
        """Invalid kebab-case should fail."""
        file_path = os.path.join(TERRAFORM_FILES_DIR, "snake_case_uppercase_nok.tf")
        errors = check_terraform_naming(str(file_path))
        assert len(errors) > 0, "Expected errors for uppercase naming"
        assert "my_ROLE" in errors[0], "Should detect 'my_ROLE' as invalid"
        assert "my_DATA_ROLE" in errors[1], "Should detect 'my_DATA_ROLE' as invalid"
        assert "my_OUTPUT" in errors[2], "Should detect 'my_OUTPUT' as invalid"
        assert "my_VARIABLE" in errors[3], "Should detect 'my_VARIABLE' as invalid"
        assert "my_LOCAL" in errors[4], "Should detect 'my_LOCAL' as invalid"
        assert "my_MODULE" in errors[5], "Should detect 'my_MODULE' as invalid"
        assert "uppercase" in errors[0], "Error message should mention uppercase"

    def test_locals_with_values_ok(self):
        """Locals with uppercase/special chars in values should pass."""
        file_path = os.path.join(TERRAFORM_FILES_DIR, "locals_with_map_ok.tf")
        errors = check_terraform_naming(str(file_path))
        assert len(errors) == 0, f"Expected no errors for locals with uppercase in values, got: {errors}"


class TestTerraformComments:
    """Test check_terraform_comments hook."""

    def test_comments_ok(self):
        """Valid # comments should pass."""
        file_path = os.path.join(TERRAFORM_FILES_DIR, "comments_ok.tf")
        errors = check_terraform_comments(str(file_path))
        assert len(errors) == 0, f"Expected no errors, got: {errors}"

    def test_comments_nok(self):
        """Invalid // and /* */ comments should fail."""
        file_path = os.path.join(TERRAFORM_FILES_DIR, "comments_nok.tf")
        errors = check_terraform_comments(str(file_path))
        assert len(errors) >= 2, "Expected at least 2 errors (// and /* */)"

        error_text = " ".join(errors)
        assert "//" in error_text or "Use '#'" in error_text, "Should detect // comments"
        assert "/* */" in error_text or "Use '#'" in error_text, "Should detect /* */ comments"

    def test_wildcard_arn_ok(self):
        """/* inside strings should pass."""
        file_path = os.path.join(TERRAFORM_FILES_DIR, "wildcard_arn_ok.tf")
        errors = check_terraform_comments(str(file_path))
        assert len(errors) == 0, f"Expected no errors for /* in strings, got: {errors}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
