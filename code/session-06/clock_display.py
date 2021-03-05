# import number_display
import time

from number_display import NumberDisplay

class ClockDisplay:
    def __init__(self, hour, minute):        
        self.__hours = NumberDisplay(hour, 24)
        self.__minute = NumberDisplay(minute, 60)
        self.__display_str = ""
        self.__update_display()

    def set_time(self, hour, minute):
        self.__hours.set_value(hour)
        self.__minute.set_value(minute)

    def get_time(self):
        """Returns an string that if formated for hours

        Returns:
            [str]: this value represents the time in the following formant 00:00
        """
        return self.__display_str

    def tick_time(self):
        self.__minute.increment()
        if self.__minute.get_value() == 0:
            self.__hours.increment()
        self.__update_display()

    def __update_display(self):
        self.__display_str = "{}:{}".format(self.__hours.display(), self.__minute.display())
        self.__display()

    def __display(self):
        print(self.__display_str)


clock = ClockDisplay(15, 59)

#while <boolean>:
# while True:
#     time.sleep(1)
#     clock.tick_time()
#     # get_time returns a string with this format 15:59
#     if clock.get_time() == "16:59":
#         break
# print(clock.get_time())
# clock.display()
# print(clock.get_time())

# clock_2 = ClockDisplay(56, "1233")
# clock_2.display()
# general = NumberDisplay(value, limit)
# hour = NumberDisplay(value, limit=50) # limit = 23
# minute = NumberDisplay(value, limit) # 59
# seconds = NumberDisplay(value, limit) # 59
