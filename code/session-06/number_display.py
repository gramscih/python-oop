class NumberDisplay:
    def __init__(self , value, limit):
        self.__value = value
        self.__limit = limit

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value = new_value

    def increment(self):
        # self.__value = self.__value + 1

        # self.__value += 1
        # if self.__value == self.__limit:
        #     self.__value = 0
        
        self.__value = (self.__value + 1) % self.__limit

    def display(self):
        """
        This function should display 00:00 23:45
        """
        if self.__value < 10:
            return f"0{self.__value}"
        else:
            return self.__value

    # def __str__(self):
    #     pass
            