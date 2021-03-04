# import number_display
from number_display import NumberDisplay

class ClockDisplay:
    def __init__(self, hour, minute):        
        self.__hours = NumberDisplay(hour, 24)
        self.__minute = NumberDisplay(minute, 59)

    def set_time(self, hour, minute):
        self.__hours.set_value(hour)
        self.__minute.set_value(minute)

    def get_time(self):
        pass

    def tick_time(self):
        pass

    def display(self):
        print("{}:{}".format(self.__hours.display(), self.__minute.display()))


clock = ClockDisplay(15, 30)
clock.display()
clock.set_time(5, 5)
clock.display()

clock_2 = ClockDisplay(56, "1233")
clock_2.display()
# general = NumberDisplay(value, limit)
# hour = NumberDisplay(value, limit=50) # limit = 23
# minute = NumberDisplay(value, limit) # 59
# seconds = NumberDisplay(value, limit) # 59