class car:
    def __init__(self, speed, color):
        self.__speed=speed
        self.__color=color

    def set_speed(self, value):
        self.__speed=value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color


honda=car(180,'Red')
print(honda.get_speed())
print(honda.get_color())

honda.set_speed(280)
print(honda.get_color())
print(honda.get_speed())

audi=car(250,'blue')


