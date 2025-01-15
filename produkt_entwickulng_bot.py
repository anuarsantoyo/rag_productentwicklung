import tkinter as tk
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
#from langchain_huggingface import HuggingFaceEmbeddings #used for locals
#from sentence_transformers import SentenceTransformer #used for locals
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import openai
from dotenv import load_dotenv
import os

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()
# ---- Set OpenAI API key
# Change environment variable name from "OPENAI_API_KEY" to the name given in
# your .env file.
openai.api_key = os.environ['OPENAI_API_KEY']

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Beantworte die Frage ausschließlich basierend auf folgendem Kontext:

{context}

---

Beantworte die Frage basierend auf dem obigen Kontext mit höchstens aber so kurz wie möglich mit auf jedem Fall weniger als {max_tokens}:{question}
"""

embedding_function = OpenAIEmbeddings()
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)


###################################################################################
max_tokens=1500
MAX_CHARACTERS=500
# Function to handle user input and display the response
def process_input():
    query_text = user_entry.get()  # Get the text from the input field
    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=2)
    relevant_text = [doc.page_content for doc, _score in results if _score > 0.7]

    if len(relevant_text) == 0:
        response = "Bitte können Sie die Frage genau formulieren, damit ich Ihnen besser helfen kann."
    else:
        if len(relevant_text) == 1:
            context_text = relevant_text[0]
        else:
            context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results[:2]])

        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text, max_tokens=max_tokens)
        model = ChatOpenAI(model='gpt-4o-mini',temperature=0.7, max_tokens=max_tokens)
        response = model.invoke(prompt).content

    # Display the user's input and response in the chat window
    chat_display.insert(tk.END, f"You: {query_text}\n")
    chat_display.insert(tk.END, f"Bot: {response}\n")

    # Clear the input field
    user_entry.delete(0, tk.END)

# Function to update character count and enforce the character limit
def update_character_count(*args):
    text = user_text_var.get()
    char_count = len(text)

    # Enforce character limit
    if char_count > MAX_CHARACTERS:
        user_text_var.set(text[:MAX_CHARACTERS])
        char_count = MAX_CHARACTERS

    # Update character count label
    char_count_label.config(text=f"{char_count}/{MAX_CHARACTERS}")


# Set up the main window
root = tk.Tk()
root.title("Produktentwicklung Bot")

# Make the root window resizable
root.geometry("600x400")  # Set initial size
root.rowconfigure(0, weight=1)  # Allow resizing for row 0
root.rowconfigure(1, weight=0)  # Fixed size for the entry field
root.rowconfigure(2, weight=0)  # Fixed size for the button
root.columnconfigure(0, weight=1)  # Allow resizing for column 0

# Display area for chat
chat_display = tk.Text(root, state="normal", wrap="word")
chat_display.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Frame for entry field and character count
entry_frame = tk.Frame(root)
entry_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

# Variable to track user input
user_text_var = tk.StringVar()
user_text_var.trace_add("write", update_character_count)

# Entry field for user input
user_entry = tk.Entry(entry_frame, textvariable=user_text_var)
user_entry.pack(side="left", fill="x", expand=True)

# Label to show character count
char_count_label = tk.Label(entry_frame, text=f"0/{MAX_CHARACTERS}")
char_count_label.pack(side="left", padx=5)

# Button to send the input
send_button = tk.Button(root, text="Send", command=process_input)
send_button.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

chat_display.insert(tk.END,"Bot: Wie kann Ich Ihnen behilflich sein?")
# Run the GUI main loop
root.mainloop()


