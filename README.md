# YouTube Chatbot with Langchain, RAG, Cohere Embedding, Chroma DB, LLama3, and Ollama

## Overview
This project leverages Langchain, RAG, Cohere Embedding, Chroma DB, LLama3, and Ollama to create a YouTube Chatbot. The chatbot can summarize YouTube videos and answer questions based on the video's transcript.

## Features
- **Video Summarization**: Generate concise summaries of YouTube videos.
- **Question Answering**: Answer questions related to the content of YouTube videos using their transcripts.
- **Advanced Embeddings**: Utilize Cohere Embedding for efficient and accurate text representation.
- **Robust Vector Database**: Store and retrieve data using Chroma DB.
- **Powerful Language Models**: Employ LLama3 and Ollama for natural language understanding and generation.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/SOURABHMISHRA5221/YoutubeVideoChatBotLLM.git
    cd YoutubeVideoChatBotLLM
    ```

## Usage
1. Run the main script:
    ```bash
    pip install -r requirements.txt
    python ChatBot.py
    ```
2. Interact with the chatbot through the provided interface.

## Configuration
- Make sure to add .env file. Ensure that the .env file contains the correct values for:
- MODEL_URL (the URL for your LLama3 or Ollama model)
- COHERE_API_KEY (your API key for Cohere embeddings)

## Acknowledgements
- Langchain
- Cohere
- Chroma DB
- LLama3
- Ollama

## To Host llama3 or any model locally checkout : 
- [Hosting LLM Locally](https://github.com/SOURABHMISHRA5221/LocalLLM)
