from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Set up SQLite database
engine = create_engine("sqlite:///mycrew.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Define model for job posting
class Job(BaseModel):
    id: int
    title: str
    company: str

# Create table for job postings in the database
engine.execute("CREATE TABLE jobs (id INTEGER PRIMARY KEY, title TEXT, company TEXT)")

app = FastAPI()

@app.post("/jobs")
async def create_job(job: Job):
    # Add job to the database
    new_job = Job(id=job.id, title=job.title, company=job.company)
    session.add(new_job)
    session.commit()
    return {"message": "Successfully added job"}

@app.get("/jobs")
async def search_jobs(
    title: str = Query(None, min_length=3, max_length=100),
    company: str = Query(None, min_length=3, max_length=100)
):
    results = session.query(Job)
    if title:
        results = results.filter(Job.title.contains(title))
    if company:
        results = results.filter(Job.company.contains(company))
    return results.all()
