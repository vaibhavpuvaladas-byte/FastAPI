from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator , model_validator , computed_field
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int 
    weight: float
    height : float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_BMI(self) -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi
def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.calculate_BMI)
    print('updated')

patient_info = {
    'name': 'nitish', 
    'email': 'abc@hdfc.com',  # Changed to pass the domain validation
    'linkedin_url': 'http://linkedin.com/1322', 
    'age': 30,  # Changed from string '30' to int 30 (though Pydantic auto-casts)
    'weight': 75.2,
    'height':165,
    'contact_details': {'phone': '2353462'}, 
    'married': True,
    'allergies': ['peanuts'] 
}

patient1 = Patient(**patient_info)

# Corrected function call to match the definition
update_patient(patient1) 