from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load JSON data from the file
json_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
with open(json_path, "r") as f:
    student_data = json.load(f)

# Create a name → marks dictionary for fast lookup
student_marks = {entry["name"]: entry["marks"] for entry in student_data}

@app.get("/")
def home():
    return {"marks": []}

@app.get("/api")
def get_marks(name: Optional[list[str]] = Query(None)):
    if not name:
        return {}
    return {"marks": [student_marks.get(n, None) for n in name]}
