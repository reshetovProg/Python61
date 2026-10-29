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
        Taxi.nums.add(num)

    def __str__(self):
        return f"num: {self.num} | {self.driver} {self.color} {self.model}"



if __name__ == '__main__':
    try:
        car1 = Taxi("a678po", "Alex", "red", "Opel")
        print(car1)
        car2 = Taxi("a678po", "Pol", "red", "Opel")
        print(car2)
    except ValueError as er:
        print(er)
