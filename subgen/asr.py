# asr.py
from faster_whisper import WhisperModel
from pathlib import Path
import typer

def transcribe_audio(
    wav_file: str,
    model_size: str = "medium",
    language: str = "auto"
) -> list[dict]:
    wav_path = Path(wav_file)
    if not wav_path.exists():
        raise FileNotFoundError(f"Ses dosyası bulunamadı: {wav_file}")

    typer.echo(f"📝 Transkripsiyon başlıyor: {wav_file} (model={model_size}, dil={language})")

    # CPU için ayar
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    segments, info = model.transcribe(
        str(wav_path),
        beam_size=5,
        language=None if language == "auto" else language
    )

    typer.echo(f"   Algılanan dil: {info.language} (prob={info.language_probability:.2f})")

    results = []
    for seg in segments:
        results.append({
            "start": seg.start,
            "end": seg.end,
            "text": seg.text.strip()
        })

    typer.echo(f"✅ Transkripsiyon tamamlandı. {len(results)} segment bulundu.")
    return results
