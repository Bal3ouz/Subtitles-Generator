
# Video Transcription and Translation Service

## Overview
This FastAPI-based service transcribes YouTube/Dailymotion videos, translates them into a target language, and saves the output as an `.srt` file.

### Features
- Transcribe videos using OpenAI's Whisper.
- Translate subtitles with Google Translate.
- Serve as a RESTful API endpoint.

## Installation

1. Clone the repository.
2. Build the Docker image:
   ```
   docker-compose build
   ```
3. Start the service:
   ```
   docker-compose up
   ```

## Usage

Send a POST request to `http://localhost:8000/transcribe_and_translate/` with the following JSON payload:
```json
{
    "video_url": "https://www.youtube.com/watch?v=example",
    "target_language": "es"
}
```

## Output

The response includes the `.srt` file path with translated subtitles.
