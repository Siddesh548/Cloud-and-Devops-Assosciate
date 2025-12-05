from typing import Annotated
from pydantic import BaseModel,ValidationError
import json
import logging

logging.basicConfig(
    filename="api_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class User(BaseModel):
    id:int
    name:str

with open("user.json",'r') as f:
    data = json.load(f)

# user_details = User(**data)
# print(data.id)

user_details = []
for item in data:
    try:
        u = User(**item)
        user_details.append(u)
    except ValidationError as e:
        print(f"Validation error: {e}")
        logging.error("Name should be in string")
for user in user_details:
    print(user.id, user.name)