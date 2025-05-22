from fastapi import FastAPI
from app.models import Note, notes

api = FastAPI()

# endpoint to test server health
@api.get(
    "/health",
    responses={
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
        500: {"description": "Internal Server Error"},
    },
)

@api.get("/notes")
def get_notes():
    return notes

@api.post("/notes")
def create_note(note: Note):
    notes.append(note)
    return {"message": "Note added."}

@api.delete("/notes/{index}")
def delete_note(index: int):
    if 0 <= index < len(notes):
        notes.pop(index)
        return {"message": "Note deleted."}
    return {"error": "Invalid index"}
