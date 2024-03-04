import logger
import sys
import os

class LoggerModule(object):
    def __init__(self, name_module):
        self.module_color = None
        self.name_module = name_module
        self.logger = None

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def _set_name_module(self, name_module):
        self.name_module = name_module
        self.module_color = 'fg #656864'


    def _printout_logger(self):
        self.log_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | " +
            f"<{self.module_color}>{self.name_module}</{self.module_color}> | " +
            "<level>{message}</level>"
        )
        logger.remove()
        logger.add(sys.stderr, format=self.log_format)
        self.logger = logger.opt(colors=True)

    def save_log(self, save_path: str = ''):
        self.logger.add(os.path.join(save_path, f'{self.name_module}.log'),
                         rotation="500 MB",
                         retention="30 days",
                         format=self.log_format)


