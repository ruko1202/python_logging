import logging.config

from python_logging.first_class import FirstClass
from python_logging.python_logging_mod2.second_class import SecondClassTwo
from python_logging.python_logging_mod2.python_logging_mod3.third_class import ThirdClass

logging.config.fileConfig("logging.conf")

if __name__ == "__main__":
    number = FirstClass()
    sys_handler = SecondClassTwo()
    for i in range(0, 1):
        sys_handler2 = ThirdClass()

        sys_handler.enable_system()
        number.increment_number()
        number.decrement_number()
        number.clear_number()
        sys_handler.disable_system()

        sys_handler2.err_log(exception_info_included=False)
        sys_handler2.err_log(exception_info_included=True)

