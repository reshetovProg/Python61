from User import *
from Taxi import *

def create_order(user: User):
    depart = input("enter department: ")
    destination = input("enter destination: ")
    user.create_order(depart, destination)
    print(user.order)


if __name__ == '__main__':
    user = User("vlad")
    car1 = Taxi("a678po", "Alex", "red", "Opel")
    car3 = Taxi("a678oo", "Pol", "red", "Opel")
    car4 = Taxi("a678om", "Pol", "red", "Opel")
    while True:
        print("MENU")
        print("1. Create Order")
        print("2. Show free taxi")
        print("3. Profile User")
        print("4. Show order")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            create_order(user)
        elif user_choice == "2":
            all = show_all_free_taxi()
        elif user_choice == "3":
            print(user)
        elif user_choice == "4":
            print(user.order)
        else:
            print("Invalid choice")

