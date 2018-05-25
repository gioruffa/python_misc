#!/usr/bin/env python
#
# Author: Giorgio Ruffa
# A skeleton for general purpose scripts
# With logging already set up
#

import argparse
import logging
import sys
import os
import datetime


def setup_logging(program_name, console_level=logging.INFO, file_level=logging.DEBUG):
    logger = logging.getLogger(program_name)
    logger.setLevel(file_level)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('{:%Y%m%d}_{}.log'.format(datetime.datetime.now(), program_name))
    fh.setLevel(file_level)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(console_level)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


if __name__ == "__main__" :
    program_name = os.path.splitext(os.path.split(sys.argv[0])[1])[0]
    parser = argparse.ArgumentParser(
        description="Decription of the program"
    )

    logger = setup_logging(program_name)
    logger.info("START")

    logger.info("DONE")
