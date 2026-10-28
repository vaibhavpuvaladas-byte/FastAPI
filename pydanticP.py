from pydantic import BaseModel , Field , EmailStr , AnyUrl
from typing import List, Dict , Annotated , Optional

class Patient(BaseModel):
    name:Annotated[str , Field(max_length = 50 , title = 'Name of the Paients' , description ='give the name of the patient in not more than 50 characters ')]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0 ,lt=100)
    weight: Annotated[float , Field(gt=0 , strict=True)]
    married: Annotated[bool , Field(default=None , description='The patient is married or not')]
    allergies: Annotated[Optional[List[str]] , Field(default=None , max_length=5)]
    contact_details: Dict[str, str]

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {
    'name': 'nitish', 
    'email': 'abc@gmail.com', 
    'linkedin_url': 'http://linkedin.com/1322', # Pydantic ignores extra fields by default
    'age': '30', 
    'weight': 75.2,
    'contact_details': {'phone': '2353462'}, 
    'married': True,
    'allergies': ['peanuts'] 
}

patient1 = Patient(**patient_info)

# Corrected function call to match the definition
update_patient(patient1)