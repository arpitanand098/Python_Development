
import logging

## Logging settings

logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arithmetic Application")

def add(x,y):
    result = x + y
    logger.debug(f"{x} + {y} = {result}")
    return result

def subtract(x,y):
    result = x - y
    logger.debug(f"{x} - {y} = {result}")
    return result

def multiply(x,y):
    result = x * y
    logger.debug(f"{x} * {y} = {result}")
    return result

def divide(x,y):
    try:
        result = x / y
        logger.debug(f"{x} / {y} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero is not allowed.")
        return None

add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 5)
