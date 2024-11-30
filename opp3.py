class Car:
    _car_count = 0  # Protected: Yaratilgan mashinalar soni (klass o'zgaruvchisi)

    def __init__(self, name, distance, year):
        self.name = name  # Mashina nomi (public)
        self._distance = distance  # Protected: Masofa (km)
        self.__year = year  # Private: Ishlab chiqarilgan yil
        Car._car_count += 1
        self.__car_id = Car._car_count  # Private: Mashina ID

    # Public method: Mashina haqida umumiy ma'lumot
    def __str__(self) -> str:
        return f"\n\nName: {self.name},\nDistance: {self._distance} km,\nYear: {self.__year},\nID: {self.__car_id}"

    # Getter: Shaxsiy (private) yil qiymatini olish
    @property
    def year(self):
        return self.__year

    # Setter: Yilni yangilash
    @year.setter
    def year(self, new_year):
        if new_year > 1886:  # Mashina yili 1886 yildan katta bo'lishi kerak
            self.__year = new_year
        else:
            print("Error: Year must be greater than 1886!")

    # Getter: Masofani olish
    def get_distance(self):
        return self._distance

    # Setter: Masofani yangilash
    def set_distance(self, distance):
        if distance > 0:
            self._distance = distance
        else:
            print("Distance cannot be negative or zero!")

    # Class method: Jami mashinalar sonini qaytarish
    @classmethod
    def get_total_cars(cls):
        return f"Total cars created: {cls._car_count}"

    # Static method: Mashina yoshini hisoblash
    @staticmethod
    def calculate_age(year):
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - year

# Mashina obyektini yaratish
car1 = Car(name="Nexia", distance=259, year=2019)

# Setter yordamida yilni o'zgartirish
car1.year = 2010

# Mashina haqida umumiy ma'lumotlarni chiqarish
print(car1)

# Mashinaning yoshini hisoblash
print(f"Car's age: {car1.calculate_age(car1.year)} years")
