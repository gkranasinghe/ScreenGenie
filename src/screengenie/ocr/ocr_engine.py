from screengenie.helpers.config import load_config

try:
    import pytesseract
except ImportError:
    pytesseract = None


class OCREngine:
    def __init__(self):
        cfg = load_config()
        self.language = cfg.get("ocr", {}).get("language", "eng")

    def extract_text(self, image):
        """Perform OCR on the provided image and return extracted text."""
        if pytesseract is None:
            return "[OCR Engine not available]"

        try:
            text = pytesseract.image_to_string(image, lang=self.language)
            return text
        except Exception as e:
            return f"[OCR Error] {e}"
