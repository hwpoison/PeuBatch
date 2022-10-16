import sys
import logging 

# File log
peu_handler = logging.FileHandler('logs/log.log')

# stdout 
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)

# configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] : %(levelname)s : %(message)s ( %(name)s ,  %(filename)s )',
    handlers=[peu_handler, stdout_handler]
)

# global logger
logger = logging.getLogger('')
