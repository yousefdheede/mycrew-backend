from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException , Form ,Body
from model import Gender, Job, Role, User, user_update 

app= FastAPI() 

db: List[User] = [ 
     User(
      id=uuid4(),
      username="dana",
      first_name="Dana",
      last_name="Hassoun",
      email="dana@gmail.com",
      password="danahassoun",
      location="44.34",
      gender=Gender.female,
      roles=[Role.client],
      skill="css,c++,datastructures",
      phonenumber="042468010"
      ),   
      User(
      id=uuid4(),
      username="yousef",
      first_name="Yousef",
      last_name="Dheede",
      email="yousef@gmail.com",
      password="yousefdheede",
      location="55.55",
      gender=Gender.male, 
      roles=[Role.admin],
      skill="css,c++,datastructures",
      phonenumber="0595746019"
      )              
]

@app.get("/api/mycrew/users") #get all users
async def fetch_users(): 
   return db;


@app.get("/api/mycrew/users/{username}") #search for user 
async def search_user(username: str):
    for user in db:
        if user.username==username: 
            return user 

 

@app.post("/api/mycrew/register") # add new yser
async def register_user(user: User):
    db.append(user) 
    return{user} 

@app.delete("/api/mycrew/users/{username}") #delete user 
async def delete_user(username: str):
    for user in db:
        if user.username == username:
            db.remove(user)
            return
        raise HTTPException(
            status_code=404,
            detail=f"user with username: {username} does not exists"
        )
        
@app.put("/api/mycrew/users/{user_id}") #update fun
async def update_user(user_update: user_update, user_id: UUID ):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name=user_update.first_name
            if user_update.last_name is not None:
                user.last_name=user_update.last_name
            if user_update.email is not None:
                user.email=user_update.email
            if user_update.password is not None:
                user.password=user_update.password
            if user_update.location is not None:
                user.location=user_update.location
            if user_update.roles is not None:
                user.roles=user_update.roles
            if user_update.skill is not None:
                user.skill=user_update.skill
            if user_update.phonenumber is not None:
                user.phonenumber=user_update.phonenumber
            return
    raise HTTPException( 
                        status_code=404, 
                        detail=f"user with user_id :{user_id} does not exists"
                        )     
    
@app.put("/api/mycrew/users/{username}") #update fun
async def update_user(user_update: user_update, username: UUID ):
    for user in db:
        if user.username == username:
            if user_update.first_name is not None:
                user.first_name=user_update.first_name
            if user_update.last_name is not None:
                user.last_name=user_update.last_name
            if user_update.email is not None:
                user.email=user_update.email
            if user_update.password is not None:
                user.password=user_update.password
            if user_update.location is not None:
                user.location=user_update.location
            if user_update.roles is not None:
                user.roles=user_update.roles
            if user_update.skill is not None:
                user.skill=user_update.skill
            if user_update.phonenumber is not None:
                user.phonenumber=user_update.phonenumber
            return
    raise HTTPException( 
                        status_code=404, 
                        detail=f"user with username :{username} does not exists"
                        )    
    
    
    
    
@app.post("/api/mycrew/login/")
async def login(email:str =Form() , password: str = Form()): 
    for user in db: 
        if email== user.email:
            if password == user.password: 
                return user
        


