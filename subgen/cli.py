import typer
from pathlib import Path
from subgen.audio import extract_audio
from subgen.asr import transcribe_audio
from subgen.translate import translate_segments
from subgen.exporter import save_srt, save_txt

app = typer.Typer(help="SubGen: MP4/MP3 dosyalarını altyazıya çevirir.")

@app.command()
def transcribe(
    input_file: str = typer.Argument(..., help="MP4 veya MP3 dosya yolu"),
    formats: list[str] = typer.Option(["srt"], help="Çıktı formatları: srt, txt, docx"),
    out_dir: str = typer.Option(".", help="Çıktıların kaydedileceği klasör"),
    model: str = typer.Option("medium", help="Whisper modeli: tiny, base, small, medium, large-v3"),
    language: str = typer.Option("auto", help="Orijinal dil (örn: tr, en, auto)"),
    target_lang: str = typer.Option(None, help="Çevrilecek hedef dil (örn: tr, en, fr, de)")  # 👈 burası eklendi
):
    input_path = Path(input_file)
    if not input_path.exists():
        typer.echo(f"❌ Dosya bulunamadı: {input_file}")
        raise typer.Exit(code=1)

    typer.echo("🔹 SubGen başlatılıyor...")

    # 1. Ses çıkarma
    wav_file = extract_audio(input_file, out_dir)

    # 2. Transkripsiyon
    segments = transcribe_audio(str(wav_file), model, language)

    # 3. Opsiyonel çeviri
    if target_lang:
        typer.echo(f"🌍 Çeviri yapılıyor → {target_lang}")
        segments = translate_segments(segments, target_lang)

    # 4. Çıktı (şimdilik ekrana yaz)
    typer.echo("\n--- ALT YAZI ---")
    for seg in segments[::]:
        typer.echo(f"[{seg['start']:.2f} → {seg['end']:.2f}] {seg['text']}")
    
    # 5. Dosyaya kaydetme
    
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for fmt in formats:
        out_file = out_dir / f"{input_path.stem}_{target_lang or language}.{fmt}"
        if fmt == "srt":
            save_srt(segments[::], out_file)
        elif fmt == "txt":
            save_txt(segments[::], out_file)
        else:
            typer.echo(f"⚠️ Desteklenmeyen format: {fmt}")
            continue
        typer.echo(f"✅ Kaydedildi: {out_file}")

if __name__ == "__main__":
    app()
