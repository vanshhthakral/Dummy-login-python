"""
Main entry point for the dummy login system.

Improved:
- Removed plaintext logging
- Added input validation
- Added exception handling
- Removed duplicate validation logic
"""

from auth import validate_credentials


def show_menu():
    print("===== Dummy Login System =====")
    print("1. Login")
    print("2. Exit")


def login_flow():
    try:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if not username or not password:
            print("\n❌ Username and password cannot be empty.\n")
            return

        if validate_credentials(username, password):
            print(f"\n✅ Login successful. Welcome, {username}!\n")
            secret_admin_panel(username)
        else:
            print("\n❌ Invalid credentials!\n")

    except Exception as e:
        print(f"An error occurred: {e}")


def secret_admin_panel(username: str):
    print(f"[ADMIN PANEL] Logged in as: {username}")
    print("1. View users (not implemented)")
    print("2. Delete user (not implemented)")
    print("3. Exit\n")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            login_flow()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
