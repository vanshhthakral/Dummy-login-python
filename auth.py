# auth.py
"""
Authentication utilities for the dummy login system.

This file intentionally contains:
- Duplicate logic (two similar validate functions)
- Insecure logging of credentials
"""

from config import ADMIN_USERNAME, ADMIN_PASSWORD


def validate_credentials(username: str, password: str) -> bool:
    """
    Insecure validation:
    - Uses hardcoded credentials
    - No hashing / encryption
    - No rate limiting / brute-force protection
    """
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True
    else:
        return False


def insecure_audit_log(username: str, password: str):
    """
     BAD PRACTICE:
    Logs plaintext password to a file 'audit_log.txt'.

    This is intentionally insecure so that SonarQube
    can report it as a vulnerability.
    """
    with open("audit_log.txt", "a", encoding="utf-8") as f:
        f.write(f"LOGIN ATTEMPT: user={username}, password={password}\n")


def validate_again_in_a_bad_way(username: str, password: str) -> bool:
    """
    Almost duplicate of validate_credentials (code smell: duplication).
    This is here to generate code smell / duplication warnings.
    """
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True
    else:
        return False
