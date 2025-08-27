from deep_translator import GoogleTranslator

def translate_segments(segments: list[dict], target_lang: str = "tr") -> list[dict]:
    """
    Segmentleri verilen hedef dile çevirir.
    
    Args:
        segments (list[dict]): Transkripsiyon segmentleri.
        target_lang (str): Hedef dil (örn: 'tr', 'en', 'fr', 'de').
    
    Returns:
        list[dict]: Çevrilmiş segmentler.
    """
    translator = GoogleTranslator(source="auto", target=target_lang)
    translated = []
    for seg in segments:
        translated.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": translator.translate(seg["text"])
        })
    return translated
