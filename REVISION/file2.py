import requests
import yaml,json
import logging

logging.basicConfig(
    filename= "revision.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.info("parsing started")

    logging.info("gettign yaml file")
    with open("revision1.yaml","r") as f:
        y_data = yaml.safe_load(f)
    logging.info("yaml loaded")

    logging.info("conrting to json")
    with open ("revision.json","w")as f:
        json.dump(y_data,f,indent=2)
    
except FileNotFoundError as e:
    logging.error(".yaml file not found")

except Exception as e:
    logging.critical("Unexpected error")
    print("check for the file")

