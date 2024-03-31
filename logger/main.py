# This is a sample main file for the logger

import logging

def setup_logging(log_file):
    # Set up logging to a file
    logging.basicConfig(filename=log_file, level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

