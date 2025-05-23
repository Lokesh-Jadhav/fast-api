from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    return {"message": "Use /api?name=X&name=Y to get marks."}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    # Return marks in the same order as names provided in query
    return {"marks": [student_marks.get(n, None) for n in name]}
