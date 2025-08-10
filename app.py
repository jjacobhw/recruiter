from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

# Vector DB Setup
load_dotenv()
loader = CSVLoader(file_path="data/Recruiter.csv")
documents = loader.load()
embedding = OllamaEmbeddings(model="llama3")
vectorstore = Chroma.from_documents(documents, embedding)
retriever = vectorstore.as_retriever()
model = OllamaLLM(model="llama3", temperature=0.1)

template = """You are an exeprt in answering questions about the data provided:
here is the question: {question}"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

result = chain.invoke({"question": "What is the capital of France?"})

print(result)