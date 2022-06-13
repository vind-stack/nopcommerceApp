import inspect
import logging

class LogGen():
    @staticmethod
    def loggerGen():

        filehandler = logging.FileHandler(".\\Logs\\automation.log")

        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s",
                                      datefmt="%m/%d/%Y %I:%M:%S %p")
        filehandler.setFormatter(formatter)

        loggerName = inspect.stack()[1][3]

        logger = logging.getLogger(loggerName)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger


