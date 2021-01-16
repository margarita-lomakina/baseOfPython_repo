import time


class TrafficLight:
    __color = 'красный'

    def running(self):
        self.__color = 'красный'
        print(self.__color)
        time.sleep(7)
        self.__color = 'жёлтый'
        print(self.__color)
        time.sleep(2)
        self.__color = 'зелёный'
        print(self.__color)
        time.sleep(4)


my_trafficLight = TrafficLight()
my_trafficLight.running()

