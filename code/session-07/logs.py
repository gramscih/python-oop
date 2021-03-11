import logging 

logging.basicConfig(filename= 'test.log', level=logging.DEBUG)

class Animal:
    def __init__(self, name, age):
        logging.debug('init: {} created'.format(name))
        self.__name = name
        self.__age = age

    def talk(self, num):
        logging.debug("talk: starting function ...")
        try:
            opr = self.__age + num
        except Exception as ex:
            logging.error("talk: Exception {}".format(ex))    
        logging.info("talk: end process function ...")



duke = Animal("Duke", 4)
duke.talk(3)
duke.talk("3")