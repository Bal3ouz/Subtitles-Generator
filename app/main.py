from fastapi import FastAPI, HTTPException
from app.services.video_handler import process_video

app = FastAPI()

@app.post("/transcribe_and_translate/")
async def transcribe_and_translate(video_url: str, target_language: str):
    try:
        srt_file_path = process_video(video_url, target_language)
        return {"message": "Processing successful", "srt_file": srt_file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
