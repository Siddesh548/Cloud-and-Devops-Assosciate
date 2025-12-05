from typing import Annotated
from annotated_types import Gt
from pydantic import ValidationError,BaseModel

class MyClass(BaseModel):
    age: Annotated[int,Gt(18)]

#valid
# obj1 = MyClass(age='jk')
# # obj1.age = input("Enter the age:")
# print(obj1)

class main(MyClass):
    def ages(age):
        try:
            obj= MyClass(age=age)
            return "enterd age is integer"
        except ValidationError as e:
            return "age should be in intege"
obj = MyClass()
agee= input("enter age:")
re = main.ages(agee)
print(re)



# from typing import Annotated
# from annotated_types import Gt
# from pydantic import BaseModel, ValidationError

# class MyClass(BaseModel):
#     age: Annotated[int, Gt(18)]

# def ages(age):
#     try:
#         obj = MyClass(age=age)
#         return f"Valid age: {obj.age}"
#     except ValidationError as e:
#         return "Age must be an integer greater than 18"

# re = ages(input("Enter age: "))
# print(re)


