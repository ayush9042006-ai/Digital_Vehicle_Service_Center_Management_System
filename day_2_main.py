# Digital Vehicle Service Center Management System

def user_authentication():
    print("\n===== USER AUTHENTICATION =====")
    print("This module will be implemented later.")


def record_management():
    print("\n===== RECORD MANAGEMENT =====")
    print("This module will be implemented later.")


def search_functionality():
    print("\n===== SEARCH FUNCTIONALITY =====")
    print("This module will be implemented later.")


def report_generation():
    print("\n===== REPORT GENERATION =====")
    print("This module will be implemented later.")


def file_data_storage():
    print("\n===== FILE-BASED DATA STORAGE =====")
    print("This module will be implemented later.")


def exception_validation():
    print("\n===== EXCEPTION HANDLING & VALIDATION =====")
    print("This module will be implemented later.")


# Main Menu
while True:
    print("\n" + "=" * 50)
    print(" DIGITAL VEHICLE SERVICE CENTER MANAGEMENT SYSTEM ")
    print("=" * 50)

    print("1. User Authentication")
    print("2. Record Management")
    print("3. Search Functionality")
    print("4. Report Generation")
    print("5. File-Based Data Storage")
    print("6. Exception Handling & Validation")
    print("7. Exit")

    choice = input("\n(Enter your choice)(0-7)---->>>>> ")

    if choice == "1":
        user_authentication()
    elif choice == "2":
        record_management()

    elif choice == "3":
        search_functionality()

    elif choice == "4":
        report_generation()

    elif choice == "5":
        file_data_storage()

    elif choice == "6":
        exception_validation()

    elif choice == "7":
        print("\nThank you for using the system.")
        print("Exiting...")
        break

    else:
        print("\nInvalid Choice! Please enter a number between 1 and 7.")