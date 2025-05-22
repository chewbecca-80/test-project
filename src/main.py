from fastapi import FastAPI
from app.models import Note, notes

app = FastAPI()

# endpoint to test server health
@app.get(
    "/health",
    responses={
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
        500: {"description": "Internal Server Error"},
    },
)

@app.get("/notes")
def get_notes():
    return notes

@app.post("/notes")
def create_note(note: Note):
    notes.append(note)
    return {"message": "Note added."}

@app.delete("/notes/{index}")
def delete_note(index: int):
    if 0 <= index < len(notes):
        notes.pop(index)
        return {"message": "Note deleted."}
    return {"error": "Invalid index"}
