"""
Twitter Amnesia

A service which can be deployed to erase tweets older than a specific date and not marked with a custom tag
"""

import logging
import sys
import datetime

import twitter

from dateutil.relativedelta import *

from twitter_amnesia.helpers import custom_logging_callback, logger_module_name
from twitter_amnesia.arg_parsing import parse_arguments

# Initialize Exception Hook
sys.excepthook = (lambda tp, val, tb: custom_logging_callback(logging.getLogger(), logging.ERROR, tp, val, tb))


# Initialize logger for this module
__log_format = '[{asctime:^s}][{levelname:^8s}]: {message:s}'
__log_format_debug = '[{asctime:^s}][{levelname:^8s}][{name:s}|{funcName:s}|{lineno:d}]: {message:s}'
__log_datefmt = '%Y/%m/%d|%H:%M:%S.%f (%Z)'
__log = logging.getLogger(logger_module_name(__file__))

# seven_days_before = datetime.now() - relativedelta(days=-7)

def main():
    try:
        parsed_args = parse_arguments()
        if sys.flags.debug:
            logging.basicConfig(format=__log_format_debug, datefmt=__log_datefmt, style='{', level=logging.DEBUG)
        else:
            logging.basicConfig(format=__log_format, datefmt=__log_datefmt, style='{', level=parsed_args.logLevel)

        __log.info(
            ''.join(['CLI arguments: ']+list(
                            ('  {:s}: {:s}'.format(str(key), str(data)) for (key, data) in vars(parsed_args).items())
                        )
                    )
        )


    except Exception:
        custom_logging_callback(__log, logging.ERROR, *sys.exc_info())
        exit(-1)

    __log.info("It's done!")
    exit(0)


if __name__ == '__main__':
    main()
