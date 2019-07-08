import logging


class FirstClass:
    def __init__(self):
        self.current_number = 0
        self.logger = logging.getLogger(__name__)

    def increment_number(self):
        self.logger.info('Число увеличивается!')
        self.current_number += 1
        self.logger.debug(f'Число: {self.current_number}')

    def decrement_number(self):
        self.logger.info('Число уменьшается!')
        self.current_number -= 1
        self.logger.debug(f'Число: {self.current_number}')

    def clear_number(self):
        self.logger.warning('Очистка значения!')
        self.current_number = 0
        self.logger.debug(f'Число: {self.current_number}')
