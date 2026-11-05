from Order import *

users = set()

def show_all_users():
    for i in users:
        print(i)

class User:
    __user_counter = 1
    def __init__(self, name):
        self.id = User.__user_counter
        self.name = name
        self.__count_of_orders = 0
        self.order=None
        User.__user_counter+=1
        users.add(self)

    def __str__(self):
        return f"{self.id}: {self.name}| {self.__count_of_orders}"

    @staticmethod
    def get_user_count():
        return (User.__user_counter)-1

    def create_order(self, depart, destination):
        if not self.order:
            self.order = Order(depart, destination, self.id)
            self.__count_of_orders+=1

if __name__ == '__main__':
    car1 = Taxi("a678po", "Alex", "red", "Opel")
    car3 = Taxi("a678oo", "Pol", "red", "Opel")
    car4 = Taxi("a678om", "Pol", "red", "Opel")

    user1 = User("Pol")
    user1.create_order("1","2")
    print(user1.order)
