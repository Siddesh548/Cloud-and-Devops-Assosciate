
# def add(x,y):
#     return x+y
# res = add(int(input('enter x:')),int(input("enter y:")))
# print(res) 
# import logging

# logging.basicConfig(filename="add_config.txt" ,level=logging.DEBUG)
# logging.debug("This is debug")
# logging.info("Program started")
# logging.warning("Warning info")
# logging.error("Error info")
# logging.critical("Critical info")


################################################

import logging

logging.basicConfig(
    filename="add_config.txt",
    level=logging.DEBUG,
    filemode="a"
)

def add(x, y):
    return x + y

logging.info("Program started")
logging.debug("This is debug")
logging.info("Program started")
logging.warning("Warning info")
logging.error("Error info")
logging.critical("Critical info")

try:
    x = int(input("enter x: "))
    y = int(input("enter y: "))
    res = add(x, y)
    print(res)                     # shows on screen
    logging.info(f"Result: {res}") # stored in log file

except Exception as e:
    logging.error(f"Error occurred: {e}")

logging.info("Program ended")
logging.debug("This is debug")
logging.info("Program started")
logging.warning("Warning info")
logging.error("Error info")
logging.critical("Critical info")
