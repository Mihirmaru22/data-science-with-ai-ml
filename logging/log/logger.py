import logging

logging.basicConfig(
    filename='what.log',
    filemode= 'w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%M-%d %H:%M:%S'
)