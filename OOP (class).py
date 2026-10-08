class Car:
    def __init__(self, model, age, price):
        self.__model=model
        self.__age=age
        self.__price=price

    def show(self):
        print(f"model: {self.__model}, "
              f"age:{self.__age},"
              f"price:{self.__price}")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_value):
        if new_value<0 or new_value<self.__age:
            raise ValueError("не корректный возраст")
        self.__age=new_value


car1 = Car("merc",0,2000000)
print(car1.age)
car1.age = 8








