
from dataclasses import dataclass

from src.job import Job
from src.job_application import JobApplication


@dataclass
class JobContext:
    job: Job = None
    job_application: JobApplication = None
