from logger import logging

logger1 = logging.getLogger('m1')
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger('m2')
logger2.setLevel(logging.WARNING)

def sum(a,b):
    result = a + b
    logging.debug('the addition of two numbers is happeing')
    return result


sum(5,7)

# log messages 

logger1.debug('this is the debug message for module1')
logger2.warning('this is the warning message for module2')
logger2.warning('this is an warning message')
logger1.error('this is the error message for module1')
logger2.info('this is the info message for module2')
logger2.critical('this is an critical ')