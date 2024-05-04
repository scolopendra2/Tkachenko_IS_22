"""Создайте базовый класс "Человек" со свойствами "имя", "возраст" и "пол". От этого
класса унаследуйте классы "Мужчина" и "Женщина" и добавьте в них свойства,
связанные с социальным положением (например, "семейное положение",
"количество детей" и т.д.)."""


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


class Man(Human):
    def __init__(self, name, age, gender, marital_status, children_count):
        super().__init__(name, age, gender)
        self.marital_status = marital_status
        self.children_count = children_count

    def __str__(self):
        return f'{super().__str__()}\nMarital Status: {self.marital_status}, Children Count: {self.children_count}'


class Woman(Human):
    def __init__(self, name, age, gender, marital_status, children_count):
        super().__init__(name, age, gender)
        self.marital_status = marital_status
        self.children_count = children_count

    def __str__(self):
        return f'{super().__str__()}\nMarital Status: {self.marital_status}, Children Count: {self.children_count}'


if __name__ == '__main__':
    man = Man('Maikl', 42, 'm', 'worker', 3)
    woman = Woman('Larisa', 50, 'f', 'worker', 2)
    print(man)
    print(woman)
