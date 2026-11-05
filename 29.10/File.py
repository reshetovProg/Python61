from Taxi import *
from User import *
class File:
    def __init__(self, filename):
        self.filename=filename

    def get_lines(self):
        with open(self.filename, 'r', encoding="UTF-8") as file:
            ls = list()
            for i in file.readlines():
                ls.append(i)
            return ls

if __name__ == '__main__':
    taxi_db = File("taxi.csv")
    cars_lines = taxi_db.get_lines()
    for i in range(1, len(cars_lines)):
        car = cars_lines[i].split(',')
        Taxi(car[0],car[1],car[2],car[3])
    show_all_taxi()


    user_db = File("user.csv")
    users_lines = user_db.get_lines()
    for i in range(1, len(users_lines)):
        User(users_lines[i])
    show_all_users()



