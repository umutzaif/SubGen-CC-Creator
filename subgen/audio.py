import subprocess
from pathlib import Path
import typer

def extract_audio(input_file: str, output_dir: str = ".", sample_rate: int = 16000) -> Path:
    """
    Verilen mp4/mp3 dosyasından wav formatında ses çıkarır.
    
    Args:
        input_file (str): Girdi medya dosyası (mp4/mp3).
        output_dir (str): Çıkış klasörü.
        sample_rate (int): Çıkış ses örnekleme hızı (default 16kHz).
    
    Returns:
        Path: Oluşan wav dosyasının yolu.
    """
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Girdi dosyası bulunamadı: {input_file}")

    output_path = Path(output_dir) / (input_path.stem + ".wav")

    cmd = [
        "ffmpeg",
        "-y",                # üzerine yaz
        "-i", str(input_path),
        "-ar", str(sample_rate),   # örnekleme hızı
        "-ac", "1",          # mono kanal
        str(output_path)
    ]

    typer.echo(f"🎵 Ses çıkarılıyor: {input_path} → {output_path}")
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        raise RuntimeError("ffmpeg ile ses çıkarma başarısız oldu!")

    return output_path
