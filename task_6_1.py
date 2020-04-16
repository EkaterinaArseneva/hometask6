"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод."""

import time
class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        #в условии сказано, что переключение между режимами строго в таком порядке. Хотелось бы зациклить, чтобы обратно
        #красный переключался и т.д.
        print(self.__color[0], end='')
        time.sleep(7)
        print('\r'+self.__color[1], end='')
        time.sleep(2)
        print('\r'+self.__color[2], end='')
        time.sleep(4)
        print('\r'+' ', end='')
    #работает, не по заданию (не останавливается после green)
    # def eternal_running(self):
        # while True:
        #     print('\r' + TrafficLight.color[0], end='')
        #     time.sleep(7)
        #     print('\r' + TrafficLight.color[1], end='')
        #     time.sleep(2)
        #     print('\r' + TrafficLight.color[2], end='')
        #     time.sleep(4)

new_trafficlight = TrafficLight()
new_trafficlight.running()
