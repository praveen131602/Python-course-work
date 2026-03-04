while True:
    print("\n--- ATM Simulation Menu ---")
    print("1. Check Average transection (ZeroDivisionError)")
    print("2.withdrawl eith invalid input(ValueError)")
    print("3.diposite with invalid data type(TypeError)")
    print("4.access invalid transection history(IndexError)")
    print("5.Access Non-Existing Account (KeyError)")
    print("6.Read missing trancsaction log file (FileNotFoundError)")
    print("7.Exit")

choice = input("select an option (1-7):")

if choice == "1":
    zero_division_error_case()
elif choice == "2":
    value_error_case()
elif choice == "3":
    type_error_case()
elif choice == "4":
    index_error_case()
elif choice == "5":
    key_error_case()
elif choice == "6":
    file_not_found_error_case()
elif choice == "7":
    print("error")
