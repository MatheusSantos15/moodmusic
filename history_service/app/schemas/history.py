from pydantic import BaseModel

class HistoryCreate(BaseModel):
    user_id: int
    song_id: int
    