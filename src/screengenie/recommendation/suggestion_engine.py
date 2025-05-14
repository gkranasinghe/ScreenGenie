class SuggestionEngine:
    def __init__(self):
        pass

    def get_suggestions(self, llm_output, context=None):
        if not llm_output:
            return ["[No suggestion from LLM]"]
        return [llm_output.strip()]