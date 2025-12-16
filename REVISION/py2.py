import yaml
import json
import logging

class APIResponseError(Exception):
    pass

logging.basicConfig(
    filename='3gpps.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def analyze_apis():

    #files = glob.glob("3GGPP/3gpp/*.yaml")[:5]
    summary = []
    for file_path in files:
        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)

           
            info = data.get("info", {})
            title = info.get("title")
            description = info.get("description")
            version = info.get("version")

            security_list = data.get("security", [])

            for item in security_list:
                return list(item.keys())[0]


        except FileNotFoundError as e:
            logging.error("check the path")
