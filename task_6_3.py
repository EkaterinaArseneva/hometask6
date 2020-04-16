"""Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self._income = Position.income_dict

class Position(Worker):
    income_dict = {}
    def get_full_name(self):
        return self.name
    def get_total_income(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        Position.income_dict[wage]=wage
        Position.income_dict[bonus]=bonus
        return sum(self._income.values())

director = Position('Ivan', 'director')
print(director.get_full_name())
print(director.get_total_income(10, 20))