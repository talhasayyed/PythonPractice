import os
import conf
import logging
import inspect


def getactlogger(loggername=None):
    # Get the full path to the log file
    filename = os.path.join(conf.LOGGING_DIR, conf.LOGFILE)

    # Automatically set logger name to caller file if __name__ == "__main__"
    if loggername is None or loggername == "__main__":
        caller_frame = inspect.stack()[1]
        caller_module = inspect.getmodule(caller_frame[0])
        if caller_module and hasattr(caller_module, '__file__'):
            loggername = os.path.basename(caller_module.__file__)
        else:
            loggername = "unknown"

    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)  # Set root logger level to DEBUG

    # Avoid adding handlers multiple times
    if not logger.handlers:
        # --- File Handler ---
        fh = logging.FileHandler(filename)
        fh.setLevel(logging.DEBUG)  # Log all levels to file

        # --- Stream Handler (Console) ---
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)  # Log all levels to console

        # --- Formatters ---
        # Detailed format for file logs
        file_formatter = logging.Formatter(
            '%(asctime)s %(name)s::%(module)s:%(lineno)d %(levelname)s - %(message)s'
        )
        # Minimal format for console logs
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')

        # Assign formatters to handlers
        fh.setFormatter(file_formatter)
        ch.setFormatter(console_formatter)

        # Add handlers to logger
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger


# For manual testing
if __name__ == '__main__':
    # log = getactlogger(__name__)
    # or 
    log = getactlogger(os.path.basename(__file__))
    log.debug("This is a test debug log from logger_file.py")
