import logging
import sys

from test.sub_test.sub_test_lib import sub_test_string

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

log_handler = logging.StreamHandler(sys.stdout)
log_handler.setLevel(logging.DEBUG)

root_logger.addHandler(log_handler)
logging.info(sub_test_string)
