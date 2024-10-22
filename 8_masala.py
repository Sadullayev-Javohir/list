"""Elementni oxirgi o'ringga ko'chirish. Ro'yxatdagi biror elementni olib, uni oxirgi o'ringa ko'chiring.
cars = ["Toyota", "Ford", "BMW", "Audi"]
Natija: ["Toyota", "BMW", "Audi", "Ford"]"""

cars = ["Toyota", "Ford", "BMW", "Audi"]

del cars[1]
cars.append("Ford")

print(cars)