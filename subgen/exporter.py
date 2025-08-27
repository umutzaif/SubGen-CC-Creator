from pathlib import Path

def format_timestamp(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def save_srt(segments, out_path: Path):
    with open(out_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, 1):
            start = format_timestamp(seg["start"])
            end = format_timestamp(seg["end"])
            f.write(f"{i}\n{start} --> {end}\n{seg['text']}\n\n")

def save_txt(segments, out_path: Path):
    with open(out_path, "w", encoding="utf-8") as f:
        for seg in segments:
            f.write(f"{seg['text']}\n")
