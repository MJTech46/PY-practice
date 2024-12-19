
# Python Code Cleanup with `pylint`

This repository demonstrates how to identify and remove unused variables and imports in a Python script using the `pylint` tool.

## Example Script

The provided example script (`sample_script.py`) intentionally includes unused imports, variables, and objects for demonstration purposes.

### Original Script

The original script contains:
- **Unused imports**: Modules that are imported but not used.
- **Unused variables**: Variables that are defined but never used.
- **Unused lambda function**: A lambda function that is declared but not utilized.

### Steps to Identify Unused Code

1. Install `pylint`:
   ```bash
   pip install pylint
   ```

2. Run `pylint` on the script:
   ```bash
   pylint sample_script.py
   ```

3. Observe the output warnings for:
   - **Unused imports**: `W0611: Unused import ...`
   - **Unused variables**: `W0612: Unused variable ...`

### Cleaned-Up Script

The cleaned-up version of the script removes all unused code while retaining the necessary functionality.

### Tools Used

- **pylint**: A static code analysis tool for Python to detect coding errors and enforce coding standards.

---

Happy Coding! 🎉
