import logging


class ThirdClass:
    def __init__(self):
        self.enabled = False
        self.logger = logging.getLogger(__name__)

    def err_log(self, exception_info_included: bool):
        try:
            open('/path/to/does/not/exist', 'rb')
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception as e:
            self.logger.error('Failed to open file', exc_info=exception_info_included)
            self.logger.critical('Failed to open file', exc_info=exception_info_included)
