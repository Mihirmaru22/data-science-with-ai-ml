from logger import logging

def add(a,b):
    logging.debug('the addition option is taking place')
    return a+b


logging.debug('the function calling is on ')
add(5,10)