from typing import Set

def validate_num(num: str):
    valid_alpha = 'etopakxcbm'
    if len(num)!=6: return False
    if (num[0] not in valid_alpha
            or num[4] not in valid_alpha
            or num[5] not in valid_alpha):
        return False
    if num[1].isdigit() and num[2].isdigit() and num[3].isdigit():
        return True
    return False

cars = set()

def show_all_taxi():
    for i in cars:
        print(i)

def get_free_taxi():
    for i in cars:
        if not i.status:
            return i

class Taxi:

    nums = set()
    def __init__(self, num, driver, color, model):
        if not validate_num(num):
            raise ValueError("не валидный гос. номер")
        if num in Taxi.nums:
            raise ValueError(f"{num} номер не уникален")
        self.num=num
        self.driver = driver
        self.color = color
        self.model = model
        self.status = False
        Taxi.nums.add(num)
        cars.add(self)

    def __str__(self):
        return f"num: {self.num} | {self.driver} {self.color} {self.model} {self.status}"

    def set_status(self, status):
        self.status = status


if __name__ == '__main__':
    try:
        car1 = Taxi("a678po", "Alex", "red", "Opel")
        print(car1)
        car3 = Taxi("a678oo", "Pol", "red", "Opel")
        car3.set_status(True)
    except ValueError as er:
        print(er)



    print("-----")
    for i in cars:
        print(i)
