from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import openai
from dotenv import load_dotenv
import os
import shutil
import json
#from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer


# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()
#---- Set OpenAI API key
# Change environment variable name from "OPENAI_API_KEY" to the name given in
# your .env file.
openai.api_key = os.environ['OPENAI_API_KEY']

CHROMA_PATH = "chroma"
DATA_PATH = "data/books"


def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    chunks = json_to_chunks(documents)
    save_to_chroma(chunks)


def load_documents():
    with open('data/output.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def json_to_chunks(json_file):
    chunks = [
        Document(
            page_content=f"{item['Problem']}\n{item['Lösung']}"
        )
        for item in json_file
    ]
    print(f"Split {len(chunks)} documents into {len(chunks)} chunks.")


    return chunks



def save_to_chroma(chunks: list[Document]):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new DB from the documents.  OpenAIEmbeddings(), HuggingFaceEmbeddings()

    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )
    #db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


if __name__ == "__main__":
    main()
