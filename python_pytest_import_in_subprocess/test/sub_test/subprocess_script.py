import logging
import os
import sys

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
log_handler = logging.StreamHandler(sys.stdout)
log_handler.setLevel(logging.DEBUG)
root_logger.addHandler(log_handler)

logging.info("PATH: %s", sys.path)
logging.info("CWD: %s", os.getcwd())
logging.info("FILE: %s", os.path.dirname(__file__))

from test.sub_test.sub_test_lib import sub_test_string
logging.info(sub_test_string)
