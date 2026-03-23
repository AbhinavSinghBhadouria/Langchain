from pydantic import BaseModel


class Student(BaseModel):
    name:str    # to use default value just use      name:str ='nitesh'


new_student={'name': 'abhinav'}

student= Student(**new_student)

print(student)