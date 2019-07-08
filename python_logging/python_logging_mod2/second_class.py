import logging


class SecondClassTwo(object):
    def __init__(self):
        self.enabled = False
        self.logger = logging.getLogger(__name__)

    def enable_system(self):
        self.logger.warning('Включение системы!')
        self.enabled = True

    def disable_system(self):
        self.logger.warning('Выключение системы!')
        self.enabled = False
