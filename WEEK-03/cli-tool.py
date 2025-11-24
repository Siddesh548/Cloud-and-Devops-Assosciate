from ip import check_ip_reachability 
from latency import show_latency_summary

while True:
    print("\n===== MENU =====")
    print("1. IP Reachability Tester")
    print("2. Latency Summary")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        check_ip_reachability()

    elif choice == "2":
        show_latency_summary()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid Choice. Try again.")