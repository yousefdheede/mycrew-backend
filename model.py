

from enum import Enum, unique
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

class Gender(str,Enum) : 
    male="male" 
    female="female" 
    
class Role(str,Enum) : 
     admin="admin" 
     client="client"
     company="company"
     
class specification(str,Enum): 
    specification_title="CE"     
     
class Job(BaseModel):
    job_id:Optional[UUID]= uuid4() 
    job_title: str 
    job_description: str 
    job_email: str
    job_password: str 
    job_location: float
    job_specification: List[specification]
    job_phone=int


   
class User(BaseModel): 
    id: Optional[UUID] = uuid4()
    username: Optional[str]= uuid4()
    first_name :str 
    last_name: str 
    email: str
    password: str
    location: float
    gender: Gender
    roles: List[Role]
    skill: str
    phonenumber: int 
    
class user_update(BaseModel): 
    first_name :Optional[str] 
    last_name: Optional[str]  
    email: Optional[str] 
    password: Optional[str] 
    location: Optional[float]
    roles: Optional[ List[Role]]
    skill: Optional[str] 
    phonenumber: Optional[int]     
    

    
    
    
     