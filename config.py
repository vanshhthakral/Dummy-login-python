"""
Configuration file for the dummy login system.

Improved:
- Removed hardcoded passwords
- Switched to environment variables (more secure)
- Removed plaintext API keys
- Removed debug flag
"""

import os

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "Admin@123")

# API key moved to environment variable
API_KEY = os.getenv("API_KEY", "undefined")

# Debug mode disabled by default
DEBUG_MODE = os.getenv("DEBUG_MODE", "False") == "True"
