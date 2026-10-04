"""Application entry point for the Library Management System."""

from src.controllers.auth_controller import AuthController
from src.views.book_view import BookView
from src.views.member_view import MemberView
from src.views.loan_view import LoanView
from src.views.search_view import SearchView
from src.views.report_view import ReportView
from src.views.admin_view import AdminView
from src.views.data_view import DataView
from src.utils.logger import get_logger


def show_main_menu(user):
    """Display the menu available to the authenticated user."""
    print("\n" + "=" * 45)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)
    print(f"Logged in: {user.username}")
    print(f"Role: {user.role}")
    print("-" * 45)

    print("1. Manage Books")
    print("2. Manage Members")
    print("3. Manage Loans")
    print("4. Search")
    print("5. Reports")
    print("6. Logout")
    print("8. Data Import / Backup")

    if user.is_admin:
        print("7. Administration")

    print("-" * 45)


def run_application():
    """Run the authentication and main application loop."""
    auth = AuthController()

    print("=" * 45)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)

    user = auth.login()

    if user is None:
        print("\nLogin failed. Maximum attempts reached.")
        return

    logger = get_logger(__name__)
    logger.info("Application login succeeded for user=%s role=%s", user.username, user.role)
    print(f"\nWelcome, {user.username}!")
    print(f"Role: {user.role}")

    book_view = BookView()
    member_view = MemberView()
    loan_view = LoanView()
    search_view = SearchView()
    report_view = ReportView()
    admin_view = AdminView()
    data_view = DataView()

    while True:
        show_main_menu(user)

        choice = input("Select an option: ").strip()

        # Logout
        if choice == "6":
            auth.logout()
            logger.info("User logged out")
            print("\nLogged out successfully.")
            break

        # Administration - Administrator only
        if choice == "7":
            if user.is_admin:
                admin_view.show_menu(user)
            else:
                print(
                    "\nAccess denied. "
                    "Administrator privileges are required."
                )
            continue

        # Data import / backup
        if choice == "8":
            data_view.show_menu()
            continue

        # Book Management
        if choice == "1":
            book_view.show_menu()

        # Member Management
        elif choice == "2":
            member_view.show_menu()

        # Loan Management
        elif choice == "3":
            loan_view.show_menu()

        # Search
        elif choice == "4":
            search_view.show_menu()

        # Reports
        elif choice == "5":
            report_view.show_menu()

        else:
            print("\nInvalid option. Please try again.")


def main():
    """Start the application."""
    run_application()


if __name__ == "__main__":
    main()
