"""
Authentication utilities for the dummy login system.

Improved:
- Removed duplicate validation
- Removed insecure logging of passwords
- Added exception handling
"""

from config import ADMIN_USERNAME, ADMIN_PASSWORD


def validate_credentials(username: str, password: str) -> bool:
    try:
        return username == ADMIN_USERNAME and password == ADMIN_PASSWORD
    except Exception:
        return False
