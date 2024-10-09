from Transcript import get_transcript
from RAGChain   import chat



def chat_bot():
	get_transcript()
	chat()
	return

if __name__ == "__main__":
	chat_bot()