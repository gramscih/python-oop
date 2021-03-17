from abc import ABC, abstractmethod

class AbstractClass(ABC):

    @abstractmethod
    def virtual_method_must_define(self):
        pass


class SubClass(AbstractClass):
    def virtual_method_must_define(self):
        pass


s = SubClass()
# print(s.virtual_method_must_define())