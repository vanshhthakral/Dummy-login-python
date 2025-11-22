# config.py
"""
Configuration file for the dummy login system.

Intentionally INSECURE:
- Hardcoded username and password
- Debug mode enabled
- API key in plain text

These are kept this way on purpose so that
SonarQube can report security issues.
"""

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "Admin@123"  # Hardcoded password (security issue)

API_KEY = "SECRET-API-KEY-12345"  # Another secret in plain text
DEBUG_MODE = True  # Leaving debug mode on in production is bad practice
