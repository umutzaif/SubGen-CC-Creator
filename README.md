# 🎬 SubGen - Otomatik Altyazı Oluşturucu

SubGen, MP4 veya MP3 dosyalarından **altyazı üretmeye** yarayan bir Python uygulamasıdır.  
Whisper tabanlı transkripsiyon yapar ve çıktıyı `.srt`, `.txt`, `.docx` gibi formatlarda kaydedebilir.  
Ayrıca farklı dillere çeviri desteği ve basit bir **GUI (PyQt5)** arayüzü vardır. 🚀

---

## ✨ Özellikler
- 🎤 MP4/MP3 dosyalarından ses çıkarma
- 📝 Whisper ile transkripsiyon
- 🌍 Altyazıyı farklı dillere çevirme
- 💾 Çıktı formatları: `srt`, `txt`, `docx`
- 🖥 GUI arayüz (PyQt5)
- 📦 `.exe` olarak paketlenebilir

---

## 📂 Proje Yapısı
```
CC_Creator/
├── subgen/
│ ├── init.py
│ ├── cli.py
│ ├── audio.py
│ ├── asr.py
│ ├── translate.py
│ ├── ui_qt.py
│ └── ...
├── dist/ # PyInstaller ile çıkan exe
├── build/
├── README.md
└── requirements.txt
```
---

## ⚙️ Kurulum

### 1. Depoyu klonla
```git clone https://github.com/<kullanıcı-adın>/CC_Creator.git```
```cd CC_Creator```
```python -m venv .venv```
```.venv\Scripts\activate```   
### Windows
```pip install -r requirements.txt```

## 🚀 Kullanım
### Komut Satırı (CLI)

Altyazı üretmek için:
python -m subgen.cli input.mp4 --formats srt txt --out-dir output --language auto --target-lang tr

### GUI (PyQt5)

Kullanıcı dostu arayüzü başlatmak için:

```python -m subgen.ui_qt```

### EXE (Windows)

Eğer .exe derlenmişse:

dist/SubGen.exe

### 📦 EXE Derleme

PyInstaller kullanarak exe oluştur:

```pip install pyinstaller```
```pyinstaller --onefile --noconsole -n SubGen subgen/ui_qt.py```
Oluşan dosya dist/SubGen.exe içinde bulunur.

## 📝 Gereksinimler

- Python 3.10+

- ffmpeg
 (ses çıkarma için)

## 📚 Kütüphaneler:

- openai-whisper

- typer

- python-docx

- pypandoc

- PyQt5

- pyinstaller

(Tüm bağımlılıklar requirements.txt içinde listelenmiştir.)

## 🌍 Lisans

MIT License © 2025 - Umut Zaif
