from Taxi import *
class Order:
    id = 0

    # price, depart, destination, user_id, taxi_number
    def __init__(self, depart, destination, user_id):
        self.id = Order.id
        Order.id += 1
        self.depart = depart
        self.destination=destination
        self.user_id = user_id
        self.taxi = get_free_taxi()
        self.taxi.status = True

    def __str__(self):
        return (f"user: {self.user_id} от:{self.depart} куда:{self.destination}"
                f"\nназначен: {self.taxi}")

if __name__ == '__main__':
    try:
        car1 = Taxi("a678po", "Alex", "red", "Opel")
        car3 = Taxi("a678oo", "Pol", "red", "Opel")
        car4 = Taxi("a678om", "Pol", "red", "Opel")
        order1 = Order("t1", "t2", "1")
        order2 = Order("t1", "t2", "2")
        order3 = Order("t1", "t2", "3")
        order4 = Order("t1", "t2", "4")
    except ValueError as er:
        print(er)
    except AttributeError as er:
        print("нет свободных машин")

    show_all_taxi()
