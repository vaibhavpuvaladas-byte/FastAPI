from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator , model_validator
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int 
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value: str):
        valid_domains = ['hdfc.com', 'icici.com']
        # EmailStr validation happens first, so 'value' is already a valid email format
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError(f'Not a Valid Domain. Allowed domains: {valid_domains}')
        return value


    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return self

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {
    'name': 'nitish', 
    'email': 'abc@hdfc.com',  # Changed to pass the domain validation
    'linkedin_url': 'http://linkedin.com/1322', 
    'age': 30,  # Changed from string '30' to int 30 (though Pydantic auto-casts)
    'weight': 75.2,
    'contact_details': {'phone': '2353462'}, 
    'married': True,
    'allergies': ['peanuts'] 
}

patient1 = Patient(**patient_info)

# Corrected function call to match the definition
update_patient(patient1) 