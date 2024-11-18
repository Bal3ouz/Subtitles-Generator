
import os
from pytube import YouTube
import whisper
from googletrans import Translator
from app.utils.srt_writer import write_srt

model = whisper.load_model("large")


def process_video(video_url, target_language):
    # Download video
    yt = YouTube(video_url)
    video_path = yt.streams.filter(only_audio=True).first().download()

    # Transcribe using Whisper
    result = model.transcribe(video_path)

    # Translate using Google Translate
    translator = Translator()
    translated_segments = [
        {"start": seg["start"], "end": seg["end"], "text": translator.translate(seg["text"], dest=target_language).text}
        for seg in result["segments"]
    ]

    # Save to SRT
    output_srt = f"{yt.title}.srt"
    write_srt(translated_segments, output_srt)
    os.remove(video_path)  # Cleanup downloaded video
    return output_srt
