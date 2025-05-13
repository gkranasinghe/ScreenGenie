from screengenie.llm.model import LocalLLM

llm = LocalLLM()
reply = llm.generate("Give me 3 Git tips.")
print(reply)
