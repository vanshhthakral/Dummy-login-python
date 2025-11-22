# login.py
"""
Main entry point for the dummy login system.

This script:
- Shows a simple text menu
- Prompts for username & password
- Calls insecure audit log
- Uses duplicate validation logic
"""

from auth import (
    validate_credentials,
    insecure_audit_log,
    validate_again_in_a_bad_way,
)


def show_menu():
    print("===== Dummy Login System =====")
    print("1. Login")
    print("2. Exit")


def login_flow():
    username = input("Enter username: ")
    password = input("Enter password: ")

    #  Insecure logging of credentials
    insecure_audit_log(username, password)

    # Unnecessary double validation 
    is_valid_first = validate_credentials(username, password)
    is_valid_second = validate_again_in_a_bad_way(username, password)

    if is_valid_first and is_valid_second:
        print(f"\n✅ Login successful. Welcome, {username}!\n")
        secret_admin_panel(username)
    else:
        print("\n❌ Invalid credentials!\n")


def secret_admin_panel(username: str):
    """
    Fake admin panel – not protected properly (just prints options).
    """
    print(f"[ADMIN PANEL] Logged in as: {username}")
    print("1. View users (not implemented)")
    print("2. Delete user (not implemented)")
    print("3. Exit\n")


def main():
    # No input validation, no exception handling (also intentionally weak)
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            login_flow()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
