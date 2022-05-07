class car:
    def __init__(self, speed, color):
        self.__speed__=speed
        self.__color__=color

    def set_speed(self, value):
        self.__speed__=value

    def get_speed(self):
        return self.__speed__

    def set_color(self, value):
        self.__color__ = value

    def get_color(self):
        return self.__color__


honda=car(180,'Red')
audi=car(250,'blue')
print(honda)

print(honda.speed)
print(honda.color)

