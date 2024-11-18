
def write_srt(segments, output_path):
    with open(output_path, "w", encoding="utf-8") as srt_file:
        for i, seg in enumerate(segments):
            start_time = format_timestamp(seg["start"])
            end_time = format_timestamp(seg["end"])
            srt_file.write(f"{i+1}\n{start_time} --> {end_time}\n{seg['text']}\n\n")

def format_timestamp(seconds):
    millis = int((seconds % 1) * 1000)
    seconds = int(seconds)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{millis:03}"
