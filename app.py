import os
from dotenv import load_dotenv
import chromadb
from openai import OpenAI
from chromadb.utils import embedding_functions

# Load environment variables/api keys
load_dotenv()
openapi_api_key = os.getenv("OPENAI_API_KEY")
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openapi_api_key, model_name="gpt-3.5-turbo")

# Initialize Vector Database
chroma_client = chromadb.PersistentClient(path="chroma_persistent_storage")
collection = "documents"
collection = chroma_client.get_or_create_collection(
    name=collection, embedding_function=openai_ef)


# OpenAI client initialization
client = OpenAI(api_key=openapi_api_key)
client.chat.completions.create(
    model="gpt-3.5-turbo",
    
)