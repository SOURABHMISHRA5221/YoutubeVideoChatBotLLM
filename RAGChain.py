import bs4
import os

from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatCohere
from langchain_community.embeddings import CohereEmbeddings
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv




#Loading and Setting Environment Variables
load_dotenv()

model_url = os.getenv("MODEL_URL")
cohere_api_key = os.getenv("COHERE_API_KEY")



#Creating Model Instance
llm = Ollama(model="llama3",base_url=model_url)



#Loading Transcript data
loader = TextLoader("transcript.txt")
document = loader.load()

#Breaking Big Document Into Chunks with overlap to provide a little internal context
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(document)


#Initializing Vector Store
vectorstore = Chroma.from_documents(documents=splits, embedding=CohereEmbeddings(user_agent="my-app",cohere_api_key=cohere_api_key))

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)



def chat():
    print("Welcome to Youtube ChatBot!")
    print("Type \"exit\"  to exit")
    response = input("question: ")
    while (response != "exit"):
        print(rag_chain.invoke(response))
        response = input("question: ")

