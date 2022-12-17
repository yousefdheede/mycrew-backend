from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException , Form ,Body
from model import Gender, Job, Job_update, Role, User, user_update 

jobapp= FastAPI()

db: List[Job] = [
      Job(
         job_id=uuid4(),
         job_title="teacher",
         job_description="str",
         job_email="job@gmail.com",
         job_password="job", 
         job_location="44.234",
         job_phone="832732987423"
        )
    ]


@jobapp.get("/api/mycrew/job/getall") 
async def get_all_jobs():
   return db; 


@jobapp.delete("/api/mycrew/job/delete/{job_title}") 
async def delete_job(job_title:str):
 for Job in db :
    if Job.job_title == job_title:
         db.remove(Job)
         return
            
    raise HTTPException(
            status_code=404,
            detail=f"user with job_title: {job_title} does not exists"
        )

@jobapp.put("/api/mycrew/job/updatejob/{job_title}") 
async def update_job(Job_update:Job_update,job_title:str):
   for Job in db :
      if Job.job_title == job_title:
         if Job_update.job_description is not None:
                Job.job_description=Job_update.job_description
         if Job_update.job_email is not None:
            Job.job_email =Job_update.job_email
          
      return
   raise HTTPException( 
                        status_code=404, 
                        detail=f"user with job_title :{job_title} does not exists"
                        )       


@jobapp.put("/api/mycrew/job/addjob") 
async def add_job(job:Job):
      db.append(job);
      return
 



