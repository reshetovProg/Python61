class Drob:
    def __init__(self, num, denom):
        self.whole = 0
        if num>denom:
            self.whole = num // denom
            self.num = num % denom
        else:
            self.num = num
        self.denom = denom

    def __str__(self):
        if self.whole == 0:
            return f"{self.num}/{self.denom}"
        else:
            return f"{self.whole} {self.num}/{self.denom}"

    def add(self, num, denom):
        self.num = self.num*denom + num*self.denom
        self.denom = self.denom * denom
        if num > denom:
            self.whole = self.whole + (self.num // self.denom)
            self.num = self.num % self.denom

    def add_drob(self, drob):
        self.num = self.num * drob.denom + drob.num * self.denom
        self.denom = self.denom * drob.denom
        if drob.num > drob.denom:
            self.whole = self.whole + (self.num // self.denom)
            self.num = self.num % self.denom

    def plus(self, drob):
        new_num = self.num * drob.denom + drob.num * self.denom
        new_denom = self.denom * drob.denom
        if self.whole!=0:
            new_num = self.whole*new_denom+new_num
        return Drob(new_num, new_denom)

    def __add__(self, other):
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        if self.whole != 0:
            new_num = self.whole * new_denom + new_num
        return Drob(new_num, new_denom)

num1 = Drob(20,5)
num2 = Drob(3,7)
num1.add(3,7)
print(num1)

num3 = Drob(20,5)
num4 = Drob(3,7)
num3.add_drob(num4)
print(num3)

num5 = Drob(20,5)
num6 = Drob(3,7)
num7 = num5.plus(num6)
print(num7)

num8 = Drob(20,5)
num9 = Drob(3,7)
num10 = num8 + num9
print(num10)

print(Drob(20,5)+Drob(3,7))


class Product:
    def __init__(self, length):
        self.length = length

    def __add__(self, other):
        return Product(self.length+other.length)

    def __str__(self):
        return str(self.length)

product1 = Product(5)+Product(8)
print(product1) # 13