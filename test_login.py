"""
Quick standalone test of the login flow (FR-1, FR-2), before the full
menu system exists.

Usage:
  1. Place this file in the root of your repo (same level as src/, database/).
  2. Make sure database/app.db exists and seed_users.py has been run.
  3. Run:  python test_login.py
  4. Log in with:  admin / Admin123!   or   librarian1 / Staff123!
"""

from src.controllers.auth_controller import AuthController

if __name__ == "__main__":
    controller = AuthController()
    user = controller.login()

    if user is not None:
        print(f"Logged in as: {user}")
        print(f"Is admin? {user.is_admin}")
        controller.logout()
        print("Logged out.")
    else:
        print("Login failed after all attempts.")
