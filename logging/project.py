import logging

# logging setting 

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%M-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('project.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('module - 1')

def add(a,b):
    result = a + b

    logger.debug(f'addition {a} + {b} = {result}')
    return result

def sub(a,b):
    result = a - b

    logger.debug(f'subtraction {a} - {b} =  {result}')
    return result

add(5,10)
sub(10,5)