import sqlite3
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dbconn = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./mycrew.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



def get_db():
    conn = sqlite3.connect("mycrew.db")
    return 


# Define model for job posting
class Job(BaseModel):
    id: int
    company: str
    job_title: str
    job_description: str
    job_email: str
    job_password: str
    job_location: str
    job_phone: str

# Create table for job postings in the database
engine.execute("CREATE TABLE jobs (id INTEGER PRIMARY KEY, title TEXT, company TEXT)")



@dbconn.post("/jobs/create_job")
async def create_job(job: Job):
    # Add job to the database
    new_job = Job(id=job.id, title=job.title, company=job.company)
    session.add(new_job)
    session.commit()
    return {"message": "Successfully added job"}

@dbconn.get("/jobs/search_jobs")

async def search_jobs(
    job_title: str = Query(None, min_length=3, max_length=100),
    company: str = Query(None, min_length=3, max_length=100)
):
    results = session.query(Job)
    if job_title:
        results = results.filter(Job.job_title.contains(job_title))
    if company:
        results = results.filter(Job.company.contains(company))
    return results.all()


@dbconn.get("/jobs/search_jobs")
async def get_user(job_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs WHERE id=?", (id,))
    results = cursor.fetchone()
    return {"JOB": results}