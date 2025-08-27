import logging



logging.basicConfig(

    level=logging.DEBUG,
    format='%(asctime)s-%(levelname)s-%(message)s',
    datefmt='%Y-%M-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('now.log'),
        logging.StreamHandler()
    ]
    
)

