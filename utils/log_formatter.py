import logging as log
import time

from colorama import Style, Fore

class CustomFormatter(log.Formatter):
    format = "[%(levelname)-6s] " + Style.RESET_ALL + " " + Fore.WHITE + "%(message)s" + Style.RESET_ALL
    FORMATS = {
        log.DEBUG: Fore.BLUE + format + Style.RESET_ALL,
        log.INFO: Fore.GREEN + format + Style.RESET_ALL,
        log.WARNING: Fore.YELLOW + format + Style.RESET_ALL,
        log.ERROR: Fore.RED + format + Style.RESET_ALL,
        log.CRITICAL: Fore.RED + Style.BRIGHT + format + Style.RESET_ALL
    }

    def __init__(self):
        super().__init__()
        self.start_time = time.time()

    def format(self, record):
        # Calculate the elapsed time in ticks
        record.ticks = int((time.time() - self.start_time) * 1000)
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = log.Formatter(log_fmt)
        return formatter.format(record)
