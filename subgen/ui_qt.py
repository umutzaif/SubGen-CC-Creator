import sys
from pathlib import Path
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QFileDialog, QComboBox, QMessageBox, QCheckBox
)

# SubGen modülleri
from subgen.audio import extract_audio
from subgen.asr import transcribe_audio
from subgen.translate import translate_segments
from subgen.exporter import save_srt, save_txt


class SubGenApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎬 SubGen - Altyazı Oluşturucu")
        self.setGeometry(200, 200, 400, 250)

        layout = QVBoxLayout()

        # Kullanıcıya dosya seçme uyarısı
        self.label = QLabel("Bir MP4 veya MP3 dosyası seçin")
        layout.addWidget(self.label)

        # Dosya seçme butonu
        self.btn_select = QPushButton("🎵 Dosya Seç")
        self.btn_select.clicked.connect(self.select_file)
        layout.addWidget(self.btn_select)

        # Model seçimi
        self.model_box = QComboBox()
        self.model_box.addItems(["tiny", "base", "small", "medium", "large-v3"])
        layout.addWidget(QLabel("Model Seç"))
        layout.addWidget(self.model_box)

        # Orijinal dil seçimi
        self.lang_box = QComboBox()
        self.lang_box.addItems(["auto", "tr", "en", "de", "fr", "es"])
        layout.addWidget(QLabel("Orijinal Dil"))
        layout.addWidget(self.lang_box)

        # Çeviri hedef dili
        self.target_box = QComboBox()
        self.target_box.addItems(["", "tr", "en", "de", "fr", "es"])
        layout.addWidget(QLabel("Hedef Dil (opsiyonel)"))
        layout.addWidget(self.target_box)

        # Çıktı formatları
        self.chk_srt = QCheckBox("SRT kaydet")
        self.chk_srt.setChecked(True)
        layout.addWidget(self.chk_srt)

        self.chk_txt = QCheckBox("TXT kaydet")
        layout.addWidget(self.chk_txt)

        # Çalıştırma butonu
        self.btn_run = QPushButton("🚀 Altyazı Oluştur")
        self.btn_run.clicked.connect(self.run_subgen)
        layout.addWidget(self.btn_run)

        self.setLayout(layout)
        self.input_file = None

    def select_file(self):
        """Dosya seçme dialogu"""
        file, _ = QFileDialog.getOpenFileName(
            self, "Dosya Seç", "", "Video/Audio (*.mp4 *.mp3)"
        )
        if file:
            self.input_file = Path(file)
            self.label.setText(f"Seçilen dosya: {self.input_file.name}")

    def run_subgen(self):
        """Altyazı oluşturma işlemi"""
        if not self.input_file:
            QMessageBox.warning(self, "Hata", "Lütfen bir dosya seçin!")
            return

        out_dir = Path("outputs")
        out_dir.mkdir(exist_ok=True)

        # 1. Ses çıkarma
        wav_file = extract_audio(str(self.input_file), out_dir)

        # 2. Transkripsiyon
        segments = transcribe_audio(
            str(wav_file),
            self.model_box.currentText(),
            self.lang_box.currentText()
        )

        # 3. Opsiyonel çeviri
        if self.target_box.currentText():
            segments = translate_segments(segments, self.target_box.currentText())

        # 4. Kaydetme
        if self.chk_srt.isChecked():
            save_srt(segments, out_dir / f"{self.input_file.stem}.srt")
        if self.chk_txt.isChecked():
            save_txt(segments, out_dir / f"{self.input_file.stem}.txt")

        QMessageBox.information(self, "Tamamlandı", f"Altyazılar {out_dir} klasörüne kaydedildi ✅")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SubGenApp()
    window.show()
    sys.exit(app.exec_())
