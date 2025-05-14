from screengenie.ocr.ocr_engine import OCREngine
from screengenie.llm.model import LocalLLM
from screengenie.recommendation.suggestion_engine import SuggestionEngine

ocr = OCREngine()
llm = LocalLLM()
recommender = SuggestionEngine()

def run_pipeline_from_image(image):
    text = ocr.extract_text(image)
    llm_output = llm.generate(text)
    suggestions = recommender.get_suggestions(llm_output)
    return suggestions