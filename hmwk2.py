class Car:
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed

    def show_info(self):
        print("Brand: {}, Color: {}, Speed: {} mph".format(self.brand, self.color, self.speed))

    def drive(self):
        print("The car is moving!")

car1 = Car("Toyota", "Red", 100)
car2 = Car("Ford", "Blue", 120)

car1.show_info()
car2.show_info()

car1.drive()
car2.drive()
