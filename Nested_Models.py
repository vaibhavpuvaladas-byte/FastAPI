from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    age: int 
    weight: float
    height: float
    gender: str
    address: Address 

# 1. Changed 'State' to 'state' to match the Address model
address_dict = {'city': 'Jamshedpur', 'state': 'Jharkhand', 'pin': '831004'}

address1 = Address(**address_dict)

# 2. Added the required 'weight' and 'height' fields
patient_dict = {
    'name': 'Sai', 
    'gender': 'Male', 
    'age': 19, 
    'weight': 65.5, 
    'height': 175.0, 
    'address': address1
}

patient1 = Patient(**patient_dict)

# 3. Changed 'patient' to 'patient1'
print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)