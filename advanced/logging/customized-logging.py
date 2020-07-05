# Demonstrate how to customize logging output

import logging

extData = {'user': 'joem@example.com'} #temporary external data to add to log message


def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extData) #adding extra data to debug message


def main():
    # set the output file and debug level, and
    # use a custom formatting specification
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s" #custom format string with data embeded
    dateStr = "%m/%d/%Y %I:%M:%S %p" #Date formating string
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        format=fmtStr, #formating string
                        datefmt=dateStr) #basic configuration

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherFunction()


if __name__ == "__main__":
    main()
